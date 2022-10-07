import csv

# update('608')
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/srn/<string:srn>', methods = ['GET'])
def update(srn):

    with open('newRSVP.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_csv = list(csv_reader)
    for i in list_of_csv:
        print(i)
        if(i[-1]==srn):
            c =i[2]
            print(i)
            
            i[-2]=0
    with open("newRSVP.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list_of_csv)
    try:
        return  jsonify({'name': c})
    except:
        return  jsonify({'name': "No such entry found"})
def disp(num):

	return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
