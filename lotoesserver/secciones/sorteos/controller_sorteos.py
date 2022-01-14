from flask import Blueprint,render_template
from flask_login import login_required
from entites.sorteo import sorteo

BP_NM = 'sorteos'

sorteos = Blueprint(BP_NM, __name__, template_folder='templates')
 
@sorteos.route('/')
#@login_required
def inicio_func():
    return render_template('sorteos.html', seccion="sorteos")

@sorteos.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')