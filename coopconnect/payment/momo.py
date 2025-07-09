import requests
import base64
from django.conf import settings

class MomoAPI:
    def __init__(self):
        self.subscription_key = settings.MOMOSUBSCRIPTION_KEY
        self.api_user = settings.MOMOAPI_USER
        self.api_key = settings.MOMOAPI_KEY
        self.base_url = "https://sandbox.momodeveloper.mtn.com"
        self.target_env = "sandbox"

    def get_access_token(self):
        url = f"{self.base_url}/collection/token/"
        credentials = f"{self.api_user}:{self.api_key}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Authorization": f"Basic {encoded_credentials}"
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json().get("access_token")

    def request_to_pay(self, phone_number, amount, external_id, payer_message, payee_note):
        access_token = self.get_access_token()
        url = f"{self.base_url}/collection/v1_0/requesttopay"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "X-Reference-Id": external_id,
            "X-Target-Environment": self.target_env,
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Content-Type": "application/json"
        }

        payload = {
            "amount": str(amount),
            "currency": " ", 
            "externalId": external_id,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": phone_number
            },
            "payerMessage": payer_message,
            "payeeNote": payee_note
        }

        response = requests.post(url, headers=headers, 
                                 json=payload)
        return response.status_code, response.json()
