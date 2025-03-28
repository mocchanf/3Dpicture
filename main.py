import os
from flask import Flask, render_template, request, send_file
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        file.save("input.png")

        # DALL·Eに画像を送って立体化
        response = openai.Image.create_edit(
            image=open("input.png", "rb"),
            prompt="Make this character look like a cute 3D soft vinyl toy",
            n=1,
            size="512x512"
        )

        image_url = response['data'][0]['url']

        # 保存しておく（wgetが必要）
        os.system(f"wget -O static/output.png {image_url}")

        return render_template("index.html", result=True)

    return render_template("index.html", result=False)

@app.route("/download")
def download():
    return send_file("static/output.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
