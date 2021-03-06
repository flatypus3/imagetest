from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import urllib

def edit_image(image):
    # resize the image so the height is 512 and the width maintains the aspect ratio
    sx,sy = image.size
    image1=image.resize((int(sx*(512 / sy)), 512))
    font = ImageFont.truetype("impact.ttf", 200)
    draw = ImageDraw.Draw(image1)
    # draw text in the center of image
    draw.text((image1.size[0]//4,image1.size[1]//4), "LMAO", font=font, fill=(255, 255, 255))
    return image1

app = Flask(__name__)

@app.route('/<path:link>')
def index(link):
    # if any([i in link for i in ["gif", "jpg", "png", "jpeg"]]):
    try:
        if "http" not in link:
            link = "http://" + link
        response = requests.get(link)
        img = Image.open(BytesIO(response.content))
        edit_image(img).save("tmp.png")
        return send_file("tmp.png")
    except Exception as e:
        try:
            urllib.urlretrieve(link, "img.png")
            edit_image(Image.open("img.png")).save("tmp.png")
            return send_file("tmp.png")
        except: 
            return f"{e}"

if __name__ == '__main__':
    app.run(debug=True)
