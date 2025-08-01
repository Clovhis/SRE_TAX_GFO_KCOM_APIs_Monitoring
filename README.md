# KCOM APIs Monitoring

Tools for monitoring KCOM TAX/GFO APIs using simple Python helpers. The
modules obtain an OAuth token, call API endpoints and record the results for
further analysis by the SRE team.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the required environment variables for each environment:
   - `prod_scope`, `prod_client_id`, `prod_client_secret`, `prod_api_key`
   - `uat_scope`, `uat_client_id`, `uat_client_secret`, `uat_api_key`
   The `api_key` values are kept for compatibility but are not sent in request
   headers.
3. Use the functions in `Caller.py` to retrieve an OAuth token and call APIs.

## Build and Test

Run a basic syntax check on the modules:
```bash
python -m py_compile Caller.py Logger.py Models.py Credentials.py \
    Checker.py ErrorHandler.py Formater.py Reader.py
```

## Contribute

Pull requests are welcome. Please ensure new code includes clear comments and
runs without errors before submission.
