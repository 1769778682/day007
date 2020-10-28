import pytest


@pytest.mark.run(order=4)
class TestDemo:

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")
