from flask import Flask, render_template, request, jsonify, redirect
from hashlib import sha1 
import requests
import json 
import os
import time 
from flask import send_file

app = Flask(__name__)
shared_dirs = []

@app.route('/getfile/<fname>', methods=['GET','POST'])
def filesearch(fname):
	try:
		for dd in shared_dirs:
			if os.path.isfile(dd + '/' +fname):
				print(request)
				#return jsonify({'code' : '200' , 'msg' : 'File Found'})
				return send_file(dd + '/' +fname , as_attachment=True)
		return jsonify({'code' : '400' , 'msg' : 'File not found'})
	except FileNotFoundError:
		return jsonify({'code' : '400' , 'msg' : 'File not found'})


if __name__ == '__main__':
	f = open('config.cnf')
	line = f.readline()
	while line:
		if line.startswith('IP:'):
			ip = line.split()[1]
			print('ip: ', ip)
		elif line.startswith('PORT:'):
			port = line.split()[1]
		elif line.startswith('SHARED_DIRS'):
			drs = line.split()[1:]
			shared_dirs = drs
		line = f.readline()
	app.run(host=ip, port=port, debug=True, threaded=True)	