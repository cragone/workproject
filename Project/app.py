from flask import Flask, render_template, request
from functions.areafunc import pull_area, room_getter

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("home.html")

@app.route('/submission', methods=['GET'])
def reg_page():
    return render_template("submission.html")

@app.route("/area", methods=['GET'])
def processpage():
    process_area_name = request.args.get('process_area_name', None, str)
    area = pull_area(process_area_name)
    if area:
            return render_template("area.html", area_name=process_area_name)
    else:
            return 'This Area does not exist', 404
     
@app.route("/rooms", methods=["GET"])
def roompage():
    room_name = request.args.get('process_area_name', None, str)
    rooms = room_getter(room_name)
    if rooms:
        return rooms
    else:
        return 'No rooms in this area', 404
        

if __name__ == '__main__':
    app.run(debug=True, port=80)
