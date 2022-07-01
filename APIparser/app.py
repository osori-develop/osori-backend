from flask      import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse, fields

import configparser
import os

#import parser package
import parser.homepage_parser.py
import parser.intranet_parser.py



#set config
config = configparser.ConfigParser()    
config.read('..\config.ini', encoding='utf-8')

port = config['APIparser_config']['port']



#controller
app = Flask(__name__)

api = Api(app, version='1.0', title='내부용 파서 API', description='Swagger 문서', doc="/api-docs")
api = api.namespace('v1')

@app.route('/')
def hello_world():
    return 'APIparser server'


@api.route('/best/<int:age>/<string:gender>',methods = ['GET','POST'])
class Best(Resource) :
    def get(self, age, gender) :
        
        #get DB
        body = {}
        body['best'] = best_menu;
        return body
    def post(self) :
        pass




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

