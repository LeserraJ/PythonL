from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Nations(Resource):
    def get(self):
        data = pd.read_csv(nations.csv) #reads csv 
        data = data.to_dict() # convert dataframe to dictionary
        return {'data' : data}, 200 # return data and 200 OK code
    pass

api.add_resource(Nations, '/nations')