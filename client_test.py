import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
  
  
     # Arrange[Expected results]
    expected_results = [
    ('ABC', 120.48, 121.2, (120.48 + 121.2)/2),
    ('DEF', 117.87, 121.68, (117.87 + 121.68)/2)
]

     
     
     # Act: Call function and store output
    for i in range (len(quotes)):
       result = getDataPoint(quotes[i])
       print(f"Test {i}: Expected {expected_results[i]}, Got {result}") # Test for mismatch, identify and clearly define issue
    # Assert: Verify that function returns expected results
       self.assertEqual(result, expected_results[i])



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]



    # Arrange[Expected results]
    expected_results = [
    ('ABC', 120.48, 119.2, (120.48 + 119.2)/2),
    ('DEF', 117.87, 121.68, (117.87 + 121.68)/2)
]


    # Act and Assert
    for i in range (len(quotes)):
       result = getDataPoint(quotes[i])
       print(f"Test {i}: Expected {expected_results[i]}, Got {result}")
       self.assertEqual(result, expected_results[i])



if __name__ == '__main__':
    unittest.main()
