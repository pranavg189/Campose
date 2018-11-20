from flask import Flask, render_template, request
import base64

app = Flask(__name__)

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
