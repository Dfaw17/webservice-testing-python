import requests
import json
from assertpy import assert_that
a = "HGU"
b = "My Third Fav Airport"

fav = {
    "airport_id": a,
    "note": b
}

response = requests.post("https://airportgap.dev-tester.com/api/favorites", data=fav, headers = {'Authorization':'Bearer token=bd2Y31TjuZdjE4YXgaHvvYHi'})
data = response.json().get('errors')[0]['detail']

assert response.status_code == 422
assert data == "This airport is already in your favorites"

