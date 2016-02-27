from indicoio.custom import Collection
from n_song_lyrics import getLyricsList, parseFromFile

artist_list = ['LMFAO',
               'Lady Gaga',
               'Taylor Swift',
               'Weird Al',
               'Hatebreed',
               'Notorious B.I.G.']

# Create collection with label
collection = Collection("hamphack_music_artist_collection")

training_data = list()

#file = open('training_data.txt', 'r')
# training_data = parseFromFile(file)
# Gather lists of song lyrics associated with artist name
for artist in artist_list:
    for data_pair in getLyricsList(artist):
        if data_pair[0] == '':
            pass
        else:
            training_data.append(data_pair)

#print training_data
# Add text-label training data
collection.add_data(training_data, domain="topics")

# Training
collection.train()

# Check status of current Collection
collection.info()

# Telling Collection to block until ready
collection.wait()