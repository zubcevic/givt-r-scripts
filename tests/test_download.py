#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for download.py.
"""
import unittest
import json
import requests
from download import LoginResponse, debug_requests_on
from download import givt_login
from download import givt_organization_details
from download import givt_download

def dummy(*args):
    print("not implemented")
    return None

def dummy_post(url, data, headers, allow_redirects):
    class MockResponse:
        def __init__(self, content, headers, status_code):
                self.content = content
                self.status_code = status_code
                self.headers = headers
    test_response = MockResponse("{ \"access_token\":\"access\"}", {"Request-Context": "request context"}, 200)
    return test_response

def dummy_get(url, headers, allow_redirects):
    class MockResponse:
        def __init__(self, content, headers, status_code):
                self.content = content
                self.status_code = status_code
                self.headers = headers
    test_response = MockResponse("[{ \"access_token\":\"access\"}]", 200)
    return test_response

def dummy_jsonload_logindata(*args):
    return {"access_token": "access"}

def dummy_jsonload_getdata(*args):
    return [{"GUID":"myguid", "OrgId":"myorgid"}]

# givt_login = dummy_login
requests.post = dummy_post
json.loads = dummy_jsonload_logindata

class TestGivt(unittest.TestCase):
    """
    Test the Givt functions.
    """
    def test_login(self):
        login_response = givt_login("user", "pass")
        self.assertEqual("access", login_response.access_token)
        json.loads = dummy_jsonload_getdata
        givt_org = givt_organization_details(login_response.access_token)
        self.assertEqual("myguid", givt_org.guid)


if __name__ == '__main__':
    unittest.main()