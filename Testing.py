
# Testing SimilarTrackFinder
from SimilarTrackFinder import *
#List = OrganizeTracks('taylor swift')
#FindSimilar('crash', 'EDEN', List)

# Normalizing Acoustic filter

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
             ['moon river','kina grannis']]



num=len(acoustics)
print(num)
mean=0

for i in range(num):
    refName= acoustics[i][0]
    refArtist= acoustics[i][1]

    findTrack= sp.search(q= 'track:' + refName + ' artist:' + refArtist, type='track', limit=1)
    thisTrack= findTrack['tracks']['items'][0]
    wantedTrackID= thisTrack['id']
    wantedTrackName= thisTrack['name']
    wantedTrackFeatures= sp.audio_features(wantedTrackID)
    print(wantedTrackFeatures[0]['acousticness'])
    mean+= (wantedTrackFeatures[0]['acousticness'])/num

print(mean)
