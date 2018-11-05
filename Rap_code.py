import lyricsgenius as genius
import json
import pprint 
import pandas as pd
api = genius.Genius('rQKd2ASIerVOjeQO1DF83KUIVUPS-1uGYw7MaTjVJX_5cAA2RVtPc9Y1idl_-0J0')
artist = api.search_artist('Andy Shauf', max_songs=3)

print(artist)
song = api.search_song('To You',artist.name)
print(song)
artist.add_song(song)
print(artist)
artist.save_lyrics()


for x in rappers_list { 
    artist = api.search_artist(x,)
    SOME CODE THAT TURNS THIS ARTIST SEARCH INTO A LIST
    for z in song_temp { 
        artist.add_song(z)
        artist.save_lyrics()
        (I WILL NEED SOME CODE THAT CREATES A PANDAS DATA FRAME AS RAPPER, SONG, LYRICS)
        (I WILL NEED TO APPEND THIS PANDAS DATA FRAME TO THE LARGER DATASET)
    }
}

Okay, so now we're at a 
