from pymongo import MongoClient
import os

working_path_list = ['/Users/kennethrhee/projects/flask-blog', '/Users/aviwilensky/Desktop/git/flask-blog']

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("gmail.com",80))
  machine_ip = s.getsockname()[0]
  s.close()
except:
  machine_ip = ''

if os.path.dirname(os.path.realpath(__file__)) in working_path_list or machine_ip == '162.243.225.65':
  mc = MongoClient('162.243.225.65')
  print 'Debug ON & Connected: local/staging'
else:
  mc = MongoClient()

'''Leave this as is if you dont have other configuration'''
DATABASE = mc.blog
POSTS_COLLECTION = DATABASE.posts
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

SECRET_KEY = ""
basedir = os.path.abspath(os.path.dirname(__file__))
secret_file = os.path.join(basedir, '.secret')
if os.path.exists(secret_file):
    # Read SECRET_KEY from .secret file
    f = open(secret_file, 'r')
    SECRET_KEY = f.read().strip()
    f.close()
else:
    # Generate SECRET_KEY & save it away
    SECRET_KEY = os.urandom(24)
    f = open(secret_file, 'w')
    f.write(SECRET_KEY)
    f.close()
    # Modeify .gitignore to include .secret file
    gitignore_file = os.path.join(basedir, '.gitignore')
    f = open(gitignore_file, 'a+')
    if '.secret' not in f.readlines() and '.secret\n' not in f.readlines():
        f.write('.secret\n')
    f.close()

LOG_FILE = "app.log"

DEBUG = True  # set it to False on production
