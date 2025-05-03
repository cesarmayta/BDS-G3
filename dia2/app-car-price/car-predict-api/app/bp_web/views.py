from flask import render_template,request
from . import bp_web

@bp_web.route('/')
def index():
    return render_template('index.html')