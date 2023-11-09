# nhlcoding-ai-server
AI server for AI tasks: Validation problem submission, program clustering

# Usage:

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