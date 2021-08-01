from flask import Flask
from webComponent import WebComponent, WCProperties
from components.daily import daily_component

app = Flask(__name__, instance_relative_config=True)

@app.route("/hello")
def hello():
    value = 5
    myProps = {"key": value}
    properties = WCProperties(myProps)
    web_component = WebComponent(properties, "web-component.html")
    return web_component.render()


@app.route("/daily")
def daily():
    return daily_component.render()


if __name__ == "__main__":
    app.run( port=8080, debug=True )