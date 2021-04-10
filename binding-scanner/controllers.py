import logging
import subprocess

from flask import (current_app, make_response)
from werkzeug.exceptions import NotFound

logger = logging.getLogger(__name__)

error_response = {
    'code': 500,
    'message': 'Something went wrong.',
}


def TsvGet(id):
    process2 = subprocess.Popen(['python3', '-m','pytest'], cwd="/app/weskit",
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    a, b = process2.communicate()
    return str(a)

def statusGet(id):
    return "Hello3"

def HeatmapGet(id):
    return "Hello"

def infoPost(id):
    return "Hello"
