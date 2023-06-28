from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = "static"

count = 0


def save_access_count(count):
    with open("Atividade-5/access_count.txt", "w+") as file:
        file.write(str(count))


def load_access_count():
    try:
        with open("Atividade-5/access_count.txt", "r") as file:
            count_str = file.read()
            if count_str.strip():
                return int(count_str)
            else:
                return 0
    except FileNotFoundError:
        return 0


@app.route("/")
def home():
    global count
    count = load_access_count()
    count += 1
    save_access_count(count)
    return render_template("index.html", count=count)


@app.route("/access_count")
def access_count():
    global count
    count = load_access_count()
    return {"count": count}


if __name__ == "__main__":
    app.run()
