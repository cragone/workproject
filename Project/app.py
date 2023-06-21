from flask import Flask, render_template, request
from functions.areafunc import pullarea

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
    if pullarea(process_area_name) == process_area_name:
            return render_template("area.html", area_name=process_area_name)
    else:
            return 'This Area does not exist'



if __name__ == '__main__':
    app.run(debug=True, port=80)
