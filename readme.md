# YouTube Music to Last.fm Scrobbler

## Overview

This script fetches the listening history from YouTube Music and scrobbles the tracks (listened on the current day) to Last.fm.

## Features

- Fetches recent tracks (current day) from YouTube Music
- Handles API authentication securely via environment variables

## Requirements

- Python 3.x
- YouTube Music API (ytmusicapi) 
- Last.fm API (pylast)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Zetsuki/YT-Music-Scrobbles.git
   cd YTMusic_Scrobbles
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your API credentials:
   ```ini
   YTM_CLIENT_ID=your_youtube_music_client_id
   YTM_CLIENT_SECRET=your_youtube_music_client_secret
   LFM_CLIENT_ID=your_lastfm_api_key
   LFM_CLIENT_SECRET=your_lastfm_api_secret
   LFM_USERNAME=your_lastfm_username
   LFM_PASSWORD=your_lastfm_password
   ```

## How to Obtain API Keys

### YouTube Music API

You need OAuth credentials to access YouTube Music history. Follow these steps:
1. Follow instructions on https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html 
2. Store the client id and client secret in the `.env` file.

### Last.fm API

1. Register for an API account at [Last.fm API](https://www.last.fm/api/account/create).
2. Get your API key and secret and store them in the `.env` file.
3. Store your Last.fm username and an MD5 hash of your password in the `.env` file.

## Running the Script

Once your `.env` file is set up, you can run the script:

```bash
python main.py
```

## API Rate Limits

- **YouTube Music API:** Limited to personal account usage. See https://ytmusicapi.readthedocs.io/en/stable/faq.html
- **Last.fm API:** Allows up to 50 tracks per batch; frequent requests may be rate-limited. See https://www.last.fm/api/tos

## Sources

- [ytmusicapi Documentation](https://ytmusicapi.readthedocs.io/)
- [Last.fm API Documentation](https://www.last.fm/api/)

## License

This project is licensed under the MIT License. See `LICENSE` for details.
