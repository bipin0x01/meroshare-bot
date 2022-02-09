import flask
from modules import login,goto_asba,open_ipo_lister, quit_browser

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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