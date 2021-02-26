import requests
from assertpy import assert_that


class TestAirport:

    def test_get_all_data(self):
        response = requests.get("https://airportgap.dev-tester.com/api/airports")

        assert_that(response.status_code).is_equal_to(200)
        assert len(response.json().get("data")) > 1

    def test_get_one_data_airport(self):
        id = "KIX"
        response2 = requests.get(f"https://airportgap.dev-tester.com/api/airports/{id}")

        assert_that(response2.status_code).is_equal_to(200)
        data = response2.json().get("data")
        assert data["id"] == id
        assert data["attributes"]["iata"] == id

    def test_get_one_airport_not_found(self):
        id = "JKT"
        detail_message_notfound = "The page you requested could not be found"
        response3 = requests.get(f"https://airportgap.dev-tester.com/api/airports/{id}")

        assert response3.status_code == 404
        assert detail_message_notfound in response3.text


class TestAirportsDistance:

    def test_calculate_distance(self):
        a = "KIX"
        b = "NRT"

        airports = {
            "from": a,
            "to": b
        }
        response4 = requests.post(f"https://airportgap.dev-tester.com/api/airports/distance", data=airports)
        assert response4.status_code == 200
        assert a + "-" + b == response4.json().get("data")["id"]
        assert response4.json().get("data")["attributes"]["from_airport"]["iata"] == a
        assert response4.json().get("data")["attributes"]["to_airport"]["iata"] == b

    def test_calculate_invalid(self):
        a = "KIX"
        b = "JKT"

        airports = {
            "from": a,
            "to": b
        }
        response5 = requests.post(f"https://airportgap.dev-tester.com/api/airports/distance", data=airports)
        data = response5.json().get('errors')[0]['detail']

        assert response5.status_code == 422
        assert data in "Please enter valid 'from' and 'to' airports."