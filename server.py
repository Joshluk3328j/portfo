import csv
from email import message
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        # just like list slicing, we are grabing data from the dictionary that we created
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # '\n' is for new line
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    # the newline='' adds a newline everytime that we append
    with open('database.csv', mode='a', newline='') as database2:
        # just like list slicing, we are grabing data from the dictionary that we created
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # '\n' is for new line
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # you pass in the parameters as a list'[]' also, note the spelling of quote.
        csv_writer.writerow([email, subject, message])
        # this is to write into the csv file
        # the delimiter is ',' i.e  each item in a row should be separated by a comma
        # qoutechar is any qoute that we want around the characters


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # make sure that the submit_form is set to post(in small letters),
    if request.method == 'POST':
        # but your post in the server should be capital letters
        # this collects the data from the form_data and turns it into a dictionary
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'
