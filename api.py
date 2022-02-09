import flask
from modules.func import *
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Get the current time from Kathmandu timezone 
def get_time():
    return datetime.now().strftime("%H:%M:%S")



def get_openipolist():
    login('11700','00629889','Mnibt@6600')
    goto_asba()
    return (open_ipo_lister())

a=get_openipolist()
quit_browser()

@app.route('/', methods=['GET'])
def home():
    return flask.jsonify(a)

@app.route('/accounts', methods=['GET'])
def accounts():
    return 

app.run()