import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import util
from util.Album import Album
from util.Artist import Artist
from util.Track import Track


class ReadSpotifyData:

	def __init__(self, secret_file_name):

		# Grab cid and secret from txt file
		with open(secret_file_name, "r") as f:
			secret_ls = f.readlines()
			cid = str(secret_ls[0]).strip()
			secret = str(secret_ls[1]).strip()
			f.close()

		# Auth and initialize spotify object
		scope = "user-top-read"
		redirect_uri = 'http://localhost:8888/callback'
		sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret,
													   redirect_uri=redirect_uri))
		# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
		# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

		self.spotify_object = sp

	def spotify_object(self):
		return self.spotify_object

	def artist(self, id):
		"""
		:param id: an artist ID, URI or URL
		:return: a single artist and metadata given the artist’s ID, URI or URL
		"""

		# initialize spotify object
		sp = self.spotify_object

		return sp.artist(id)

	def top_tracks(self, user, time_range):
		"""
		Returns the top 50 Spotify tracks that the user has listened to the most over the provided timeframe.
		Those tracks are added to the user object's top_tracks list. The albums from those tracks are added
		to the user object's top_albums list.
		:param time_range: short_term (last 4 wks), medium_term (last 6 mos), long_term (several years)
		:return: top 50 tracks listened to in the given time_range and associated metadata (track, album and artist)
		"""

		# delete top lists for user if they already have data in them
		if len(user.top_tracks) > 0:
			user.top_tracks = []
		if len(user.top_albums) > 0:
			user.top_albums = []

		# check time range
		if time_range not in ['short_term', 'medium_term', 'long_term']:
			raise ValueError("get_top_tracks: time_range must be 'short_term', 'medium_term' or 'long_term'")

		# initialize spotify object
		sp = self.spotify_object

		# pull top tracks in raw format
		top_tracks_raw = sp.current_user_top_tracks(limit=50, offset=0, time_range=time_range)

		# initialize a set to hold albums
		albums_raw = set()

		for item in top_tracks_raw['items']:

			# clean artist data
			track_artists = []
			artists_raw = item["artists"]
			for artist_raw in artists_raw:
				artist_id = artist_raw["id"]
				artist_uri = artist_raw["uri"]
				artist_name = artist_raw["name"]

				# Grab additional info about artist from Spotify api
				addl_artist_info = self.artist(artist_raw["id"])
				artist_genres = addl_artist_info["genres"]
				artist_followers = addl_artist_info["followers"]["total"]
				artist_popularity = addl_artist_info["popularity"]
				artist_image_url = None
				if (len(addl_artist_info["images"]) > 0 and addl_artist_info["images"][0]["url"] is not None
						and addl_artist_info["images"][0]["height"] == 640):
					artist_image_url = addl_artist_info["images"][0]["url"]
				artist = Artist(artist_id, artist_uri, artist_name, artist_genres, artist_followers, artist_popularity,
								artist_image_url)
				track_artists.append(artist)

			# clean album data
			album_id = item["album"]["id"]
			album_uri = item["album"]["uri"]
			album_name = item["album"]["name"]
			album_image_url = None
			if (item["album"]["images"][0] is not None and item["album"]["images"][0]["height"] == 640):
				album_image_url = item["album"]["images"][0]["url"]
			track_album = Album(album_id, album_uri, album_name, album_image_url)
			albums_raw.add(track_album)

			# clean track data
			track_id = item["id"]
			track_name = item["name"]
			track_popularity = item["popularity"]
			track = Track(track_id, track_name, track_artists, track_album, track_popularity)
			user.top_tracks.append(track)

		# convert set to list and add to user's top albums list
		user.top_albums = list(albums_raw)

		return user.top_tracks

	def top_artists(self, user, time_range):
		"""
		Returns the top 50 musical artists that the user has listened to the most over the provided timeframe.
		Those artists are added to the user object's top_artists list. The genres from those artists are added
		to the user object's top_genres list.
		:param time_range: short_term (last 4 wks), medium_term (last 6 mos), long_term (several years)
		:return: top tracks listened to in the given time_range and associated metadata (track, album and artist)
		"""

		# delete top lists for user if they already have data in them
		if len(user.top_artists) > 0:
			user.top_tracks = []
		if len(user.top_genres) > 0:
			user.top_genres = []

		# check time range
		if time_range not in ['short_term', 'medium_term', 'long_term']:
			raise ValueError("get_top_tracks: time_range must be 'short_term', 'medium_term' or 'long_term'.")

		# initialize spotify object
		sp = self.spotify_object

		# pull top tracks in raw format
		top_artists_raw = sp.current_user_top_artists(limit=50, offset=0, time_range=time_range)

		# initialize a weighted dict to hold told genres by count
		genres_raw = {}

		# clean artist data
		for artist_raw in top_artists_raw['items']:
			artist_id = artist_raw['id']
			artist_uri = artist_raw['uri']
			artist_name = artist_raw['name']
			artist_genres = artist_raw["genres"]

			# append artist genres to user's top genres list
			for genre in artist_genres:
				if genre not in genres_raw:
					genres_raw[genre] = 1
				else:
					genres_raw[genre] += 1
			artist_followers = artist_raw['followers']["total"]
			artist_popularity = artist_raw["popularity"]
			if (len(artist_raw["images"]) > 0 and artist_raw["images"][0]["url"] is not None
					and artist_raw["images"][0]["height"] == 640):
				artist_image_url = artist_raw["images"][0]["url"]
			artist = Artist(artist_id, artist_uri, artist_name, artist_genres, artist_followers
							, artist_popularity,artist_image_url)

			# append artist to user's top artists list
			user.top_artists.append(artist)

		# sort the weighted dict of genres desc, convert to list and add to user's top artists list
		top_genres_raw_list = sorted(genres_raw.items(), key=lambda x: x[1], reverse=True)
		for genre in top_genres_raw_list:
			user.top_genres.append(genre[0])

		# return top_artists_raw
		return user.top_artists
