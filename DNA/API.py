import requests
from requests.auth import HTTPBasicAuth
import urllib3
from auth import DNA

def dnac_login():
    response = requests.post(DNA.BASE_URL + DNA.AUTH_URL, auth=HTTPBasicAuth(DNA.USERNAME, DNA.PASSWORD), verify=False)
    token = response.json()['Token']
    print(response.json()['Token'])
    return response.json()["Token"]

if __name__=="__main__":
    dnac_login()