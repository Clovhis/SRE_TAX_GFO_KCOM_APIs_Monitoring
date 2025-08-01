from Models import Config
import os

# ---------------------------------------------------------------------------
# Environment Credentials
# Loads OAuth credentials for production and UAT environments. api_key values
# are retained for backward compatibility but are not sent in request headers.
# ---------------------------------------------------------------------------

# AZF PROD Env
prodCredentials = Config(
    os.environ['prod_scope'],
    os.environ['prod_client_id'],
    os.environ['prod_client_secret'],
    "client_credentials",
    os.environ['prod_api_key'],
)

# UAT
uatCredentials = Config(
    os.environ['uat_scope'],
    os.environ['uat_client_id'],
    os.environ['uat_client_secret'],
    "client_credentials",
    os.environ['uat_api_key'],
)
