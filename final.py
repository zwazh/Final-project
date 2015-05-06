import json, csv
from flask import Flask, g, render_template, make_response

app = Flask(__name__)

@app.route("/about")
def aboutpage():
    title="About this site"
    return render_template("about.html", title = title)

@app.route("/json")
def sample_json():

    data = list(csv.DictReader(open("SBA_Disaster_Loan_Data_FY14.csv", 'rU')))

    # Turn the data into JSON
    json_string = json.dumps(data)

    # Return JSON to the browser
    response = make_response(json_string)
    response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/state/<state_code>")
def state_loan(state_code):
    reader = csv.DictReader(open("SBA_Disaster_Loan_Data_FY14.csv", 'rU'))
    amount = 0
    records = []
    cities = {}
    for line in reader:
        if line['Damaged Property State Code'].upper() == state_code:
            record_amount = float(line['Total Approved Loan Amount'].replace(',', ''))
            amount += record_amount

            records.append({'city_name': line['Damaged Property City Name'], 'amount': record_amount})

            if line['Damaged Property City Name'] not in cities.iterkeys():
                cities[line['Damaged Property City Name']] = record_amount
            else:
                cities[line['Damaged Property City Name']] += record_amount

    city_list = []
    for key, value in cities.iteritems():
        city_list.append({'city_name': key, 'amount': value})

    return render_template("flask.html", state_code = state_code, approved_loan = amount, cities = city_list)


if __name__ == "__main__":
    app.run(debug=True)

















