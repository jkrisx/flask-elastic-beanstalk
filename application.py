from flask import Flask
application = Flask(__name__)
app = application

@app.route('/')
def hello_world():
    return 'Test pake AWS Elastic Beanstalk'