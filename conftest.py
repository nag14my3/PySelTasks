import pytest


@pytest.fixture(params=[("user1", "pwd1"), ("user2", "pwd2"), ("user3", "pwd3"), ("user4", "pwd4")])
def data_provider(request):
    return request.param
