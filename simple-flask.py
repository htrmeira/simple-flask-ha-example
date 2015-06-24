#!/usr/bin/python

import socket

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	with open("/storage/simple-flask-storage/teste.txt", "a+") as somefile:
		towrite = ("<div>Hostname: %s</div>\n" % (socket.gethostname()) )
		somefile.write(towrite)
		somefile.close()

	with open("/storage/simple-flask-storage/teste.txt", "r+") as rofile:
		return ("<body>%s</body>" % (rofile.read()) )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
