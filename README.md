# nhlcoding-ai-server
AI server for AI tasks: Validation problem submission, program clustering

# Basic usage:

1. Activate the venv
```bash
source venv/bin/activate
```
2. Install necessary packages:
```shell
pip install -r requirements.txt
```
3. Run the server:
```shell
python main.py
```
# API Usage
API Requests: 
- **POST URL**: http://127.0.0.1:5000/api/v1/validate-description
    - Request body: JSON format
    ```json
    {
        "description": "problem description" 
    }
    ```
    - Response:
    ```json
    {
        "isValid": Boolean 
    }
    ```
- **POST URL**: http://127.0.0.1:5000/api/v1/cluster-programs
    - Request body: JSON format
    ```json
    {
        "submissions": [
            {1: "Submission 1"},
            {2: "Submission 2"},
            {3: "Submission 3"},
            {4: "Submission 4"}, ...
        ]
    }
    ```
    - Response:
    ```json
    {
        "clusters": [
            ["1", "2", "3", ...],
            ["5", "6", "7", ...], ...
        ],
        "no_cluster": Integer
    }
    ```
# Change processing model

## Validation endpoint

Change these paths (in `/services/ValidationService.py`) to your prefer encoder and classifier
```python
self.encoder = pickle.load(open('./pre-trained-encoders/tf_vectorize', 'rb'))
self.validate_model = pickle.load(open('./pre-trained-models/svm_tf', 'rb'))
```

This repo currently supports 2 type:
- `tf_vectorize` encoder along with `svm_tf` or `naive_bayes_tf` classifier.
- `tfidf_vectorize` encoder along with `svm_tfidf` or `naive_bayes_tfidf` classifier.

## Program clustering endpoint (`In progress`)
Currently, the cluster-program endpoint is for testing purpose only.

