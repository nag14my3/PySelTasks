import logging

import pytest

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(module)s:%(lineno)d] %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Project executed properly")

@pytest.mark.smoke
def test_pytestMethod1():
    print("First PYtest method is PASSED")


@pytest.mark.smoke
def test_pytestMethod2():
    print("Second PYtest method is PASSED")


@pytest.mark.regression
def test_pytestMethod3():
    print("Third PYTest method is PASSED")


@pytest.mark.smoke
def test_pytestMethod4():
    print("Fourth PYTest method is PASSED")


@pytest.mark.skip
def test_cognizant_demo1():
    print("Fifth PYTest method is PASSED")


@pytest.mark.smoke
def test_cognizant_demo2():
    print("Sixth PyTest ethod is PASSED")


@pytest.mark.xfail
def test_cognizant_demo3():
    print("Seventh PyTest method is PASSED")

