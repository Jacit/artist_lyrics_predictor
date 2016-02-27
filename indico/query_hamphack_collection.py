from indicoio.custom import Collection
from sys import stdin

# Create collection with label
collection = Collection("hamphack_music_artist_collection")

def predictArtist(text):
    highest = 0
    highest_artist = "All zero"
    correlation = collection.predict(text, domain='topics')
    for artist in correlation:
        if correlation[artist] > highest:
            highest = correlation[artist]
            highest_artist = artist
#    print correlation
    return highest_artist

# Read everything from stdin
text = stdin.read()

# Print result
print predictArtist(text)