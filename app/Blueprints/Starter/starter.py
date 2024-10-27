from flask import Blueprint, render_template, redirect


starter_bp = Blueprint('starter', __name__, template_folder='templates')


@starter_bp.route('/')
def index():
    return render_template('index.html')