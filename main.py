import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("description")

encoder = pickle.load(open('./pre-trained-encoders/tf_vectorize', 'rb'))
validate_model = pickle.load(open('./pre-trained-models/svm_tf', 'rb'))

class ValidationEndPoint(Resource):
    def get(self):
        return {'hello': 'world'}
    
    def post(self):
        args = parser.parse_args()
        description = args.get("description")
        
        encode_description = encoder.transform({description: 1})
        predict_value = validate_model.predict(encode_description)

        return "Valid" if predict_value == 0 else "Invalid"


api.add_resource(ValidationEndPoint, '/api/v1/validate-description')

if __name__ == '__main__':
    app.run(debug=True)