#coding=utf-8
import pytest
from utils import *
from pytrade import *
import requests.exceptions

def on_connect(req,res,py):
    return Halt

def on_error(req,err,py):
    if req.url.endswith('?test-req-throw'):
        assert str(err)=='thrown'

    if req.url.endswith('?test-res-throw'):
        assert str(err)=='thrown'

    return Response(headers={'x-foo':'bar'},body='catched')

def test_con_throw(s):
    with pytest.raises(requests.exceptions.RequestException):
        s.get('https://example.com')

def test_drop_connection(s):
    res=s.get(SERVER+'?test-drop-connection')
    assert res.headers['x-foo']=='bar' and res.text=='catched'

def test_normal_req(s):
    res=s.get(SERVER)
    assert 'x-foo' not in res.headers and res.text!='catched'