import pytest
from math import pi
from app.area import area_of_circle

class TestCircleArea:

    @pytest.mark.parametrize('radius, result',
        [
            (1, pi),
            (0, 0),
            (2.1, pi*(2.1**2))
        ]
    )
    def test_area(self, radius, result):
        # Test areas when radius >= 0

        # assert area_of_circle(1) == pytest.approx(pi)
        # assert area_of_circle(0) == 0
        # assert area_of_circle(2.1) == pytest.approx(pi*(2.1**2))

        # to simplify this code use parametrize and it will always loop thought the list given
        # print(area_of_circle(radius))
        assert area_of_circle(radius) == pytest.approx(result)


    @pytest.mark.parametrize('number',[-2,-10,-3])
    def test_value(self, number):
        # Test is it raises a value error is the input in less than 0

        pytest.raises(ValueError, area_of_circle, number)


    @pytest.mark.parametrize('value',[True, 'test'])
    def test_type(self, value):
        # Test is it raises a Type error if the input is a string or boolean

        pytest.raises(TypeError, area_of_circle, value)
        # pytest.raises(TypeError, area_of_circle, 'radius')