import lyricsgenius as genius
import json
import pprint 
import pandas as pd
import os
path_link = "D:/Users/asimon/Desktop/Rap"
os.chdir(path_link)
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

Okay, so now were at a point where we have a pandas data frame consisting of ... 
rapper name, song title, lyrics (large blogs of texts, really) ... 
we need a dataset that has all of this + broken up by line
 (okay this seems to be a minor problem and we'll probably  work on this with the json file)
-- looks like /n breaks up each line and their are other things we'd have to clean
worth exploring some data, but right the lyrics line looks like a mess
could have a dummy for each verse. which verse each line belongs to 
so its looking lie it'll be: 

rapper name, song title, lurics (less of a large blob of texts), line number, verse number, ...
annotation? (this could actually be pretty intersteing)
so the question for each of these variables is 


verse number: 
1. we can pull the all the [Verse n] of the song and then destring the ns (dropping [Verse])
2. then we can keep the highest number!
3. then we iterate throught the list the number of times for each song and then run the line number
4. right now well have the line number for each verse and then we can each ...
line by the largest line number of the previous verse
line number: 
1. im thinking we can count the number of/n and then iterate through this number
 -- then we can break up the text right before nth apperance of each /n
 2. this iteration will give us the line number and we can then append this to a new pd without the blob of lurics

 annotation: 
 Im thinking we can keep the annotations as a seperate column, itll be interseting to see this later
 -- im mainly skeptical because i dont want the program to capture the different voices as opposed to the content


once we get this working dataset, 

im going to try to merge in data that relates to the year the song was released and its charting history
i might have to create a new dataset of all the songs that charted i nour universe and then
merge it
i also want to see the year of release so thatll be a hunt
we also might want to do grammys
album sales would be intersting
oh, the album its from would also be necessary!


then we will throw in the rhyme scheme analysis program, not sure what we will do but itll be cool.



FINALLY, we will throw in the NLP work

LYRICS ANALYSIS

-- sentiment analysis of each song (we can do some cool pictures off of this)
total for each song, total for each album, total for each artist, total foreach year, decade, subgenre

-- bag of words for each song (removing the stop words)

-- tf-idf for each song, album, arist, year, decade, subgenere

-- doc2vec fore ach song, album, artist, year, decade, subgenere 


------ average vector for each song, artist, album, year, decade, subgenere and then plot them using PCA




