import pytest

def func(x):
    return x+1

def test_result():
    assert func(3) ==2



def f():
    raise SystemExit(1)

def test_my_test():
    with pytest.raises(SystemExit):
        f()

