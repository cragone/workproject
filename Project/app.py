from flask import Flask, render_template, request
from functions.areafunc import pull_area, room_getter
from functions.subfunc import room_note, equip_note

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
    
    
    
    
#to pull room info from submission page    
@app.route("/roominfo", methods=["POST"])
def roominfo():
    room_name = request.args.get("room_name", None, str)

    if not room_name:
        return "Missing room name", 400

    room_notes = request.args.get("room_notes", None, str)
    datetime = request.args.get("datetime", None, str)
    print(room_name, room_notes, datetime)
    room_data = room_note(room_name, room_notes, datetime)
    print(room_data)

    if room_data is None:
        return "Error saving data", 400
    else:
        return "Good request", 200


@app.route("/equipinfo", methods=["POST"])
def equipinfo():
    room_name = request.args.get("room_name", None, str)

    if not room_name:
        return "Missing room name", 400


    ecn = request.args.get("ecn", None, str)
    status = request.args.get("status", None, str)
    expiry = request.args.get("expiry", None, str)
    print(room_name, ecn, status, expiry)
    equip_data = equip_note(room_name, ecn, status, expiry)
    print(equip_data)

    if equip_data is None:
        return "Error saving data", 400
    else:
     return "Good request", 200
     

if __name__ == '__main__':
    app.run(debug=True, port=80)