import csv
import math
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from json import dumps
from sqlalchemy import and_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///batchData.sqlite3'
db = SQLAlchemy(app)

#   This class defines the table in the sqlite database
#   Columns: id, batch_number, submitted_at, nodes_used
class batchData(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    batch_number = db.Column(db.Integer, nullable = True)
    submitted_at = db.Column(db.String(25), nullable=True)
    nodes_used = db.Column(db.Integer, nullable=True)

#   This method specifies json formatting for get response
def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    res = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    res.headers['mimetype'] = 'application/json'
    res.status_code = status
    return res

#   This method accepts a 3 column csv file, and loads it into an sqlite3 database.
#   @ param: string, path to the csv file
def initialize_database(fileName):
    with open(fileName, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            num = row[0]
            date = row[1]
            nodes = row[2]
            batch_data = batchData(batch_number=num, submitted_at=date, nodes_used=nodes)
            db.session.add(batch_data)
        db.session.commit()

#   Route to http://localhost : purposefully left blank
@app.route('/')
def index():
    return 'api data can be accessed at /batch_jobs'

#   Route for the api endpoint, supports filtering via min and max nodes used
#   as well as filtering by the first and last dates. All filters are optional
#   not using any filters returns all database entries. Data with missing attributes
#   are omitted.
@app.route('/batch_jobs', methods=['GET'])
def api_filter():
    output = []
    data = []
    query_parameters = request.args
    link = request.url
    output.append({'links': {'self': link}})

    #Retreive Query parameters
    subAfter = query_parameters.get('filter[submitted_after]')
    subBefore = query_parameters.get('filter[submitted_before]')
    minNode = query_parameters.get('filter[min_nodes]')
    maxNode = query_parameters.get('filter[max_nodes]')

    #initialize default parameters
    minParam = -math.inf
    maxParam = math.inf
    firstDateParam =  '0000000000000000000000000'
    lastDateParam = 'zzzzzzzzzzzzzzzzzzzzzzzzz'

    #update parameters
    if minNode:
        minParam = int(minNode)
    if maxNode:
        maxParam = int(maxNode)
    if subAfter:
        firstDateParam = str(subAfter)
    if subBefore:
        lastDateParam = str(subBefore)

    #Query the database
    filteredList = batchData.query.filter(and_(batchData.nodes_used >= minParam,
                                             batchData.nodes_used <= maxParam,
                                             batchData.submitted_at >= firstDateParam,
                                             batchData.submitted_at <= lastDateParam)).all()

    # "+" char is replaced with ' ' in query_parameter.get() method
    # replace ' ' with "+" and search for instances of the exact date
    # see ReadME.md: temporarily resolved issue for more information
    if subBefore:
        exactDate = lastDateParam[:19] + '+' + lastDateParam[20:]
        lastEl = batchData.query.filter(batchData.submitted_at == exactDate).all()
        for el in lastEl:
            filteredList.append(el)

    #Add the filtered results to the output
    for x in filteredList:
        attributes = {'batch_number': x.batch_number,'nodes_used': x.nodes_used, 'submitted_at': x.submitted_at}
        record = {'type': 'batch_jobs', 'id': x.id, 'attributes': attributes}
        data.append(record)
    output.append({'data': data})

    #convert output to json and return the result
    return jsonify(indent=2, **{'batch_jobs': output})

############################################
#PROGRAM DRIVER
############################################
if __name__ == '__main__':
    app.run()