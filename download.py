#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download script for GIVT reports.

This script can be used to download csv data from GIVT.

Example:

    $ python3 download.py

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import os
import json
import logging
from http.client import HTTPConnection  # py3
import requests

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


GIVT_API_URL = 'https://api.givtapp.net'
LOGIN_URL = GIVT_API_URL + '/oauth2/token'
GETORG_URL = GIVT_API_URL + '/api/CollectGroupView/CollectGroup'

#sys.exit(0)


class LoginResponse:
    def __init__(self, access_token):
        self.access_token = access_token

class GivtOrg:
    def __init__(self, guid, org_id):
        self.guid = guid
        self.org_id = org_id

def givt_login(user_name, user_password):
    request_headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
    login_data = {
        'grant_type': 'password',
        'userName': user_name,
        'password': user_password
    }
    login_response = requests.post(LOGIN_URL,
                                   data=login_data,
                                   headers=request_headers,
                                   allow_redirects=True)
    status = login_response.status_code
    access_token = json.loads(login_response.content)['access_token']
    request_context = login_response.headers.get('Request-Context')
    print("status code: ", status)
    print("access_token: ", access_token)
    print("request_context: ", request_context)
    return LoginResponse(access_token)

def givt_organization_details(access_token):
    request_headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    getorg_response = requests.get(GETORG_URL,
                                   headers=request_headers,
                                   allow_redirects=True)
    org_id = json.loads(getorg_response.content)[0]['OrgId']
    guid = json.loads(getorg_response.content)[0]['GUID']
    print("org_id: ", org_id)
    print("guid: ", guid)
    return GivtOrg(guid = guid, org_id = org_id)


def givt_download(access_token, givt_org):
    request_headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'nl-NL',
        'Authorization': 'Bearer ' + access_token,
        'CollectGroupId': givt_org.guid
    }
    request_parameters = {
        'startDate': '2021-11-04T14:32:47.238Z',
        'endDate': '2021-11-11T14:32:47.238Z'
    }
    download_url = GIVT_API_URL + '/api/v2/organisations/' \
        + givt_org.org_id + '/collectgroups/' + givt_org.guid + '/payments/export'
    download_response = requests.get(download_url,
                                     params=request_parameters,
                                     headers=request_headers,
                                     allow_redirects=True)
    with open('sample.csv', 'w', encoding='UTF-8') as csv_file:
        csv_file.write(download_response.content.decode('UTF-8'))
    print(download_response.content.decode('UTF-8'))

def main():
    # debug_requests_on()
    login_response = givt_login(os.environ.get('dep_username'), os.environ.get('dep_password'))
    givt_org = givt_organization_details(login_response.access_token)
    givt_download(login_response.access_token, givt_org)

if __name__ == '__main__':
    main()
