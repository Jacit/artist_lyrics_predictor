from musixmatch import artist, albums, track
from string import rfind

def lyricsFilter(lyrics):
    index = rfind(lyrics, '...')
    return lyrics[:index]


artist_dict = {'LMFAO':'ed5d9086-e8cd-473a-b96c-d81ad6c98f0d',
           'Lady Gaga':'650e7db6-b795-4eb5-a702-5ea2fc46c848',
           'Taylor Swift':'20244d07-534f-4eff-b4d4-930878889970',
           'Weird Al':'7746d775-9550-4360-b8d5-c37bd448ce01',
           'Hatebreed':'40b7efb7-1268-4a80-b354-600afdcbe9e2',
           'Notorious B.I.G.':'d5d97b2b-b83b-4976-814a-056d9076c8c3'}

for artist_name in artist_dict:
    print artist_name
    album_dict = artist.getAlbums(**{'artist_mbid':artist_dict[artist_name],'format':'json'})
    for album_name in album_dict:
        print album_name
        track_dict = albums.getAlbumTracks(**{'album_id':album_dict[album_name], 'format':'json'})
        for track_name in track_dict:
            track_object = track.Track(track_id=track_dict[track_name])
            try:
                print lyricsFilter(track_object.lyrics()['lyrics_body'].encode('utf-8'))
            except:
                pass
