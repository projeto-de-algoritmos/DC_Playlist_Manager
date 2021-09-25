import logging

from django.conf import settings

import requests


logger = logging.getLogger(__name__)


class SpotifyClient(object):
    def __init__(self) -> None:
        self.HOST = "https://api.spotify.com/v1"
        self.ACCESS_TOKEN = settings.SPOTIFY_ACCESS_TOKEN
        self.HEADERS = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}"
        }

    def get_playlist(self, playlist_id: str = None) -> dict:
        """Returns a playlist data"""
        print('playlist id:', playlist_id)
        playlist_id = playlist_id if playlist_id else settings.DEFAULT_PLAYLIST_ID

        url = f"{self.HOST}/playlists/{playlist_id}"
        response = requests.get(url, headers=self.HEADERS)
        response_json = response.json()
        if "error" in response_json:
            logger.error(
                f"Error fetching playlist {playlist_id}",
                extra={"response_json": response_json, "status_code": response.status_code}
            )
            return {}
        else:
            return response_json

    def format_playlist_tracks(self, playlist_data: dict) -> list:
        """Format playlist with data that will be displayed"""
        playlist_tracks = playlist_data["tracks"]["items"]
        IMAGE_DIMENSION_300 = 1
        formatted_playlist_tracks = []

        for track in playlist_tracks:
            playlist_track_data = {
                "album_name": track["track"]["album"]["name"],
                "album_image": track["track"]["album"]["images"][IMAGE_DIMENSION_300],
                "artists": [artist["name"] for artist in track["track"]["artists"]],
                "track_name": track["track"]["name"],
                "popularity": track["track"]["popularity"],
                "duration": track["track"]["duration_ms"],
            }
            formatted_playlist_tracks.append(playlist_track_data)
        return formatted_playlist_tracks


if __name__ == "__main__":
    client = SpotifyClient()
    
    playlist_top_50_br = "37i9dQZF1DX0FOF1IUWK1W"
    playlist_data = client.get_playlist(playlist_top_50_br)
    formatted_track_data = client.format_playlist_tracks(playlist_data)

    print(formatted_track_data)
