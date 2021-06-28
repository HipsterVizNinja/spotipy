import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

# Connect to Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='[Enter Client ID]',client_secret='[Enter Client Secret]'))
# token = credentials.get_access_token()
#spotify = spotipy.Spotify()

# Set up the output
with open('/Users/sm029588/Desktop/spotify_test_out.csv', 'w', newline='') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(
        ["Performer", "Song", "Updated_Performer", "Updated_Song", "spotify_genre", "spotify_track_id", "spotify_track_album", "spotify_track_duration_ms",
         "spotify_track_popularity","spotify_track_explicit","spotify_track_track_number"])

    i = 0
    with open('/Users/sm029588/Desktop/spotify_test.csv') as csv_input:
        csv_reader = csv.DictReader(csv_input, delimiter=',')
        for song in csv_reader:
            i += 1

            artist_name = song["Performer"]
            track_name = song["Song"]

            updated_artist_name = song["Updated_Performer"]
            updated_track_name = song["Updated_Song"]

            # Apostraphes in the titles causes problems, so strip all that stuff out for the API call
            artist_name_cleaned = updated_artist_name.replace("'", "")
            track_name_cleaned = updated_track_name.replace("'", "")

            # Get Spotify metadata for each unique song

            # Artist
            results = spotify.search(q=f"artist:#{artist_name_cleaned}", type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                artist = items[0]
                spotify_artist_genres = artist['genres']
            else:
                spotify_artist_genres = ""

            # Track
            results = spotify.search(q=f"artist:#{artist_name_cleaned} track:#{track_name_cleaned}", type='track')
            items = results['tracks']['items']
            if len(items) > 0:
                track = items[0]
                spotify_track_id = track['id']
                spotify_track_album = track['album']
                spotify_track_duration_ms = track['duration_ms']
                spotify_track_popularity = track['popularity']
                spotify_track_explicit = track['explicit']
                spotify_track_track_number = track['track_number']
            else:
                spotify_track_id = ""
                spotify_track_album = ""
                spotify_track_duration_ms = ""
                spotify_track_popularity = ""
                spotify_track_explicit = ""
                spotify_track_track_number = ""

            row_to_write = [artist_name,track_name,updated_artist_name,updated_track_name,spotify_artist_genres,spotify_track_id,spotify_track_album,spotify_track_duration_ms,spotify_track_popularity,spotify_track_explicit,spotify_track_track_number]

            if i % 100 == 0:
                print(i)
                print(row_to_write)

            csv_writer.writerow(row_to_write)