import argparse
import os
import subprocess
import shutil
from shutil import copytree, ignore_patterns
import sys
from pathlib import Path

import toml

def clear_folder(dir):
    if os.path.exists(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    if file_path.endswith(".so"):
                        Path(file_path).unlink(missing_ok=True)
                else:
                    clear_folder(file_path)
                    with os.scandir(file_path) as d:
                        if not any(d):
                            shutil.rmtree(file_path, ignore_errors=True)
                    if file_path.endswith(".egg-info") or file_path.endswith("target") or file_path.endswith("build"):
                        shutil.rmtree(file_path, ignore_errors=True)
            except Exception as e:
                print(e)

def prerunclean(wd, appname, appversion):
    os.chdir(wd)
    shutil.rmtree(".venv", ignore_errors=True)
    clear_folder(wd)
    process = subprocess.Popen(
        ["py3clean", appname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    process.wait()

def stage(wd, appname, appversion):
    os.chdir(wd)
    os.makedirs(".builddebwd", exist_ok=True)
    shutil.copytree(os.getcwd(), ".builddebwd/" + appname, ignore=ignore_patterns('.*',"release"))
    shutil.copytree(os.getcwd(), ".builddebwd/" + appname + "-" + appversion, ignore=ignore_patterns('.*',"release"))

    os.chdir(".builddebwd/" + appname + "-" + appversion)

    shutil.rmtree(".git", ignore_errors=True)
    shutil.rmtree(".github", ignore_errors=True)
    shutil.rmtree(".tmp", ignore_errors=True)
    shutil.rmtree(".envs", ignore_errors=True)
    shutil.rmtree(".auth", ignore_errors=True)
    shutil.rmtree(".repo", ignore_errors=True)
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    Path(".gitignore" ).unlink(missing_ok=True)        
    Path("activate.sh" ).unlink(missing_ok=True)
    Path("Vagrantfile" ).unlink(missing_ok=True)
    Path("Makefile" ).unlink(missing_ok=True)
    Path("builddeb.py" ).unlink(missing_ok=True)
    Path("builddeb.sh" ).unlink(missing_ok=True)
    Path("pyproject.toml.old" ).unlink(missing_ok=True)

def gatherartifacts(wd, appname, appversion):
    os.chdir(wd)
    os.makedirs("release", exist_ok=True)
    debname = appname + "_" + appversion + "_amd64.deb"
    shutil.move('.builddebwd/' + debname, "release/" + debname)

def postrunclean(wd, appname, appversion):
    os.chdir(wd)
    shutil.rmtree(".builddebwd", ignore_errors=True)
    shutil.move('pyproject.toml.old', 'pyproject.toml')

def invoke(wd, appname, appversion):
    os.chdir(wd)
    process = subprocess.Popen(
        ["dpkg-buildpackage", "-uc", "-us"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    for line in process.stdout:
        sys.stdout.write(str(line, 'utf-8'))

def modifyproject(wd, appname, appversion):
    os.chdir(wd)
    with open('pyproject.toml', 'r') as f:
        config = toml.load(f)
    print(config["project"]["dependencies"])
    dependencies = config["project"]["dependencies"]
    dependencies.append("ext @ file:///vagrant/extensions/ext")
    dependencies.append("extc @ file:///vagrant/extensions/extc")
    dependencies.append("extcython @ file:///vagrant/extensions/extcython")
    dependencies.append("extrust @ file:///vagrant/extensions/extrust")
    config["project"]["dependencies"] = dependencies
    shutil.copyfile('pyproject.toml', 'pyproject.toml.old')
    with open('pyproject.toml', 'w') as f:
        toml.dump(config, f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('build', help='build')
    parser.add_argument('--path', "-p", help='path')
    args = parser.parse_args()
    if args.build:
        appversion = "0.1.0"
        appname = args.path

        prerunclean("/vagrant", appname, appversion)
        modifyproject("/vagrant", appname, appversion)
        stage("/vagrant", appname, appversion)
        invoke("/vagrant/.builddebwd/" + appname + "-" + appversion, appname, appversion)
        gatherartifacts("/vagrant", appname, appversion)
        postrunclean("/vagrant", appname, appversion)

if __name__ == '__main__':
    main()
