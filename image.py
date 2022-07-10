from flask import Flask, send_file
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/<path:link>')
def index(link):
    # if any([i in link for i in ["gif", "jpg", "png", "jpeg"]]):
    try:
        response = requests.get(link)
        img = Image.open(BytesIO(response.content)).save("img.png")
        return send_file("img.png")
    except Exception as e:
        return f"{e}"

if __name__ == '__main__':
    app.run(debug=True)