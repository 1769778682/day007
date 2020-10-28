import pytest


class TestDemo:

    def test_a(self):
        print("test_a")
        assert "abc"

    def test_b(self):
        print("test_b")
        assert 0
