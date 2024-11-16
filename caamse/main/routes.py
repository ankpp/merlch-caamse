##############################################################################
# routes.py
#
# Defines the possible routes in the application
##############################################################################

from flask import flash
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from . import main
from .forms import IndexForm

@main.route('/', methods=['GET'])
def index():
    form = IndexForm()
    return render_template('index.html', form=form)