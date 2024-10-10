from wtforms import FileField, Form, StringField, PasswordField

class loginForm(Form):
    username = StringField("Usuario")
    psw =  PasswordField("contraseña")

class GeneralForm(Form):
    excel_general = FileField("Archivo Excel (.xls,xlsx)")

