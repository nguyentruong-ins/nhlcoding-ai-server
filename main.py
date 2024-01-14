from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from services.ValidationService import ValidationService
from services.ClusterService import ClusterService

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("description",
                    type = str,
                    help = "Bad request")
parser.add_argument("submissions",
                    type = dict,
                    help = "Bad request",
                    action = "append")

# Validation endpoint
class ValidationEndPoint(Resource):
    validationService = None

    def __init__(self) -> None:
        super().__init__()
        self.validationService = ValidationService()

    def post(self):
        # Get the parameters
        args = parser.parse_args()
        description = args.get("description")

        return self.validationService.validate(description)

# Clustering program endpoint
class ClusteringProgram(Resource):
    clusterService = None
    def __init__(self) -> None:
        super().__init__()
        self.clusterService = ClusterService()

    def post(self):
        """
            Input:
            {
                "submissions": [
                    {1: "Submission 1"},
                    {2: "Submission 2"},
                    {3: "Submission 3"},
                    {4: "Submission 4"}, ...
                ]
            }

            Output:
            {
                "clusters": [
                    ["1", "2", "3", ...],
                    ["5", "6", "7", ...], ...
                ],
                "no_cluster": Integer
            }
        """

        # Get the parameters
        args = parser.parse_args()
        submissions = args.get("submissions")
        
        return self.clusterService.clusterTestFunction(submissions)


if __name__ == '__main__':
    # Add endpoints
    api.add_resource(ValidationEndPoint, 
                     '/api/v1/validate-description',
                     endpoint = "validate_endpoint")
    api.add_resource(ClusteringProgram, 
                     '/api/v1/cluster-program', 
                     endpoint = "cluster_endpoint")
    
    # Run server
    app.run(debug=True)
