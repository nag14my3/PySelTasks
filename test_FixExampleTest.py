import pytest

@pytest.mark.usefixtures('data_provider')
class TestDemo1 :
    def test_FixturesDemo2(self, data_provider):
        print(data_provider)

