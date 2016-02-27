from sanction.client import Client 
import urllib.request

myState = 'abc123456789'

# instantiating a client to process OAuth2 response
c = Client(token_endpoint="https://api.genius.com/oauth/authorize?",
#            resource_endpoint="https://www.googleapis.com/oauth2/v1",
            client_id=config["z7Qwk_XP1A7LnDqop1pKFjf7EkmHghSOqxIzKqYb2ocZgluGC4eGGDUDGHtNPFBk"],
            redirect_uri="http://localhost:8080/login/google",
#            client_secret=config["9rw35Y1-KdvH1XPsQqUgInZxlZUgXtUreqv4T-ocyuMf4frQzH-gpiFCrLyADqRUpNMNi91iVebU0BcrOX5BGg"
            state=state,
            response_type='code'])

url = 'https://api.genius.com/search?q=Kendrick%20Lamar'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

print(the_page)