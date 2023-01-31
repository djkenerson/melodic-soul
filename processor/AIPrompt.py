class AIPrompt:

	def __init__(self):
		self.prompt = None

	def ai_prompt(self, user):
		"""
		:param user: user object
		:return: ai prompt that can be fed to AI to create a musical portrait of the user
		"""

		# retrieve and clean the user data ahead of inserting into prompt
		top_artists = user.top_artists
		top_genres = user.top_genres
		if (user.age == None or user.age <= 0):
			age = ""
		else:
			age = str(user.age) + " year old "
		if (user.gender == None or user.gender == ""):
			gender = ""
		else:
			gender = user.gender.lower() + " "
		if (user.sentiment == None or user.sentiment == "" or user.sentiment == "Neutral"):
			sentiment = ""
		else:
			sentiment = " The sentiment of the person and the picture is " + user.sentiment + "."

		artists_str = ""
		i = 0
		while (i < 5):
			if i >= len(top_artists):
				break
			artists_str += top_artists[i].name
			if (i != 4):
				artists_str += ", "
			i += 1

		genres_str = ""
		j = 0
		while (j < 5):
			if i >= len(top_genres):
				break
			genres_str += top_genres[j]
			if (j != 4):
				genres_str += ", "
			j += 1

		self.prompt = "Editorial fashion photography autochrome portrait of a " \
					  + age + gender + "person with sunglasses who enjoys these music genres: " \
					  + genres_str + " and who likes these bands: " + artists_str + "." + sentiment

		return self.prompt
