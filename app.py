"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Flask, redirect, flash


# Import personal modules



# Definition of the app
def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = '29FTh4Swfr3DuMlNRcQcZxCk7IFBMooP'

    # Import blueprints
    ## Import main blueprint
    from python.blueprints.mainBP import mainBP
    app.register_blueprint(mainBP)

    ## Import login blueprint
    from python.blueprints.loginBP import loginBP
    app.register_blueprint(loginBP)

    ## Import programm blueprint
    from python.blueprints.programBP import programBP
    app.register_blueprint(programBP)

    ## Import one program blueprint
    from python.blueprints.progFullBP import progFullBP
    app.register_blueprint(progFullBP)

    ## Import redirects blueprint
    from python.blueprints.redirectsBP import redirectsBP
    app.register_blueprint(redirectsBP)

    ## Import delete blueprint
    from python.blueprints.deleteBP import deleteBP
    app.register_blueprint(deleteBP)

    ## Import map blueprint
    from python.blueprints.mapBP import mapBP
    app.register_blueprint(mapBP)

    # Error 404 handler
    @app.errorhandler(404)
    def pageNotFound(error):
        flash("HTTP 404 Not Found", "Red_flash")
        return redirect('/')

    return app


# Start app if file is not imported
if __name__ == "__main__":
    app = create_app()
    app.run(debug=1, host='0.0.0.0', port=5454)
