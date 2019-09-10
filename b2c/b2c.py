
from django.conf import settings

import requests
from requests.auth import HTTPBasicAuth

class B2C:
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    api_url = settings.API_URL

    def access_token(self):
        r = requests.get(self.api_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        access_token = r.json()["access_token"]
        return access_token

    def register_url(self, access_token):
        register_url = settings.REGISTER_URL
        headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/json"
        }
        body = {
            "ShortCode": "174379",
            "ResponseType": "[Completed]",
            "ConfirmationURL": "[https://363791ad.ngrok.io]",
            "ValidationURL": "[https://363791ad.ngrok.io]"
        }
        r = requests.post(register_url, json=body, headers=headers)

        return r
        
    
    def payment_request(self, access_token):
        payment_request_url = settings.PAYMENT_URL
        headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/json"
        }
        body =  {
            "InitiatorName": settings.INITIATOR_NAME,
            "SecurityCredential": settings.INITIATOR_SECURITY_CREDENTIAL,
            "CommandID": "SalaryPayment",
            "Amount": "100",
            "PartyA": settings.PARTY_A,
            "PartyB": "254792799958",
            "Remarks": "Salary from Hairways",
            "QueueTimeOutURL": "https://593652c3.ngrok.io" ,
            "ResultURL": "https://593652c3.ngrok.io/api/b2c_results",
            "Occassion": ""
        }
        # print(headers, body)
        r = requests.post(payment_request_url, json=body, headers=headers)
        return r 


