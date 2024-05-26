import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock,bid_price,ask_price,price=getDataPoint(quotes[0])
    self.assertEqual(stock,quotes[0]["stock"])
    self.assertEqual(bid_price,quotes[0]["top_bid"]["price"])
    self.assertEqual(ask_price,quotes[0]["top_ask"]["price"])
    self.assertEqual(price,(quotes[0]["top_bid"]["price"]+quotes[0]["top_ask"]["price"])/2)
    stock,bid_price,ask_price,price= getDataPoint(quotes[1])
    self.assertEqual(stock,quotes[1]["stock"])
    self.assertEqual(bid_price,quotes[1]["top_bid"]["price"])
    self.assertEqual(ask_price,quotes[1]["top_ask"]["price"])
    self.assertEqual(price,(quotes[1]["top_bid"]["price"]+quotes[1]["top_ask"]["price"])/2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote["stock"],quote["top_bid"]["price"],quote["top_ask"]["price"],(quote["top_bid"]["price"]+quote["top_ask"]["price"])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock_a, bid_price_a, ask_price_a, price_a = getDataPoint(quotes[0])
    stock_b, bid_price_b, ask_price_b, price_b = getDataPoint(quotes[1])
    self.assertEqual(getRatio(price_a,price_b),(quotes[0]["top_bid"]["price"]+quotes[0]["top_ask"]["price"])/(quotes[1]["top_bid"]["price"]+quotes[1]["top_ask"]["price"]))

  def test_getRatio_DivideByZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock_a, bid_price_a, ask_price_a, price_a = getDataPoint(quotes[0])
    stock_b, bid_price_b, ask_price_b, price_b = getDataPoint(quotes[1])
    self.assertEqual(getRatio(price_a,price_b),0)

if __name__ == '__main__':
    unittest.main()
