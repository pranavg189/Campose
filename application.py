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
def capture():
    """Display UI to capture/save an image"""
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

        return 'OK'
    else:
        return render_template("capture.html")

@app.route('/display')
def display():
    """Display all captured images"""
    images = CameraImage.query.order_by(CameraImage.id.desc()).all()

    if len(images) == 0:
        flash("No captured images found !")
    else:
        flash("Showing all captured images......")

    return render_template("display.html", images=images)

def main():
    """Create initial database tables"""
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
