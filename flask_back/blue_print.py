from flask import Blueprint, render_template

blue_print = Blueprint('blueprint', __name__, 'static_folders', template_folder='template')