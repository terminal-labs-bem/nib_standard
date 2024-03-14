import os.path
from importlib.metadata import version

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
PROJECTNAME = PROJECT_NAME.replace("_", "").replace("-", "")
VERSION = version(PROJECT_NAME)

VERSION = "0.0.8"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
SETUP_NAME = NAME
PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
EGG_NAME = SETUP_NAME.replace("_", "-")
TEMPDIR = "/tmp"
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
DIRS = [f"{TEMPDIR}/{PROJECT_NAME}"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
PAYLOADPATH = SITEPACKAGESPATH

reponame = "sdm"
VERSION = "0.0.1"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
SETUP_NAME = reponame
PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
EGG_NAME = SETUP_NAME.replace("_", "-")
TEMPDIR = "/tmp"
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
DIRS = [f"{TEMPDIR}/{SETUP_NAME}workingdirs"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
PAYLOADPATH = SITEPACKAGESPATH  # noqa: F841
server_port = 5000
socket_host = "0.0.0.0"
PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
POSTGRES_URL = "stub"
POSTGRES_USER = "stub"
POSTGRES_PW = "stub"
POSTGRES_DB = "stub"
DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
)
MONGO_DB = PROJECT_NAME  # noqa: F821
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
BASEDIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
STATIC_DIR = os.path.join(PAYLOADPATH, "static")
PERSISTENT_WORKING_DIRS = "stub"
CONFIG_DIC = {
    "POSTGRES_URL": POSTGRES_URL,
    "POSTGRES_USER": POSTGRES_USER,
    "POSTGRES_PW": POSTGRES_PW,
    "POSTGRES_DB": POSTGRES_DB,
}
tempfile.tempdir = TEMPDIR  # noqa: F821

import os
import tempfile

from sampleprojectdpewebapp.utils import get_env_variable

PROJECT_NAME = "sampleprojectdpewebapp"

# std config vars
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

# we should refactor this into f-strings
DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

MONGO_DB = PROJECT_NAME

VERSION = "0.2"

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])

TEMPDIR = "/dev/shm"

BASEDIR = os.path.abspath(os.path.dirname(__file__))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIR = os.path.join(ROOT_DIR, "templates")

STATIC_DIR = os.path.join(ROOT_DIR, "static")

TEXTTABLE_STYLE = ["-", "|", "+", "-"]

server_port = 5000

socket_host = "0.0.0.0"

# special config objects
CONFIG_DIC = {"POSTGRES_URL": POSTGRES_URL, "POSTGRES_USER": POSTGRES_USER, "POSTGRES_PW": POSTGRES_PW, "POSTGRES_DB": POSTGRES_DB}

tempfile.tempdir = TEMPDIR
