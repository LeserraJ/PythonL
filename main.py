from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Nations(Resource):
    def get(self):
        return {'usa':'ground', 
                'germany':"ground",
                'russia':'ground',
                'great_britian':'ground',
                'france': 'ground',
                'italy':'ground',
                'sweden':'ground',
                'israel':'ground'
                }


api.add_resource(Nations, "/nations")


if __name__ == "__main__":
    app.run(debug=True)