"""
This file is for seperating your liked songs into 3 different BPM ranges: Slow(60-80bpm), Medium(90-110bpm) and Fast(130-150bpm)

It requires a Spotify API token that can be obtained here: 
"""
    
import sys
from matplotlib.pyplot import get

from sympy import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

# Globals
scopes = ""
client_id = "6f46de0204fe4d269b49ae4ed626de40"
redirect_uri = 'https://workout-playlists.com/callback'

# 1. Obtain an authenticated Spotipy agent to issue requests from
def get_agent(username):
    token = util.prompt_for_user_token(username, scopes, client_id=client_id, client_secret='d5597fa540c84aa9ade5859bba91b681',redirect_uri='http://trythis/callback')

    if token: # If Token is granted, create the spotipy agent with it and return the agent
        sp = spotipy.Spotify(auth=token)
        return sp
    else:# Otherwise return None
        return None
  
# 2. Do the thing  
def group_liked_songs(sp):
    # first get all of the user's saved tracks and load into a df
    saved_tracks = sp.current_user_saved_tracks(limit=999999)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print('Missing Argument, "username"')
        sys.exit()

    
    agent = get_agent(username)
    if agent is not None:
        print('Agent Obtained')
        group_liked_songs()