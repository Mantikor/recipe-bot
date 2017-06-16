"""
This is the test suite for methods related to querying the Yummly API.
"""
import unittest
import os
from recipe_bot import get_search_results, create_payload

"""
Test methods related to creating dictionary of query parameters as payload
"""
class TestPayloadCreation(unittest.TestCase):

	# Test creating basic request parameters as payload:
	def test_create_basic_payload(self):
		expected_payload = {'q': 'onion soup'}
		payload = create_payload('onion soup')
		self.assertEqual(expected_payload, payload)

	# Test creating payload with optional allergy parameter
	def test_optional_allergy_parameter(self):
		expected_payload = {
			'q': 'onion soup',
			'allowedAllergy[]': 'Gluten-Free'
		}
		allergy = "Gluten-Free"
		payload = create_payload('onion soup', allergy=allergy)
		self.assertEqual(expected_payload, payload)

	# Test creating payload with optional time parameter
	def test_optional_time_parameter(self):
		expected_payload = {
			'q': 'onion soup',
			'maxTotalTimeInSeconds': '5400'
		}
		time = '5400'
		payload = create_payload('onion soup', time=time)
		self.assertEqual(expected_payload, payload)



"""
Test methods related to checking for successful search queries in API
"""
class TestSearchSuccess(unittest.TestCase):
	
	# Test simple search for onion soup
	def test_simple_search_api(self):
		expected_simple_result = 200
		simple_search_term = "onion soup"
		simple_response = get_search_results(simple_search_term)
		self.assertEqual(expected_simple_result, simple_response.status_code)

	# Test search with allergy parameter
	def test_allergy_search_api(self):
		expected_allergy_result = 200
		allergy_search_term = "onion soup"
		allergy = "Gluten-Free"
		allergy_response = get_search_results(allergy_search_term, allergy=allergy)
		self.assertEqual(expected_allergy_result, allergy_response.status_code)

	# Test search with time parameter
	def test_time_search_api(self):
		expected_time_result = 200
		time_search_term = "onion soup"
		time = "5400"
		time_response = get_search_results(time_search_term, time=time)
		self.assertEqual(expected_time_result, time_response.status_code)


	# Test parsing search results and returning highest rated query

if __name__ == '__main__':
	unittest.main()