import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        result = getDataPoint(quotes[0])  # Use the first quote for testing
        expected_result = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
        self.assertEqual(result, expected_result)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        result = getDataPoint(quotes[0])  # Use the first quote for testing
        expected_result = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
        self.assertEqual(result, expected_result)

    def test_getRatio_positivePrices(self):
        result = getRatio(10.0, 5.0)
        expected_result = 2.0
        self.assertEqual(result, expected_result)

    def test_getRatio_priceBZero(self):
        result = getRatio(10.0, 0.0)
        expected_result = None
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
