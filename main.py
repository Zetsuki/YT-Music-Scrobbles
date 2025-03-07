from ytmusicapi import YTMusic, OAuthCredentials
import os
from dotenv import load_dotenv
import utils
from dataclasses import dataclass
import pylast

# Load environment variables from .env file
load_dotenv()

# YouTube Music API credentials
YTM_client_id = os.getenv('YTM_CLIENT_ID')
YTM_client_secret = os.getenv('YTM_CLIENT_SECRET')

# Last.fm API credentials
LFM_client_id = os.getenv('LFM_CLIENT_ID')
LFM_client_secret = os.getenv('LFM_CLIENT_SECRET')
LFM_username = os.getenv('LFM_USERNAME')
LFM_password_hash = pylast.md5(os.getenv('LFM_PASSWORD'))

# Authenticate with Last.fm
network = pylast.LastFMNetwork(
    api_key=LFM_client_id,
    api_secret=LFM_client_secret,
    username=LFM_username,
    password_hash=LFM_password_hash
)

# Authenticate with YouTube Music API
yt = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=YTM_client_id, client_secret=YTM_client_secret))

# Retrieve listening history from YouTube Music
history = yt.get_history()

# Data structure for storing track info before scrobbling
@dataclass
class TrackInfo:
    artist: str 
    title: str
    album: str
    timestamp: int

# List to store tracks ready for scrobbling
track_info_array = []

# Process history and extract relevant track information
iteration = 0
for track in reversed(history[:200]):  # Process from oldest to newest
    artist = track['artists'][0]['name']
    title = track['title']
    timestamp_iso = track['played']
    duration_seconds = track['duration_seconds']

    # Extract album name, fallback to "Unknown Album" if missing
    album = (track.get('album') or {}).get('name', "Unknown Album")

    # Process only tracks played today
    if "Today" in timestamp_iso:
        if iteration == 0:
            duration_seconds = 0  # First track of the day gets timestamp 0
        track_info = TrackInfo(
            artist=artist,
            title=title,
            album=album,
            timestamp=utils.convert_to_unix(timestamp_iso, duration_seconds)
        )
        track_info_array.append(track_info)
        iteration += 1

# Send tracks to Last.fm (Scrobbling)
for track_info in track_info_array:
    try:
        print(f"Scrobbling: {track_info.artist} - {track_info.title} (Album: {track_info.album}, Timestamp: {track_info.timestamp})")
        network.scrobble(
            artist=track_info.artist,
            title=track_info.title,
            album=track_info.album,
            timestamp=track_info.timestamp
        )
        print("Scrobbled successfully!")
    except Exception as e:
        print(f"Error scrobbling {track_info.title}: {e}")

    print("-" * 40)  # Separator for readability
