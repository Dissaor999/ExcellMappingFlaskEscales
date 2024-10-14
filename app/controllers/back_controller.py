import json
import os

from flask import Blueprint, jsonify, redirect, render_template, request
from werkzeug.utils import secure_filename
import controllers.forms_controller as forms
import controllers.process_controller as processor




template_dir = os.path.abspath("./templates")
excel_routes = Blueprint("Excel_Routes", __name__, template_folder=template_dir)

users = {
    'Dissaor':'admin',
    'Isaac':'admin'
}

@excel_routes.route("/", methods=["GET"])
def home():
    loginForm = forms.loginForm()
    return render_template("login.html", LoginForm=loginForm)

@excel_routes.route("/login", methods=["POST"])
def login():
    name = request.form['username']
    psw = request.form['psw']
    if name not in  users:
        loginForm = forms.loginForm()
        return render_template("login.html", LoginForm=loginForm)
    else:
        if users[name] != psw: 
            loginForm = forms.loginForm()
            return render_template("login.html", LoginForm=loginForm )
        else:
            formg = forms.GeneralForm()
            return render_template("excel.html", GeneralForm=formg )
        
@excel_routes.route("/actions", methods=["POST"])
def actions():
    if request.method == "POST":
        excel_file = request.files["excel_general"]
        excel_name = secure_filename(excel_file.filename)
        excel_file.save("./app/files/" + excel_name)
        processor.process(excel_name)
        return "Generando los archivos de importacion a gephi " + excel_name