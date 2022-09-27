import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
from tkinter import *
from config import client_id
from config import client_secret


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
                                                           
key_dict = {0: ["C", "B#"], 1: ["C#", "Db"], 2: ["D"], 3:["D#", "Eb"],
            4: ["E", "Fb"], 5: ["F", "E#"]}

print("Welcome to the artist key finder!")

while True:
    artist = input("Enter an artist name or done: ")
    if artist == 'done':
        break
    input_key = input("Enter key: ").upper()

    results = sp.search(q=artist, limit=40)

    for item in results['tracks']['items']:
        song = sp.audio_features(item['id'])
        key = song[0]['key']
        
        try:
            dict_key = key_dict[key]
            if input_key in dict_key:
                print(f"Artist: {artist}\nSong: {item['name']}")
        except:
            pass

    webbrowser.open(f"http://www.songsterr.com/a/wa/bestMatchForQueryString?a={artist}")  