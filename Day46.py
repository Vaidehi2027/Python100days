# day 46 
# creating a musical player using python - create a top 100 songs on billboard back in the time

# step 1 - importing names from the billboard website

from bs4 import BeautifulSoup
import requests
date = input("Enter the year you want to search for top 100 songs put in yyyy-mm-dd form: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url,headers = header)
#print(response.text)

# now create the soup
soup = BeautifulSoup(response.text,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

# step 2 - authentication with spotify
client_id = "746fa626be1e43a59896ec1fd5b03d64"
client_secret = "37401861ed6d4a3981bcbe5901093f9f"

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = client_id, client_secret = client_secret, redirect_uri = "https://example.com", scope = "playlist-modify-private",show_dialog=True, cache_path = "token.txt",username = "Purple rose27")
                     
                     
)

user_id = sp.current_user()["id"]
print(user_id)

# now we want to fetch the songs from the spotify
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type= "track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in spotify. Skipping it.")


# abhi hum playlist banayenge
sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "http://example.com",
        client_id = client_id,
        client_secret = client_secret,
        show_dialog = True,
        cache_path = "token.txt"
    )

)
playlist = sp.user_playlist_create(user=user_id, name = f"{date} Billboard 100", public = False)
print(playlist)

# the final step  
sp.playlist_add_items(playlist_id = playlist['id'], items = song_uris)