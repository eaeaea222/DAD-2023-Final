from flask import Flask, request, render_template
import string

app = Flask(__name__, template_folder='templates')


def get_image_filename(letter):
    letter_to_image = {
        "a": "a.png",
        "b": "b.png",
        "c": "c.png",
        "d": "d.png",
        "e": "e.png",
        "f": "f.png",
        "g": "g.png",
        "h": "h.png",
        "i": "i.png",
        "j": "j.png",
        "k": "k.png",
        "l": "l.png",
        "m": "m.png",
        "n": "n.png",
        "o": "o.png",
        "p": "p.png",
        "q": "q.png",
        "r": "r.png",
        "s": "s.png",
        "t": "t.png",
        "u": "u.png",
        "v": "v.png",
        "w": "w.png",
        "x": "x.png",
        "y": "y.png",
        "z": "z.png",
        "space": "space.png"

    }
    return letter_to_image.get(letter)

@app.route("/", methods=["GET", "POST"])
def generate_images():
    if request.method == "POST":
        word = request.form["word"]
        images = []
        for letter in word:
            if letter.isalpha():
                filename = get_image_filename(letter.lower())
            else:
                filename = "space.png"
            if filename:
                images.append(filename)
        return render_template("images.html", images=images)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(port=8000) #Changing this bc error running the original!

