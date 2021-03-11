#01/27/2021 - Version 0.1

**This is a Custom Flask API Written in Python**


**Task: Your objective for this challenge will be to produce a tool that will query the ‘status’ page on 1000 servers and produce a report based on data within the status page. Each server has a ‘status’ endpoint that returns json data. The details of that json data will be provided below.**

**My Notes: I have written a Flask API called flask_api.py and the file that will run the code for my tool is called Query_Server_Data.py. As you will also need the servers.txt file to pull in the list of servers in the API and Query_Server_Data.py**

**Instructions:**

**Download the folder 'TwitterAPI' and unzip it to your Desktop on a Mac/Linux/windows
Open up a terminal window and "cd" into your directory: cd Desktop/TwitterAPI
Make sure you have Python 3.x or higher installed on your computer, to verify you can use - 
$python3 -V 
returns python 3.x ( mine is Python 3.8.5)
As I didn't use any aliases you can use one if you would wish to like - 
$alias python=python3
**
**
**If you don't have a virtual env created then follow these steps else you can ignore - 
Create a virtual environment by doing the following: 
If you face any issue with venv you can list all the virtual env's
$find myvirtualenv -type l 
$rm -rf `pipenv --venv` 
**

1. In your terminal within the same directory (Desktop/TwitterAPI) run: $ python3 -m venv interview 
2. Activate the virtual environment: $ . venv/bin/activate 
3. Install Flask in virtual environment by running: $ pip3 install Flask
Now run the Flask API by executing the following command: 
(i). $ export FLASK_APP=flask_api.py 
(ii). $ flask run
Check if the API is up and running by testing out id=1. Go to: http://localhost:5000/status/1 You should see a JSON response with id=1

4. Open up a second terminal but leave the first one open
Navigate to the correct folder: 
$ cd Desktop/TwitterAPI
5. Run the Query_Server_Data.py file with the following command: 
$ python3 Query_Server_Data.py 
6. You'll see several things:
 (i)An api_data.json file will be created in your TwitterAPI folder
the output will print to the console
 (ii)A file called file_output.txt will output to your TwitterAPI folder
open the file to see the output**
