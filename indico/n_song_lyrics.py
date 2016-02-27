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

def getLyricsList(artist_name):
    lyricsList = list()
    album_dict = artist.getAlbums(**{'artist_mbid':artist_dict[artist_name],'format':'json'})
    for album_name in album_dict:
        track_dict = albums.getAlbumTracks(**{'album_id':album_dict[album_name], 'format':'json'})
        for track_name in track_dict:
            track_object = track.Track(track_id=track_dict[track_name])
            try:
                lyricsList.append([lyricsFilter(track_object.lyrics()['lyrics_body'].encode('utf-8')),
                                   artist_name])
            except:
                pass
    return lyricsList

def nextCh(file):
    return file.read(1)

def parseFromFile(file):
    data_pair_list = list()
    char = nextCh(file)
    while not char is None:
        if (char == '['):
            nextCh(file)
            more = True
            s = ""
            l = ""
            while more == True:
                c1 = nextCh(file)
                if c1[0] == '\''[0] or c1[0] == '"'[0]:
                    c2 = nextCh(file)
                    if c2[0] == ','[0]:
                        c3 = nextCh(file)
                        if c3[0] == ' '[0]:
                            c4 = nextCh(file)
                            if c4[0] == '\''[0]:
                                more = False
                            else:
                                s + c4
                        else:
                            s + c3
                    else:
                        s + c2
                else:
                    s + c1
            c = nextCh(file)
            while c[0] != '\''[0]:
                l + c
            data_pair_list.append(s)
            data_pair_list.append(l)
        else:
            pass
        char = nextCh(file)

    return data_pair_list