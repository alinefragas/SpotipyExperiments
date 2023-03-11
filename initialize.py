# Always update and run this file before using the program
# Always remove the credentials before a commit

# 1. Import libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 2. Set up credentials << UPDATE CREDENTIALS 
SPOTIPY_CLIENT_ID = 
SPOTIPY_CLIENT_SECRET = 
SPOTIPY_REDIRECT_URI = 

# 3. Connect to spotipy api
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)