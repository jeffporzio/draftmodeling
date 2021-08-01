from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route("/hello")
def hello():
    return "<h1> Hello World <h1>"


@app.route("/daily")
def daily():
    title = "Daily"
    return render_template('daily.html', title=title )


if __name__ == "__main__":
    app.run( port=8080, debug=True )