# Final-project
import json, csv
from flask import Flask, g, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello():
	return "SBA Disaster Loan in FY 2014"

@app.route("/json")
def sample_json():

    data = list(csv.DictReader(open("SBA_Disaster_Loan_Data_FY14.csv", 'rU')))

    # Turn the data into JSON
    json_string = json.dumps(data)

    # Return JSON to the browser
    response = make_response(json_string)
    response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/flask")
def state_loan():
    reader = csv.DictReader(open("SBA_Disaster_Loan_Data_FY14.csv", 'rU'))
    amount = 0
    for line in reader:
        if line['Damaged Property State Code'].upper() == 'MO':
            amount += float(line['Total Approved Loan Amount'].replace(',', ''))


    return render_template("flask.html", state_code = 'mo', approved_loan = amount)


if __name__ == "__main__":
    app.run(debug=True)
