import requests

BASE_URL = "http://127.0.0.1:8000/api/"

# Make two users and add them to a group
requests.post(f"{BASE_URL}users/create", json={
    "username": "dylan"
})

requests.post(f"{BASE_URL}users/create", json={
    "username": "akbar"
})

requests.post(f"{BASE_URL}users/create", json={
    "username": "zakiya"
})

requests.post(f"{BASE_URL}groups/create", json={
    "group_name": "friends"
})

requests.post(f"{BASE_URL}groups/add_user", json={
    "group_name": "friends",
    "username": "dylan",
})

requests.post(f"{BASE_URL}groups/add_user", json={
    "group_name": "friends",
    "username": "akbar",
})

requests.post(f"{BASE_URL}groups/add_user", json={
    "group_name": "friends",
    "username": "zakiya",
})


# Make an election
res = requests.post(f"{BASE_URL}elections/create", json={
    "group_name": "friends",
    "question": "Which sport"
})
print(res.json())

# find it's number

res = requests.get(f"{BASE_URL}users/dylan/list")
e_id = res.json()['data']['groups'][0]['election_id']
print("election #", e_id)

# Make the proposals
requests.post(f"{BASE_URL}elections/{e_id}/propose", json={
    "option": "Basketball",
    "username": "dylan"
})

req = requests.post(f"{BASE_URL}elections/{e_id}/propose", json={
    "option": "football",
    "username": "akbar"
})
print(req.text)

requests.post(f"{BASE_URL}elections/{e_id}/propose", json={
    "option": "soccer",
    "username": "zakiya"
})
print(req.text)

requests.post(f"{BASE_URL}elections/{e_id}/propose", json={
    "option": "hockey",
    "username": "zakiya"
})

req = requests.get(f"{BASE_URL}elections/{e_id}")
print(req.json())

input()

# Make a vote
requests.post(f"{BASE_URL}elections/{e_id}/vote", json={
    "option": "hockey",
    "username": "akbar",
    "power": 30
})

