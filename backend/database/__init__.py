

def init_app(app):
    from backend.configuration import config_provider
    config = config_provider.config['DATABASE']
    print(config)
    _init_sqlalchemy(app, config)


def _init_sqlalchemy(app, config):
    app.config["SQLALCHEMY_DATABASE_URI"] = get_connection_url(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


def get_connection_url(config):
    password = ":" + config["PASSWORD"] if len(config["PASSWORD"]) > 0 else ""
    user = config["USER"]
    host = config["HOST"]
    port = config["PORT"]
    database = config["DB"]
    return "mssql+pymssql://{}{}@{}:{}/{}?charset=utf8".format(user, password, host, port, database)