from ytmusicapi import YTMusic, OAuthCredentials
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Load auth
yt = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))

# Get history
history = yt.get_history()

# Last 5 listened tracks
for track in history[:50]:
    artist = track['artists'][0]['name']
    title = track['title']
    timestamp_iso = track['played']

    # Convert to UNIX timstamp
    #timestamp_unix = int(datetime.strptime(timestamp_iso, "%Y-%m-%dT%H:%M:%SZ").timestamp())

    print(f"{artist} - {title} (Timestamp: {timestamp_iso})")
    print("-" * 40)