from flask import Flask, request
import precincts

app = Flask(__name__)

@app.route('/precincts/<precinct_id>')
def precinct_id(precinct_id):
    return precincts.endpoint(request.values, direct_id = precinct_id)
    
@app.route('/precincts/')
def call_precincts():
    return precincts.endpoint(request.values)

@app.route('/measures/<measure_id>')
def measure_id(measure_id):
    pass

@app.route('/measures/')
def measures():
    pass

@app.route('/elections/<election_id>')
def election_id(election_id):
    pass

@app.route('/elections/')
def elections():
    pass

app.run(host='0.0.0.0', debug=True)
