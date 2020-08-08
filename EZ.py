# OpenOPS - PowerMax, Dell EMC PowerMax/VMAX Monitor
# PowerMax: PowerMax 2000, VMAX 250F
# Unisphere Version: 9.1.0.9
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 8th Aug. 2020
# Get REST api Documents
# https://IP address:8443/univmax/restapi/docs

# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote


# Set up endpoint and authentication credentials
endpoint = 'https://IP address:8443/univmax/restapi/91'

# Get base system information--symmetrixId
api = '/system/symmetrix'
url = endpoint + api
username = 'username'
password = 'password'
auth = HTTPBasicAuth(username, password)
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
}
res = requests.get(url, headers=headers, auth=auth, verify=False)
print(res.headers)
print(res.text)

payload = json.loads(res.text)
symmID = payload['symmetrixId'][0]


# Get response, example: system basic information, and show disk number
url  = endpoint +api + "/" + symmID
res1 = requests.get(url, headers=headers, auth=auth, verify=False)
print(res1.text)
payload1 = json.loads(res1.text)
diskNum = payload1['disk_count']
print(diskNum)

# Get response, example: system capacity information
url  = endpoint + "/sloprovisioning/symmetrix/" + symmID
res2 = requests.get(url, headers=headers, auth=auth, verify=False)
payload2 = json.loads(res2.text)
CapTotal = payload2['system_capacity']['subscribed_total_tb']
print('System Capacity: ', CapTotal, 'TB')
