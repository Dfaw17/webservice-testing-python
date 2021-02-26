import requests
from assertpy import assert_that


class TestCreateFavorite:

    def test_create_favorite(self):
        a = "HGU"
        b = "My Third Fav Airport"

        fav = {
            "airport_id": a,
            "note": b
        }

        response = requests.post("https://airportgap.dev-tester.com/api/favorites", data=fav,
                                 headers={'Authorization': 'Bearer token=bd2Y31TjuZdjE4YXgaHvvYHi'})
        data = response.json().get("data")

        assert response.status_code == 201
        assert data["type"] == "favorite"
        assert data["attributes"]["airport"]["iata"] == a
        assert data["attributes"]["note"] == b

    def test_create_favorite(self):
        a = "HGU"
        b = "My Third Fav Airport"

        fav = {
            "airport_id": a,
            "note": b
        }

        response2 = requests.post("https://airportgap.dev-tester.com/api/favorites", data=fav)
        data = response2.json().get('errors')[0]['detail']

        assert response2.status_code == 401
        assert data == "You are not authorized to perform the requested action."


    def test_favorite_already_created(self):
        a = "HGU"
        b = "My Third Fav Airport"

        fav = {
            "airport_id": a,
            "note": b
        }

        response3 = requests.post("https://airportgap.dev-tester.com/api/favorites", data=fav,
                                  headers={'Authorization': 'Bearer token=bd2Y31TjuZdjE4YXgaHvvYHi'})
        data = response3.json().get('errors')[0]['detail']

        assert response3.status_code == 422
        assert data == "This airport is already in your favorites"


    def test_favorite_invalid_airport(self):
        a = "JKT"
        b = "My Third Fav Airport"

        fav = {
            "airport_id": a,
            "note": b
        }

        response4 = requests.post("https://airportgap.dev-tester.com/api/favorites", data=fav,
                                  headers={'Authorization': 'Bearer token=bd2Y31TjuZdjE4YXgaHvvYHi'})
        data = response4.json().get('errors')[0]['detail']

        assert response4.status_code == 422
        assert data == "Please enter a valid airport code"
