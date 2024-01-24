import csv
import sampleapi
from sampleapi import db

#   This method accepts a 3 column csv file, and loads it into an sqlite3 database.
#   @ param: string, path to the csv file
def initialize_database(fileName):
    with open(fileName, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            num = row[0]
            date = row[1]
            nodes = row[2]
            batch_data = sampleapi.batchData(batch_number=num, submitted_at=date, nodes_used=nodes)
            db.session.add(batch_data)
        db.session.commit()

############################################
#PROGRAM DRIVER
############################################
#ETL csv data into SQLite3 database
db.create_all()
initialize_database('example_batch_records.csv')