# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import os

from document import api




app = Flask(__name__)



@app.route('/',methods = ['GET'])
def get_Api():

    return jsonify(api)





if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
#host='0.0.0.0',
