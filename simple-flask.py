#!/usr/bin/python

import socket
import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	with open("/storage/simple-flask-storage/teste.txt", "a+") as somefile:
		today = datetime.datetime.now()
		towrite = ("<div>Hostname: %s - %s</div>\n" % (socket.gethostname(), today) )
		somefile.write(towrite)
		somefile.close()

	with open("/storage/simple-flask-storage/teste.txt", "r+") as rofile:
		return ("<body>%s</body>" % (rofile.read()) )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
