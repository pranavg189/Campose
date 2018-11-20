from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'urlinfo.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.secret_key = "super secret key"

db.init_app(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image_data = request.values.get("imageBase64")

        with open('image.png', 'wb') as image_file:
            image_file.write(base64.b64decode(image_data))

        return 'OK'
    else:
        """Display UI to capture an image"""
        return render_template("capture.html")

"""Run this block of code to create the initial tables for the model"""
def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
