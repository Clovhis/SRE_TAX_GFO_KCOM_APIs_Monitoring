from Models import APIs
from ErrorHandler import validationException

calls_list = []

for call in calls_list:
    print(call.url)
    print(call.response_code)
    print(call.status)
    print(call.error_message)

#Create a call to an API endpoint and evaluate the reponse code, using get method
#For each failure add the error message to the response object
    
def checkStatus(response_list):
    try:
        count = int(0)
        for response in response_list:
            if response.response_code != 200:
                count += 1
        if count > 0:
            return False
    except Exception as e:
        raise validationException("The API call has failed. Please check the URL and try again.")