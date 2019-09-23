import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

class B2C:
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    api_url = settings.API_URL

    def access_token(self):
        r = requests.get(self.api_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
        access_token = r.json()["access_token"]
        return access_token
        
    
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
            "PartyB": settings.PARTY_B,
            "Remarks": "Salary from Hairways",
            "QueueTimeOutURL": "%s/api/b2c_queue_timeout_url" % settings.HOST_ADDRESS,
            "ResultURL": "%s/api/b2c_results"% settings.HOST_ADDRESS,
            "Occassion": ""
        }
        r = requests.post(payment_request_url, json=body, headers=headers)
        return r 


