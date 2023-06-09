# import libraries
from initialize import *
import random

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ORGANIZE TS TRACKS OF A GIVEN ARTIST 

# each track is a list organized as follows:
# 0: trackID (STRING)
# 1: trackName (STRING)
# 2: speechiness - <0.33: music, 0.33-0.66: music and speech, >0.66: speech (FLOAT)
# 3: liveness - Higher liveness values represent an increased probability that the track was performed live (TRUE IF LIVE)
# 4: acousticness - from 0.0 to 1.0 (1.0 represents high confidence the track is acoustic) (TRUE IF ACOUSTIC)
# 5: instrumentalness - “Ooh” and “aah” sounds are treated as instrumental in this context (TRUE IF INSTRUMENTAL)
# 6: danceability - 0.0 is least danceable and 1.0 is most danceable (FLOAT)
# 7: energy - 0.0 to 1.0 and represents a perceptual measure of intensity and activity (FLOAT)
# 8: valence - 0.0 to 1.0 describing the musical positiveness conveyed by a track (FLOAT)

def OrganizeTracks(wantedArtist): # input the artist name as a string
    print('organizing tracks ...')
    
    tracks= []
    for i in range(0,500,50):
        allTracks = sp.search(q= wantedArtist, type='track', limit=50,offset=i)
        for i, t in enumerate(allTracks['tracks']['items']):

            trackName= t['name']
            trackID= t['id']
            trackFeatures= sp.audio_features(trackID)

            tracks.append([trackID, trackName, trackFeatures[0]['speechiness'], trackFeatures[0]['liveness']>0.75, trackFeatures[0]['acousticness']>0.75, trackFeatures[0]['instrumentalness']>0.75, trackFeatures[0]['danceability'], trackFeatures[0]['energy'], trackFeatures[0]['valence']])

    print(str(len(tracks)) + ' tracks saved ...')
    return tracks # list of tracks


def FindSimilar(refName, refArtist, trackList):
    # refName: name of the reference track
    # refArtist: name of the reference artist
    # trackList: list of tracks (from the OrganizeTracks function) -> trackList[i] = [name, acousticness, danceability, energy, instrumentalness, liveness, speechiness, valence]
    
    # find track and get features
    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)

    wantedTrack= [wantedTrackID, wantedTrackName, wantedTrackFeatures[0]['speechiness'], wantedTrackFeatures[0]['liveness']>0.9, wantedTrackFeatures[0]['acousticness']>0.9, wantedTrackFeatures[0]['instrumentalness']>0.9, wantedTrackFeatures[0]['danceability'], wantedTrackFeatures[0]['energy'], wantedTrackFeatures[0]['valence']]

    print('track ' + wantedTrackName + ' from ' + refArtist + ' found ...')

    #filter liveness, acousticness and instrumentalness
    filteredTrackList=[]
    for i in range(len(trackList)):
        if trackList[i][3:5]==wantedTrack[3:5]:
            filteredTrackList.append(trackList[i])

    print(' This track is ' + ('live' if wantedTrack[3] else 'not live') + ' and ' + ('acoustic' if wantedTrack[4] else 'not acoustic') + ' and ' + ('instrumental' if wantedTrack[5] else 'not instrumental') + ' ...' )
    print(str(len(filteredTrackList)) + ' tracks left to search ...')

    # SPEECH FILTER
    # 2: speechiness - <0.33: music, 0.33-0.66: music and speech, >0.66: speech
    filt=[]
    if wantedTrack[2] > 0.66:                                           # if speech, only keep speech
        print('Hmm this track sounds like a speech')
        for i in range(len(filteredTrackList)):
            if filteredTrackList[i][2] > 0.66:
                filt.append(filteredTrackList[i])
    elif wantedTrack[2] < 0.33:                                         # if music, only keep music
        print('Oh! This sounds like music')
        for i in range(len(filteredTrackList)):
            if filteredTrackList[i][2] < 0.33:
                filt.append(filteredTrackList[i])
    else:                                                               # if music and speech, keep music and speech
        print('Interesting, this track is music with speech... Is it rap?')
        for i in range(len(filteredTrackList)):
            if filteredTrackList[i][2] > 0.33 and filteredTrackList[i][2] < 0.66:
                filt.append(filteredTrackList[i])
    
    filteredTrackList= filt

    print(str(len(filteredTrackList)) + ' tracks left to search ...')

    # DANCEABILITY, ENERGY, VALENCE FILTER
    # 6: danceability - 0.0 is least danceable and 1.0 is most danceable
    # 7: energy - 0.0 to 1.0 and represents a perceptual measure of intensity and activity
    # 8: valence - 0.0 to 1.0 describing the musical positiveness conveyed by a track

    # look for an exact match
    match=[]
    for i in range(len(filteredTrackList)):
        if filteredTrackList[i][6:8] == wantedTrack[6:8]:
            match.append(filteredTrackList[i])

    if len(match) > 0:
        result = random.choice(match)
        print('Look! An exact match! You should listen to ' + result[1] + ' by ' + refArtist + ' :)')
    
    # look for a close match using minimum square distance
    else:
        result = filteredTrackList[0]
        msd = (result[6]-wantedTrack[6])**2 + (result[7]-wantedTrack[7])**2 + (result[8]-wantedTrack[8])**2

        for i in range(len(filteredTrackList)):
            square_distance = (filteredTrackList[i][6]-wantedTrack[6])**2 + (filteredTrackList[i][7]-wantedTrack[7])**2 + (filteredTrackList[i][8]-wantedTrack[8])**2
            if square_distance < msd:
                msd = square_distance
                result = filteredTrackList[i]
        
        print('I found something you may like: ' + result[1] + ' :)')
        print(result)
