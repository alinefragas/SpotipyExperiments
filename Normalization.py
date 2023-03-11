# This script is used to normalize the threshold values applied for each filter

# Imports and credentials
from initialize import *

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# DATASETS
acoustics = [['flowers','boyce avenue'], 
             ['true colors','boyce avenue'], 
             ['I wanna dance with somebody','boyce avenue'], 
             ['take on me','boyce avenue'], 
             ['diamonds','boyce avenue'], 
             ['zombie','boyce avenue'],
             ['just like heaven','the lumineers'],
             ['here comes the sun','christina perri'],
             ['the only exception','katelyn tarver'],
             ['mr. brightside','run river north'],
             ['blackbird','jml'],
             ['accidentally in love','cole swensen'],
             ['linger','freedom fry'],
             ['i melt with you','daulton hopkins'],
             ['have a little faith in me','syml'],
             ['that funny feeling','phoebe bridgers'],
             ['a long december','mary bragg'],
             ['moon river','kina grannis'],
             ['chasing cars','the wind and the wave'],
             ['closer','ysabelle cuevas'],
             ['young blood','graeme james'],
             ['I kissed a girl','william fitzsimmons'],
             ['taylor swift 1989 medley','gardiner sisters'],
             ['city of stars','gavin james'],
             ['fix you','canyon city'],
             ['stitches','jaclyn davies'],
             ['holy','peter gergely'],
             ['i will follow you into the dark','eddie island'],
             ['seven nation army','zella day'],
             ['hello','erato']]
Nacoustics=len(acoustics)
mean_acoustics=0

non_acoustics = []
Nnon_acoustics=len(non_acoustics)
mean_non_acoustics=0

instrumentals = []
Ninstrumentals=len(instrumentals)
mean_instrumentals=0

non_instrumentals = []
Nnon_instrumentals=len(non_instrumentals)
mean_non_instrumentals=0

lives = []
Nlives=len(lives)
mean_lives=0

non_lives = []
Nnon_lives=len(non_lives)
mean_non_lives=0

# TESTING

# 1. ACOUSTICNESS
# acoustic songs
for i in range(Nacoustics):
    refName= acoustics[i][0]
    refArtist= acoustics[i][1]
    print(refName)
    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_acoustics+= (wantedTrackFeatures[0]['acousticness'])/Nacoustics
print('mean acousticness of acoustic songs:' + str(mean_acoustics))

# non acoustic songs
for i in range(Nnon_acoustics):
    refName= non_acoustics[i][0]
    refArtist= non_acoustics[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_non_acoustics+= (wantedTrackFeatures[0]['acousticness'])/Nnon_acoustics
print('mean acousticness of non acoustic songs:' + str(mean_non_acoustics))

# 2. INSTRUMENTALNESS
# instrumental songs
for i in range(Ninstrumentals):
    refName= instrumentals[i][0]
    refArtist= instrumentals[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_instrumentals+= (wantedTrackFeatures[0]['acousticness'])/Ninstrumentals
print('mean acousticness of acoustic songs:' + str(mean_instrumentals))

# non instrumental songs
for i in range(Nnon_instrumentals):
    refName= non_instrumentals[i][0]
    refArtist= non_instrumentals[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_non_instrumentals+= (wantedTrackFeatures[0]['acousticness'])/Nnon_instrumentals
print('mean acousticness of acoustic songs:' + str(mean_non_instrumentals))

# 3. LIVE
# instrumental songs
for i in range(Nlives):
    refName= lives[i][0]
    refArtist= lives[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_lives+= (wantedTrackFeatures[0]['acousticness'])/Nlives
print('mean acousticness of acoustic songs:' + str(mean_lives))

# non instrumental songs
for i in range(Nnon_lives):
    refName= non_lives[i][0]
    refArtist= non_lives[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    mean_non_lives+= (wantedTrackFeatures[0]['acousticness'])/Nnon_lives
print('mean acousticness of acoustic songs:' + str(mean_non_lives))
