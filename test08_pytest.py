import pytest


# from parameterized import parameterized


class Test:

    # @parameterized.expand([['羊排', '1'], ['骨头', '2'], ['狗粮', '3']])
    # def test_dog_eat(self, food, weight):
    #     print(f'大黄今天吃了{weight}斤{food}')

    @pytest.mark.parametrize(['name', 'food', 'weight'], [['大黄', '羊排', '1'], ['二哈', '骨头', '2'], ['金毛', '狗粮', '3']])
    def test_Dog_eat(self, name, food, weight):
        print(f'{name}今天吃了{weight}斤{food}')
