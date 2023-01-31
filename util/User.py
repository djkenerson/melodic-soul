import uuid


class User:
	top_tracks = []
	top_artists = []
	top_genres = []
	top_albums = []

	def __init__(self, firstname, lastname, gender, age):
		self.id = uuid.uuid4()
		self.firstname = firstname
		self.lastname = lastname
		self.gender = gender
		self.age = age
		self.sentiment_score = None
		self.sentiment = None
		self.avatar_image_url = None

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
