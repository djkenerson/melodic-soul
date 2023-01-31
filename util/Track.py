class Track:

	def __init__(self, id, name, artists, album, popularity):
		self.id = id
		self.name = name
		self.artists = artists
		self.album_name = album
		self.popularity = popularity
		self.sentiment_score = None
		self.sentiment = None

	def set_sentiment(self):
		if self.sentiment_score is None:
			self.sentiment = None
		elif self.sentiment_score <= -0.8:
			self.sentiment = 'Extremely Negative'
		elif self.sentiment_score <= -0.4:
			self.sentiment = 'Negative'
		elif self.sentiment_score <= -0.2:
			self.sentiment = 'Slightly Negative'
		elif self.sentiment_score <= 0.2:
			self.sentiment = 'Neutral'
		elif self.sentiment_score <= 0.4:
			self.sentiment = 'Slightly Positive'
		elif self.sentiment_score <= 0.8:
			self.sentiment = 'Positive'
		elif self.sentiment_score > 0.8:
			self.sentiment = 'Extremely Positive'











