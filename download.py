#!/usr/bin/env python3

import os
import requests
import json
import logging
import contextlib
from http.client import HTTPConnection  # py3


def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


# debug_requests_on()

request_headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
login_data = {
    'grant_type': 'password',
    'userName': os.environ.get('dep_username'),
    'password': os.environ.get('dep_password')
}
login_url = 'https://api.givtapp.net/oauth2/token'
login_response = requests.post(login_url,
                               data=login_data,
                               headers=request_headers,
                               allow_redirects=True)

status = login_response.status_code
access_token = json.loads(login_response.content)['access_token']
request_context = login_response.headers.get('Request-Context')

# print("header: ", response.headers.get('Content-Type'), response)
print("status code: ", status)
print("access_token: ", access_token)
print("request_context: ", request_context)

request_headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}
getorg_url = 'https://api.givtapp.net/api/CollectGroupView/CollectGroup'
getorg_response = requests.get(getorg_url,
                               headers=request_headers,
                               allow_redirects=True)

print(getorg_response.content)
org_id = json.loads(getorg_response.content)[0]['OrgId']
guid = json.loads(getorg_response.content)[0]['GUID']

print("org_id: ", org_id)
print("guid: ", guid)

request_headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept-Language': 'nl-NL',
    'Authorization': 'Bearer ' + access_token,
    'CollectGroupId': guid
}
request_parameters = {
    'startDate': '2021-11-04T14:32:47.238Z',
    'endDate': '2021-11-11T14:32:47.238Z'
}
download_url = 'https://api.givtapp.net/api/v2/organisations/' \
    + org_id + '/collectgroups/'+guid+'/payments/export'
download_response = requests.get(download_url,
                                 params=request_parameters,
                                 headers=request_headers,
                                 allow_redirects=True)

csv_file = open('sample.csv', 'w')
csv_file.write(download_response.content.decode('UTF-8'))
csv_file.close()

print(download_response.content.decode('UTF-8'))