"""Test Urls"""

import json

from django.test import Client, TestCase

from api.constants import BASE_POWER, STARTING_POWER


class TestUrls(TestCase):
    def test_urls(self):
        c = Client()

        # Create Users and a group
        r = c.post("/api/users/create",
                   {"username": "dylan"}, content_type="application/json")
        assert r.status_code == 201
        r = c.post("/api/users/create",
                   {"username": "akbar"}, content_type="application/json")
        assert r.status_code == 201
        r = c.post(
            "/api/groups/create", {"group_name": "frens"}, content_type="application/json")
        assert r.status_code == 201
        # Add both to the group
        r = c.post("/api/groups/add_user",
                   {"group_name": "frens", "username": "dylan"}, content_type="application/json")
        r = c.post("/api/groups/add_user",
                   {"group_name": "frens", "username": "akbar"}, content_type="application/json")
        assert r.status_code == 201

        # Make sure the list user response is right
        res = c.get("/api/users/dylan/list")
        assert res.status_code == 200
        data = res.json()['data']
        assert data["username"] == "dylan"
        assert data["groups"][0]["name"] == "frens"
        assert data["groups"][0]["power"] == STARTING_POWER

        # For Akbar too
        res = c.get("/api/users/akbar/list")
        assert res.status_code == 200
        data = res.json()['data']
        assert data["username"] == "akbar"
        assert data["groups"][0]["name"] == "frens"
        assert data["groups"][0]["power"] == STARTING_POWER

        # Create an election
        r = c.post("/api/elections/create", {"question": "who is the best",
                   "group_name": "frens"}, content_type="application/json")
        assert r.status_code == 201

        # get election id
        res = c.get("/api/users/dylan/list")
        data = res.json()['data']
        e_id = data["groups"][0]['election_id']

        # make proposal
        res = c.post(f"/api/elections/{e_id}/propose", {
            "option": "Me ofc",
            "username": "dylan"
        }, content_type="application/json")
        assert res.status_code == 201

        # support proposal
        res = c.post(f"/api/elections/{e_id}/vote", {
            "option": "Me ofc",
            "username": "akbar",
            "power": 10
        }, content_type="application/json")

        # assert election list results
        res = c.get(f"/api/elections/{e_id}")
        data = res.json()['data']
        assert data['proposals'][0]["power"] == BASE_POWER + 10
        assert data['proposals'][0]["text"] == "Me ofc"

        # assert dylan remaining powers
        res = c.get("/api/users/dylan/list")
        data = res.json()['data']
        assert data["groups"][0]["power"] == STARTING_POWER - BASE_POWER

        # assert akbar remaining powers
        res = c.get("/api/users/akbar/list")
        data = res.json()['data']
        assert data["groups"][0]["power"] == STARTING_POWER - 10
