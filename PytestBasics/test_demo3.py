import  pytest

# test should start or end with 'test' keyword
# for pytest to recognize

def test_m11():
    a=3
    b=4
    assert a+1==b, "test  failed"
    assert a > b, "test  failed as a is not greater than b"

def test_m12():
    name="SELENIUM"
    assert name.upper()=="SELENIUM"

def test_m13():
    assert True

def test_m15():
    assert 100==100

@pytest.mark.login
def test_login_python():
    assert "admin12"=="admin12"


@pytest.mark.login
def test_login_gmail():
    assert "admin_gmail"=="admin_gmail1"

@pytest.mark.login
def reddit_login():
    assert "dankindia"== "dankindia"
