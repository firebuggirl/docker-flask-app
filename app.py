from flask import Flask, render_template
import random

app = Flask(__name__)

# list of dog images
images = [
    "https://source.unsplash.com/pChE-f_gqVc/800x450",
    "https://source.unsplash.com/7c3mrD9IGiU/800x450",
    "https://source.unsplash.com/saRU3vzmgkY/800x450",
    "https://source.unsplash.com/w_O_tPgxvok/800x450",
    "https://source.unsplash.com/WdyeFpkjcqs/800x450",
    "https://source.unsplash.com/uDpDycSH2r4/800x450",
    "https://source.unsplash.com/remPwE2zZus/800x450",
    "https://source.unsplash.com/6WneSv56YVI/800x450",
    "https://source.unsplash.com/fzvsFGYj8W8/800x450",
    "https://source.unsplash.com/IEqPWQvnR1E/800x450",
    "https://source.unsplash.com/Aka2x2D4Ph0/800x450",
    "https://source.unsplash.com/Aka2x2D4Ph0/800x450",


]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
