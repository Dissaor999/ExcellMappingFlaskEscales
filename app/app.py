import json
import os
from flask import Flask,render_template

from controllers.back_controller import excel_routes
app = Flask("_name_")
app.register_blueprint(excel_routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)