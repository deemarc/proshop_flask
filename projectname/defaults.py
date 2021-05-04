""" Config defaults """

from logging import DEBUG
import os

FLASK_ENV = "development"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI="postgresql://projectname_usr:projectname_pass@127.0.0.1:5442/projectname_dev"
PORT="5000"
DEBUG = True
home_dir = os.environ.get("HOME")
if home_dir:
    LOG_FILE_PATH = home_dir + "/projectname.log"
else:
    "./projectname.log"

