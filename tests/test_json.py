from app.data import StudentController
import pytest

@pytest.fixture
def db():
    db = StudentController()
    db.connect('data.json')
    yield db

@pytest.mark.parametrize('key, value',[
    ('id',1),
    ('name','Leon'),
    ('result','pass')
])
def test_leon_data(db, key, value):
    leon_data = db.get_data('Leon')
    assert leon_data[key] == value

@pytest.mark.parametrize('key, value',
    [
        ('id',2),
        ('name','Mark'),
        ('result','fail')
    ]
    )
def test_mark_data(db, key, value):
    mark_data = db.get_data('Mark')
    assert mark_data[key] == value