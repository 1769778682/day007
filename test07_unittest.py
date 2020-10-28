import unittest
from parameterized import parameterized


class Test(unittest.TestCase):

    @parameterized.expand([['羊排', '1'], ['骨头', '2'], ['狗粮', '3']])
    def test_dog_eat(self, food, weight):
        print(f'大黄今天吃了{weight}斤{food}')
