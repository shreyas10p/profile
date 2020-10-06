from flask import Flask,render_template,send_file
import os
from livereload import Server

DOWNLOAD_FOLDER = 'static/files/'
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/downloadfile/<filename>", methods = ['GET'])
def downloadFile(filename):
    file_path = DOWNLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')




if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
