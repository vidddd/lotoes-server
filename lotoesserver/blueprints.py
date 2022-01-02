from config import config

def mount_blueprints(app, config_name):
    if not app:
        return
    
    from lotoes.secciones.inicio import inicio
    #from lotoes.secciones.usuarios import usuarios

    app.register_blueprint(inicio, url_prefix='')
    #app.register_blueprint(usuarios, url_prefix='/usuarios')
