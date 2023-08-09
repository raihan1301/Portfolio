# python3 -m -venv .venv - to create environment
# . venv/bin/activate - to activate the environment
import csv

from flask import Flask, render_template, url_for, request , redirect

app = Flask(__name__)  # this is the app name
print(__name__)



@app.route("/")
def hello_world():
  return render_template('index.html')



@app.route("/<string:page_name>")
def html_page(page_name):
  print(f'i am here {page_name}')
  return render_template(page_name)



@app.route("/work<int:index>", methods=['GET', 'POST'])
def work_page(index):
  work_pge= 'work' + str(index) + '.html'
  print(f'i am page {work_pge}')
  return render_template(work_pge)  #jinja variable which is in html = variable we pass in this defination)



@app.route('/submit_form', methods=['POST', 'GET'])  #get means browser wants to send, Post measn browser want us to give
def submit_form():
  if request.method == 'POST':
  # we can do request.form['email'] to grab single item but by doing to_dict we are getting all the data in form of dictionary
    data = request.form.to_dict()    #data is variable  # now we have data we have to store this data
    print(data)
    write_to_file(data)  #this will call this method to write inside the database
    write_to_csv(data)  #this will write in csv 
  # return 'form Submitted'  #render_template('login.html', error=error)
    return redirect('thankyou.html')  #this will redirect to html of thank you page
  
  else:
    return 'Something went wrong'



# this code is store in text file which is not convienent hence we store our database in CSV file
# Also this is on local host
def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email  = data["email"]  #this can extract from our data which we have passed
    subject = data["subject"]  #this are key inside the bracket
    message = data["message"]
    file = database.write(f'\n{email}, {subject}, {message}')



#this will create a csv file but its in same server but how to write on database on different machines
def write_to_csv(data):
  with open('DatabaseUpdated.csv', mode='a', newline='') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    
    # , in databaseUpdated it means it ends of one column in csv
    csvDataBase = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
    csvDataBase.writerow([email,subject,message])  # we are writing it as a list and it samrt enough to know its as variable
    
    #delimeter means how you want to seprated here we selecetd ,
    #quotechar means do you want any quote in your string we need it "
    #quoting is csv.quote_minimal
    #postgres, oracle, Sql - Relational Database
    #mongodb, redis - non-relational databse no need of schema first- mongodb is document type





if __name__ == "__main__":
  app.run()







  #extras
  # for powershell
  #$env:FLASK_APP="main.py"  - to run flask
  # flask run
  # $env:FLASK_APP="main.py" - to make debug on for 1 time
  # $env:FLASK_DEBUG = "1" - for all the time

  #url_for is good we do not need to do hard code check documentation

  #Url Parameters to pass the parameters from url - variable rules please see documentation we can get id , int, uuid, string

  #MIME type - will send the content by flask  because it send as text but flask will tell is it html or css ot js tetx/CSS

  #server or API is also works for server it can also send json.
  #Swapi #Robohash

  # for different have different syntax
  # our is - export FLASK_APP=main.py after this
  # do - flask run

  # flaskApp = appname we need
  # export FLASK_ENV=development this is to make debug on

  # this is send the text but what if we have to send html template it comes with the function render template

  # now we have to add css - static files which cannot be change so we store style in static folder

  # favicon.ico it means error for not founding image

  #python anywhere allow us to deploy the site for free

  # open new terminal git clone - https://github.com/raihan1301/Portfolio.git  this will clone our project