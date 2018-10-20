"""
Main app root of the api endpoints
"""
from flask import Flask
from api.config import config
from api.config.routes import Routes

class Loader:
    """ Create loader object to start server """
    @staticmethod
    def create_app(env_name):
        """
        static method for starting a server
        """
        #app initiliazation
        app = Flask(__name__)
        app.config.from_object(config.APP_CONFIG[env_name])

        #Directing to Routes
        Routes.fetch_routes(app)

        return app

APP = Loader.create_app('development')

if __name__ == '__main__':
    APP.run(port=2018)
