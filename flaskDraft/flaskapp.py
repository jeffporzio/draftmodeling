from flask import Flask, request, jsonify
# from dailydraft.getPlayerData import getDailyBatterData
from dailydraft.playerpool import Playerpool
import jsons

app = Flask(__name__, instance_relative_config=True)

@app.route("/hello",methods=['GET'])
def hello():
    return "<h1> Hello World <h1>"

@app.route("/test",methods=['GET'])
def testEndpoint():
    responseDict = {
        "responseCode": 200,
        "responseData":"this is a test!"
        }
    return jsonify(responseDict)

@app.route("/daily/pool/pitcher", methods=['GET'])
def dailyPitcher(): 
    date = request.args.get('date')
    playerpool = Playerpool(date)
    for pitcher in playerpool.pitcherPool: 
        print(pitcher)
    return jsonify(date) 

@app.route("/daily/pool/batter", methods=['GET'])
def dailyBatter(): 
    date = request.args.get('date')
    playerpool = Playerpool(date)
    return jsonify(playerpool.batterPool) 


if __name__ == "__main__":
    app.run( port=8082, debug=True )