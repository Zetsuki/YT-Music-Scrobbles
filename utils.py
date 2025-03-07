import datetime

# ---------------------------------------------------------------------#
# The YouTube Music API (or more precisely, the YouTube Data API)      #
# does not provide precise timestamps for played tracks.               #
# This function estimates the UNIX timestamp by assuming that:         #
# - Tracks marked as "Today" are set to midnight by default.           #
# - The timestamp for subsequent tracks is calculated by adding the    #
#   duration of the previous track.                                    #
# ---------------------------------------------------------------------#

def convert_to_unix(timestamp_iso, previous_track_duration):
    """
    Converts a given timestamp (ISO format) to a UNIX timestamp.

    Parameters:
    - timestamp_iso (str): The timestamp string provided by YouTube Music API.
    - previous_track_duration (int): Duration (in seconds) of the previous track.

    Returns:
    - int: Estimated UNIX timestamp.
    """
    if "Today" in timestamp_iso:
        today = datetime.datetime.today()
        return int(today.replace(hour=0, minute=0, second=0).timestamp() + previous_track_duration)
    
    # If not "Today", use current timestamp as fallback
    return int(datetime.datetime.now().timestamp())
