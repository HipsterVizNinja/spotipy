import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

# Connect to Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='[Enter Client ID]',client_secret='[Enter Client Secret]'))
# token = credentials.get_access_token()
#spotify = spotipy.Spotify()


# Set up the output
with open('[Enter Output File Name]', 'w', newline='') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["spotify_track_id", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "time_signature"])

    i = 0
    with open('[Enter Input File Name]') as csv_input:
        csv_reader = csv.DictReader(csv_input, delimiter=',')
        for song in csv_reader:
            i += 1

            spotify_track_id = song["spotify_track_id"]

            results = spotify.audio_features(spotify_track_id)
            if results[0] is not None:
                track = results[0]
                danceability = track["danceability"]
                energy = track["energy"]
                key = track["key"]
                loudness = track["loudness"]
                mode = track["mode"]
                speechiness = track["speechiness"]
                acousticness = track["acousticness"]
                instrumentalness = track["instrumentalness"]
                liveness = track["liveness"]
                valence = track["valence"]
                tempo = track["tempo"]
                time_signature = track["time_signature"]
            else:
                danceability = ""
                energy = ""
                key = ""
                loudness = ""
                mode = ""
                speechiness = ""
                acousticness = ""
                instrumentalness = ""
                liveness = ""
                valence = ""
                tempo = ""
                time_signature = ""

            row_to_write = [spotify_track_id, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature]

            if i % 100 == 0:
                print(i)
                print(row_to_write)

            csv_writer.writerow(row_to_write)