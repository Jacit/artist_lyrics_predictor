from indicoio.custom import Collection
from sys import stdin

# Create collection with label
collection = Collection("hamphack_music_artist_collection")

# Read everything from stdin
text = stdin.read()

# Print result
print collection.predict(text, domain='topics')

# Optional function for client
def predictArtist(text):
    return collection.predict(text, domain='topics')