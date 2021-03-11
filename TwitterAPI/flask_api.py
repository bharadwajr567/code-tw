'''
This Flask api is using REST API calls to generate
random data and it acts like a client, server to get 
and post data for each server in the servers.txt file
'''

import json
import pathlib
import random
from flask import Flask , request



app = Flask(__name__)

# change the configuration for server name
app.config['SERVER_NAME'] = 'localhost:5000'


# Read server names from file and split the data 
server_file = pathlib.Path("servers.txt")
server_list = server_file.read_text().split()

# create empty dictionary to hold json data
# if you observe it is using a key, value to hold the data
json_data = dict()

# create application names
# this information is based on the json inputs
application_name = ('Cache2',
                    'Webapp1',
                    'Webapp0',
                    'Cache1',
                    'Database1',
                    'Database2',
                    'Database0')

# create version numbers
# same json inputs as above 
version_number = ('1.0.0',
                  '0.0.2',
                  '1.1.0',
                  '1.2.2',
                  '0.2.2',
                  '1.2.1',
                  '0.1.1',
                  '1.1.1')

# loop through each server in list and get the index and server name
for i, server in enumerate(server_list, start=1):
    # populate the dictionary with the keys and values
    json_data[i] = {
                    'id':i,
                    'Server': server,
                    'Application':random.choice(application_name),
                    'Version':random.choice(version_number),
                    'Uptime':random.randrange(10**9, 10**10),
                    'Request_Count':random.randrange(10**9, 10**10),
                    'Error_Count':random.randrange(10**9, 10**10),
                    'Success_Count':random.randrange(10**9, 10**10)
                    }
# create an endpoint: /status/1
# instead of reading the file everytime , 
# we can read the data and store it in cache
@app.route("/status/<int:status_id>", methods=['GET'])
def get_status(status_id):
    # open a file in write mode
    with open("api_data.json", "w") as json_file:
        # dump the json_data dictionary into a string
        data = json.dump(json_data, json_file, indent=4)
    # initialize an empty dictionary
    dict = {}
    # set name to None
    name = None
    # for every entry in the jdon_data's values
    for entry in json_data.values():
        # if the entry id is the same as the status id
        if entry['id'] == int(status_id):
            return json.dumps(entry)

    #print('Can not find a name for status id {}'.format(status_id))
    #return "Not Found in Dictionary", 404
    return "Invalid application_name" , 400

if __name__ == '__main__':
    app.run(debug=True)
