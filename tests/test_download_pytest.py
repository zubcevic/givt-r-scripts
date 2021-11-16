#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for download.py.
Usage: python3.9 -m pytest tests/test_download_pytest.py.
"""
import pytest
import json
import requests
from download import LoginResponse, debug_requests_on
from download import givt_login
from download import givt_organization_details
from download import givt_download

def dummy(*args, **kwargs):
    print("not implemented")
    return None

def dummy_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, headers, status_code):
                self.content = content
                self.status_code = status_code
                self.headers = headers
    test_response = MockResponse("{ \"access_token\":\"access\"}", {"Request-Context": "request context"}, 200)
    return test_response

def dummy_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, headers, status_code):
                self.content = content
                self.status_code = status_code
                self.headers = headers
    test_response = MockResponse("[{ \"access_token\":\"access\"}]", 200)
    return test_response

def dummy_jsonload_logindata(*args, **kwargs):
    return {"access_token": "access"}

def dummy_jsonload_getdata(*args, **kwargs):
    return [{"GUID":"myguid", "OrgId":"myorgid"}]

def test_login():
    requests.post = dummy_post
    json.loads = dummy_jsonload_logindata
    login_response = givt_login("user", "pass")
    assert "access" == login_response.access_token
    json.loads = dummy_jsonload_getdata
    givt_org = givt_organization_details(login_response.access_token)
    assert "myguid" == givt_org.guid


