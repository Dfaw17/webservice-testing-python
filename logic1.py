import requests
from assertpy import assert_that


response = requests.get("https://airportgap.dev-tester.com/api/airports")

assert_that(response.status_code).is_equal_to(200)
assert len(response.json().get("data")) > 1
print("faw")
