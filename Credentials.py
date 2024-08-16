from Models import Config
import os

#AZF PROD Env
#PROD
prodCredentials = Config(os.environ['prod_scope'],os.environ['prod_client_id'],os.environ['prod_client_secret'],"client_credentials",os.environ['prod_api_key'])

#UAT
uatCredentials = Config(os.environ['uat_scope'],os.environ['uat_client_id'],os.environ['uat_client_secret'],"client_credentials",os.environ['uat_api_key'])