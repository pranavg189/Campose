from flask import Flask, render_template, request, flash
from models import *

basedir = os.path.abspath(os.path.dirname(__file__))

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

        try:
            imgur_id = request.values.get("imageID")
            latitude = request.values.get("latitude")
            longitude = request.values.get("longitude")

            # save image path along with latitude longitude in the database
            image = CameraImage(imgur_id=imgur_id, latitude=latitude, longitude=longitude)

            db.session.add(image)
            db.session.commit()
        except Exception as e:
            return apology("An error occured....")

        # add try catch statement to catch any errors if possible and return apology message
        return 'OK'
    else:
        """Display UI to capture an image"""
        return render_template("capture.html")

@app.route('/display')
def display():
    images = CameraImage.query.order_by(CameraImage.id.desc()).all()

    if len(images) == 0:
        flash("No captured images found !")
    else:
        flash("Showing all captured images......")

    return render_template("display.html", images=images)

"""Run this block of code to create the initial tables for the model"""
def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
