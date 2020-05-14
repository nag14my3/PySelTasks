import pytest

@pytest.fixture()
def setUp():
    print("Fixtures at the Method Level i, e Before Method")
    yield
    print("Fitures at the Method Level i. e After Method")

def test_CallFixtures(setUp):
    print("Calling Fixtures")