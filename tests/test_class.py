import pytest

class TestClass:

    def test_one(self):
        x = 'leon'
        assert 'l' in x
    
    def test_two(self):
        x = 'wakoli'
        assert hasattr(x, 'wakoli')