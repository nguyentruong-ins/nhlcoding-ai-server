# nhlcoding-ai-server
AI server for AI tasks: Validation problem submission, program clustering

# Basic usage:

1. Install necessary packages:
```shell
pip install -r requirements.txt
```
2. Run the server:
```shell
python main.py
```
3. API Requests: 
- **POST URL**: http://127.0.0.1:5000/api/v1/validate-description
    - Request body: JSON format
    ```json
        {
            "description": "problem description" 
        }
    ```
    - Response:  `"Valid" / "Invalid"`

# Change processing model

## Validation endpoint

Change these path (in `main.py`) to your prefer encoder and classifier
```python
encoder = pickle.load(open('./pre-trained-encoders/tf_vectorize', 'rb'))
validate_model = pickle.load(open('./pre-trained-models/svm_tf', 'rb'))
```

This repo currently supports 2 type:
- `tf_vectorize` encoder along with `svm_tf` or `naive_bayes_tf` classifier.
- `tfidf_vectorize` encoder along with `svm_tfidf` or `naive_bayes_tfidf` classifier.

## Program clustering endpoint (`In progress`)

