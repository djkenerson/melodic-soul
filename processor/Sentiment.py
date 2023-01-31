from statistics import mean
from musixmatch import Musixmatch
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Sentiment:

	def __init__(self, secret_file_name):

		# Grab api key from txt file and auth into musixmatch
		with open(secret_file_name, "r") as f:
			secret_ls = f.readlines()
			api_key = str(secret_ls[0]).strip()
			f.close()

		# Initialize musixmatch object
		self.musixmatch_obj = Musixmatch(api_key)

		# Initialize sentiment analyzer object
		self.sentiment_obj = SentimentIntensityAnalyzer()

	def track_sentiment_score(self, track):
		"""
		:param track: music track object
		:return: Vader compound sentiment score (float) - normalized value between [-1.0,1.0] where -1 is extreme negative
		sentiment and +1 is extreme positive sentiment. If musixmatch doesn't have lyrics, we'll return a neutral
		sentiment score of 0.0
		"""

		# check if sentiment score is already set for track
		if track.sentiment_score is not None:
			return track.sentiment_score

		track_sentiment_score = 0.0
		try:
			# Retrieve lyrics - musixmatch free plan only returns 30% of lyrics
			lyrics_raw = self.musixmatch_obj.matcher_lyrics_get(track.name, track.artists[0].name)
			lyrics = lyrics_raw['message']['body']['lyrics']['lyrics_body']

			# Calc and return sentiment score
			track_sentiment = self.sentiment_obj.polarity_scores(lyrics)
			track_sentiment_score = track_sentiment['compound']
			track.sentiment_score = track_sentiment_score
			track.set_sentiment()
			return track_sentiment_score

		except Exception as e:
			pass

		track.sentiment_score = track_sentiment_score
		track.set_sentiment()

		return track_sentiment_score

	def user_sentiment_score(self, user):
		"""
		:param user: user object
		:return: Average Vader compound sentiment score (float) of user's most listened to music tracks. This is a
		normalized value between [-1.0,1.0] where -1 is extreme negative sentiment and +1 is extreme positive sentiment.
		"""

		top_tracks_sentiment_scores = []
		for track in user.top_tracks:
			top_tracks_sentiment_scores.append(self.track_sentiment_score(track))

		user_sentiment_score = mean(top_tracks_sentiment_scores)
		user.sentiment_score = user_sentiment_score
		user.set_sentiment()

		return user_sentiment_score


