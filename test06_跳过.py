import pytest


class TestDemo:
    version = 20

    def test_a(self):
        print("test_a")
        assert "abc"

    @pytest.mark.skipif(version < 30, reason="支持30版本")
    def test_b(self):
        print("test_b")
        assert 1