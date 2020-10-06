from flask import Flask,render_template,send_file,request
import os
from livereload import Server
import redis
from rq import Connection, Worker, Queue
import time


DOWNLOAD_FOLDER = 'static/files/'
app = Flask(__name__)
# r = redis.Redis()
# q = Queue(connection = r)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/downloadfile/<filename>", methods = ['GET'])
def downloadFile(filename):
    file_path = DOWNLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

# def task_in_background(t):
#     delay = 1
#     print("Running Task")
#     print("start delay")
#     time.sleep(delay)
#     print(len(t))
#     print("complete task")
#     return len(t)

@app.route("/suggestions",methods=["POST"])
def add_task():
    data = request.form
    print(data)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
