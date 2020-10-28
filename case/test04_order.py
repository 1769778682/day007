import pytest


@pytest.mark.run(order=1)
class TestDemo:
    def test_case_one(self):
        print("test_case_one")

    def test_case_two(self):
        print("test_case_two")

    def test_case_three(self):
        print("test_case_three")

    def test_case_four(self):
        print("test_case_four")
