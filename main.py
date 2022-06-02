print("hello")
from flask import Flask
from random import randint
from flask import session
from db_scripts import get_question_after
session['']

def index():
random.quez_id()
return '<a href='/test">Викторина</a>
def test():
    if not('quiz' in session) or int(session['quiz'])<0
    return redirect(url_for("index"))
    else:

    result = get_question_after(session["last_question"], session["quez"])
    if  result is None or len(result) == 0
    else:
        session['last_question'] = result[0]
        return'h1'+ str(session['quiz']) + '<br>' + str(result + '</h1>')
def result()
end_quiz()


app = Flask(__name__)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/', 'test', test)
app.add_url_rule('/', 'result', result)
if __name__ == "__main__":

app.run() 

random.choices() 
