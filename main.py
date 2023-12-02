from flask import Flask, request, json, jsonify

import sys
sys.path.append('./barista_robot')
from barista_robot.barista_test import BaristaTest
import demo

app = Flask(__name__)

@app.route("/drip", methods=['POST'])
def start_drip():
    params = request.get_json()
    print("받은 Json 데이터 ", params)

    my_recipe = []
    for i in range(len(params["order"])):
        temp = []
        temp.append(params["order"][i])
        temp.append(params["water"][i])
        temp.append(params["sec"][i])
        my_recipe.append(temp)
    print(my_recipe)
    robot = demo.robotController({"ip":"192.168.58.2"})
    if params["name"] == "Tetsu Kasuya":
        robot.run_program('Tetsu')
    # barista = BaristaTest()
    # barista.make_coffee(my_recipe)

    response = {
        "result": "ok"
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)