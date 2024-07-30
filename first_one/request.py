# to use httpx change the requests with httpx


# 1.
def areq():
    import requests
    r = requests.get("http://localhost:8000/hi")
    aas = r.json()
    print(aas)
# areq()


# 2.
# a request with parameter
def arequest():
    import requests
    r = requests.get("http://localhost:8000/hi/KhanMuhammad")
    aas = r.json()
    print(aas)
# arequest()


# 3.
# a request with query parameter
def aarequest():
    import requests
    r = requests.get("http://localhost:8000/hii?who=MOM")
    aas = r.json()
    print(aas)
# aarequest()


# 3.
# a request with query parameter but with param arguments
def aaarequest():
    import requests
    r = requests.get("http://localhost:8000/hii", params={"who": "khanbaba"})
    aas = r.json()
    print(aas)
# aaarequest()


# 4.
# a request with body
def aaaaarequest():
    import requests
    r = requests.post("http://localhost:8000/hiii", json={"who": "body"})

    aas = r.json()
    print(aas)
# aaaaarequest()

# 5.
# a request with header


def request1():
    import requests
    r = requests.post("http://localhost:8000/hi1", json={"who": "body"})

    aas = r.json()
    print(aas)
