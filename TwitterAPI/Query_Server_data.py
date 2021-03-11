import requests
import json

# This is a method to query the REST Api endpoints 
def query_file(server_file):
    # create an empty server's list to hold a dictionary of servers from our response
    server_list = []

    # open the server file
    with open('servers.txt', 'r') as file:
        # read in the file and split each server on a new line
        file_list = file.read().split()
    
    # loop through each server in the list and get the index
    for id, server in enumerate(file_list, start=1):
        # get the id
        server_id = id
        # create a constant url that will change with the server id
        url = f"http://localhost:5000/status/{server_id}"
        # do a get request for each of the server id's and store in a response
        response = requests.get(url)   
        # if the response is ('OK') or 200
        if response.status_code == 200:
            # turn text into a Python dictionary
            dict = json.loads(response.text)
            
            # append the dictionary to the server_list
            server_list.append(dict)

    # open a text file to write and append the output data
    with open("file_output.txt", "a") as writer:
        # Use a dictionary to keep success/error by application and version
        for i in range(0, len(server_list)):
            # provide names for the dictionary values
            app = server_list[i]['Application']
            ver = server_list[i]['Version']
            key = app + ' ' + ver
            if key in res:
              res[key]['success'] = res[key]['success'] + server_list[i]['Success_Count']
              res[key]['error'] = res[key]['error'] + server_list[i]['Error_Count']
            else:
              res[key]['success'] = server_list[i]['Success_Count']
              res[key]['error'] = server_list[i]['Error_Count']

        for k,v in res.items():
            app = k.split(' ')[0]
            ver = k.split(' ')[1]
            success_rate = ( v['success'] * 100.0) / (v['success'] + v['error'])
            # write the output to a file
            writer.write(f"Your application {app} with version {ver} has a success rate of {success_rate:.2f}\n")
            # print the output to the console
            print(f"Your application {app} with version {ver} has a success rate of {success_rate:.2f}")


query_file('servers.txt')








