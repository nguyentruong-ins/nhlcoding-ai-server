import pickle
from flask import jsonify

class ValidationService():
    encoder = None
    validate_model = None

    def __init__(self) -> None:
        # Prepare the embedding model and validate model
        self.encoder = pickle.load(open('./pre-trained-encoders/tf_vectorize', 'rb'))
        self.validate_model = pickle.load(open('./pre-trained-models/svm_tf', 'rb'))
        
    def validate(self, description: str):
        # Encode description
        encode_description = self.encoder.transform({description: 1})
        
        # Predict
        predict_value = self.validate_model.predict(encode_description)

        return jsonify(
            isValid = True if (predict_value == 0) else False
        )