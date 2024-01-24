### About
This project is a sample batch data search API. It was made in python, Flask, SQLite 

### Configuration and Installation Instructions
If python is not installed on your computer please download python here: https://www.python.org/downloads/


##### Activate venv and install requirements
To run this app first open terminal, cmd, or powershell.
From the terminal navigate to the extracted .zip file
Create the virtual envirionment:
CMD:
> py -m venv .venv

Terminal/Shell/Bash:
> python3 -m venv .venv

Powershell:
> virtualenv .venv -p

activate virtual envirionment:
CMD:
> .venv\Scripts\activate

Terminal/Shell/Bash:
> source .venv/bin/activate

Powershell:
> Scripts\activate.ps1

Next install the requirements, all requirements are saved in the requirements.txt file:

>pip install -r requirements.txt

##### Construct and initialize database
Run the constructDB.py file from the terminal.

CMD:

> py constructDB.py

Terminal:

> python3 constructDB.py

##### Run the application: 
CMD: 
> set FLASK_APP=sampleapi
> flask run

Terminal/Shell/Bash:
> export FLASK_APP=sampleapi
> flask run

Powershell
> $env:FLASK_APP = "sampleapi"
> flask run

##### Using the application
Open a url and navigate to http://127.0.0.1:5000/batch_jobs
Data can be filtered using keywords filter[submitted_after], 
filter[submitted_before], filter[min_nodes], filter[max_nodes].
All filters are optional. 
Data with missing feilds are omitted from the search.
Endpoint filtering must be structured as: 
localhost/batch_jobs?filter[insert_keyword]&filter[insert_keyword]&....
Example:
http://127.0.0.1:5000/batch_jobs?filter[submitted_after]=2018-02-28T00:14:25+00:00&filter[submitted_before]=2018-03-04T17:45:37+00:00&filter[min_nodes]=2&filter[max_nodes]=20

## Unresolved Issues / Improvements that can be made
Unresolved Issues:
- '[' and ']' characters in the link: URL in the json response are replaced with '%5B' and '%5D'
- json response has an extra outer layer {} which contains superfluous: "{'batch_jobs' = []}"

Temporarily resolved issue:
- When the query parameter is captured for the ISO 8601 formatted date/Time the '+' character is switched to a ' ' character. When
	the query filters for dates <= submitted_before the results are exclusive of jobs that took place with the same dateTime. 
	To resolve this such that the results are inclusive, the query parameter is manually altered to replace the " " with '+'

Future Improvements
- fix all char set bugs
- support for POST requests to the database
- support for database updates
- add api homepage
- ability to quickly find rows with missing values

## Testing
Basic unit tests are provided via the test.py file
Run the tests via terminal.
CMD:
> py test.py

Terminal
> python3 test.py

## References
    Data provided by OLCF
