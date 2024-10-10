import json
import os
from flask import Flask,render_template

from controllers.back_controller import excel_routes
app = Flask("_name_")
UPLOAD_FOLDER = "./app/files"
app.register_blueprint(excel_routes)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)