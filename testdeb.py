import argparse
import os
import sys
import subprocess
import shutil

process = subprocess.Popen(
    ["apt-get", "remove", "template", "-y"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
(output, err) = process.communicate()  
if "The following packages will be REMOVED" in str(output) or "Unable to locate package template" in str(output):
    print("clean seems fine")


process = subprocess.Popen(
    ["dpkg", "-i", "release/template_0.1.0_amd64.deb"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
(output, err) = process.communicate()
if "Setting up" in str(output):
    print("install seems fine")


process = subprocess.Popen(
    ["template"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
(output, err) = process.communicate()  
if "boilerplate for python ext seems fine" in str(output):
    print("invoke seems fine")
