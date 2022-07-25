from flask      import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse, fields

import configparser
import os
from parser import intranet_parser

#import parser package
import parser.homepage_parser
import parser.intranet_parser



#set config
config = configparser.ConfigParser()    
config.read('config.ini', encoding='utf-8')

port = config['APIparser_config']['port']



#controller
app = Flask(__name__)

api = Api(app, version='1.0', title='내부용 파서 API', description='Swagger 문서', doc="/")
api = api.namespace('v1')


@api.route('/exist/<string:id>/<string:pw>',methods = ['GET'])
class Best(Resource) :
    def get(self, id, pw) :
        return intranet_parser.get_user_exist(id,pw)

@api.route('/info/<string:id>',methods = ['GET'])
class Best(Resource) :
    def get(self, id) :
        str = intranet_parser.get_user_info(id)
        print(str)

        if str == -1 :
            return -1
        else :
            body = {}
            body["id"] = str[0]
            body["name"] = str[1]
            body["floor"] = str[2]
            body["room"] = str[3]
            body["room_num"] = str[4]
            #body["date"] = str[5]

        
            return body

@api.route('/in_room/<string:id>',methods = ['GET'])
class Best(Resource) :
    def get(self, id) :
        return intranet_parser.get_in_room(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

