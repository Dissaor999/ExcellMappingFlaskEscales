import json
import os
from flask import Flask,render_template
#template_dir = os.path.abspath("./templates")
#print(template_dir)
app = Flask("_name_")
@app.route("/")
def home():
    return render_template("login.html")
    



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)