import pytest

class Test_Demo:

    @pytest.mark.smoke
    def test_pytestMethod1(self):
        print("First PYtest method is PASSED")

    @pytest.mark.smoke
    def test_pytestMethod2(self):
        print("Second PYtest method is PASSED")

    @pytest.mark.regression
    def test_pytestMethod3(self):
        print("Third PYTest method is PASSED")

    @pytest.mark.smoke
    def test_pytestMethod4(self):
        print("Fourth PYTest method is PASSED")

    @pytest.mark.skip
    def test_cognizant_demo1(self):
        print("Fifth PYTest method is PASSED")

    @pytest.mark.smoke
    def test_cognizant_demo2(self):
        print("Sixth PyTest ethod is PASSED")

    @pytest.mark.xfail
    def test_cognizant_demo3(self):
        print("Seventh PyTest method is PASSED")

    @pytest.mark.regression
    def test_pyTestMethod8(self):
        print("Eight PYTest Method is PASSED")

    def test_pyTestMethod9(self):
        print("Ninth PYTest Method is PASSED")

    def test_pyTestMethod10(self):
        print("Tenth PYTest Method is PASSED")
