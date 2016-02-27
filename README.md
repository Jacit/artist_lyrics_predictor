# indicoio_project
HampHack project using Indico library to train a neural network.
You need an account and key from Inidico and their python API in order to use this library.
You should be able to train the network by simply calling python train_hamphack_collection.py
Once it is successfully trained, you can query it with the call python query_hamphack_collection.py < file_with_song_lyrics
and it will output its guess as to which artist wrote the lyrics passed to it.
Adding an artist requires adding the name to both the list in train_hamphack_collection.py and the dictionary (paired with the artist's
musicbrainz id) in n_song_lyrics.py
Using this library requires the files in musixmatch since I added a few functions to the original library.
