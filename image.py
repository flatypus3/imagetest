from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import urllib

def edit_image(image):
    image.thumbnail((720, 720), Image.ANTIALIAS)
    font = ImageFont.truetype("impact.ttf", 200)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "LMAO", font=font, fill=(255, 255, 255))
    return image

app = Flask(__name__)

@app.route('/<path:link>')
def index(link):
    # if any([i in link for i in ["gif", "jpg", "png", "jpeg"]]):
    try:
        if "http" not in link:
            link = "http://" + link
        response = requests.get(link)
        img = Image.open(BytesIO(response.content))
        edit_image(img).save("img.png")
        return send_file("img.png")
    except Exception as e:
        try:
            urllib.urlretrieve(link, "img.png")
            edit_image(Image.open("img.png")).save("img.png")
            return send_file("img.png")
        except: 
            return f"{e}"

if __name__ == '__main__':
    app.run(debug=True)
