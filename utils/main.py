import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

spotify = spotipy.Spotify()

#dependencies: track of song
#test: Accidentally in Love by Counting Crows
#spotify:track:7FQSD5JjWqGtS1BaQQiT6V

scope = 'user-library-modify'

if len(sys.argv) > 2:
    username = sys.argv[1]
    tids = sys.argv[2:]
else:
    print("Usage: %s username track-id ..." % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_saved_tracks_add(tracks=tids)
    pprint.pprint(results)
else:
    print("Can't get token for", username)

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_id = 'spotify:track:7FQSD5JjWqGtS1BaQQiT6V'
analysis = sp.audio_analysis(song_id)
print(json.dumps(analysis, indent=4))
