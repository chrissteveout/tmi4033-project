import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIPY_CLIENT_ID = '2f1db9e053ad48cbb9b2a5940c4601f2'
SPOTIPY_CLIENT_SECRET = '5ec0ed1460b34a75af79aab1f96e8522'

# Set up Spotify authentication
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit app
st.title("Music Recommendation System")

# Input for the seed track
seed_track = st.text_input("Enter a seed track (e.g., a track name or artist):")

if seed_track:
    # Search for the seed track
    results = sp.search(q=seed_track, type='track', limit=1)
    
    if results['tracks']['items']:
        seed_id = results['tracks']['items'][0]['id']
        seed_name = results['tracks']['items'][0]['name']
        seed_artist = results['tracks']['items'][0]['artists'][0]['name']
        
        st.success(f"Seed Track Found: {seed_name} by {seed_artist}")
        
        # Get recommended tracks
        recommendations = sp.recommendations(seed_tracks=[seed_id], limit=10)
        
        st.subheader("Recommended Tracks:")
        
        for idx, track in enumerate(recommendations['tracks']):
            st.image(track['album']['images'][0]['url'], caption=f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
            st.write(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
    
    else:
        st.error("Seed Track Not Found. Please enter a valid track name or artist.")