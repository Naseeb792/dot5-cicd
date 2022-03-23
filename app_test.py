from app import index
from app import featurey
from app import featurex
from app import featurez

def test_index():
    assert index() == "Hello, world!"

def test_featurez():
    assert featurez() == "feature-z"
def test_featurey():
    assert featurey() == "feature-y"
def test_featurex():
    assert featurex() == "feature-x"
def test_featureyfail():
    assert featurey() == "featurey"
def test_featurexfail():
    assert featurex() == "featurex"
