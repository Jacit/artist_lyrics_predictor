# indicoio_project
HampHack indicoio project
To train a network you need an account and key from inidico and their python API.
You should be able to train the network by simply calling python train_hamphack_collection.py
Once it is successfully trained, you can query it with the call python query_hamphack_collection.py < <your_test_data_file>
and it will output its guess as to which artist wrote the lyrics passed to it.
Adding an artist requires adding the name to both the list in train_hamphack_collection.py and the dictionary (paired with the artist's
musicbrainz id) in n_song_lyrics.py
Using this library requires the files in musixmatch since I added a few functions to the original library.
