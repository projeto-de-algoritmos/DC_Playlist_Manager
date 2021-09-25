import requests
import os


class SpotifyClient(object):
    def __init__(self) -> None:
        self.HOST = "https://api.spotify.com/v1"
        self.ACCESS_TOKEN = os.getenv("SPOTIFY_ACCESS_TOKEN", "")
        self.HEADERS = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}"
        }

    def get_playlist(self, playlist_id: str) -> dict:
        """Returns a playlist data"""
        url = f"{self.HOST}/playlists/{playlist_id}"
        response = requests.get(url, headers=self.HEADERS)
        response_json = response.json()
        return response_json

    def format_playlist_tracks(self, playlist_data: dict) -> list:
        """Format playlist with data that will be displayed"""
        playlist_tracks = playlist_data["tracks"]["items"]
        IMAGE_DIMENSION_640 = 0
        IMAGE_DIMENSION_300 = 1
        IMAGE_DIMENSION_64 = 2
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
