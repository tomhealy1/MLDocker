#! /usr/bin/pthon

import sys
sys.path.insert(0, "/var/www/flask/flask_predict_api")
sys.path.insert(0, '/opt/conda/lib/python/3.6/site-packages')
sys.path.insert(0, )"/opt/conda/bin/")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from flask_predict_api import as application