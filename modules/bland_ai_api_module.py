import requests
from modules import env_module

class bland_api:
    def __init__(self, api_key:str, phone_number:str):
        self.headers = {
            'authorization': api_key,
            "Content-Type": "application/json"
        }
        self.pathway_id = env_module.get_pathway_id()
        self.phone_number = "+44"+phone_number

    def call_data(self, menu):
        data = {
            "phone_number": self.phone_number,
            "task": f"",
            "voice": "Karl",
            "request_data": {
                'menu': menu
            },
            "record": True,
            "reduce_latency": True,
            "ivr_mode": True,
            "temperature": 0.5,
            "webhook": "https://webhook.site/72186de7-061a-4087-aae2-1b0f688589d5",
            "pathway_id": self.pathway_id
        }