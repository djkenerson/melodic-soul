import os
import openai

class SpotifyAvatar:

	def __init__(self, secret_file_name):
		self.image_url = None
		self.openai_secret_file_name = secret_file_name

	def spotify_avatar(self, user, ai_prompt):
		"""
		:param ai_prompt: string prompt for the DALL-E openai image generator
		:return: string image url
		"""

		# Auth into openai
		with open(self.openai_secret_file_name, "r") as f:
			secret_ls = f.readlines()
			openai.api_key = str(secret_ls[0]).strip()
			f.close()

		# generate image from prompt and return image_url
		i = 5
		e = False
		while (i != 0):
			try:
				response = openai.Image.create(
					prompt=ai_prompt,
					n=1,
					size="512x512"    # "256x256", "512x512", "1024x1024"
				)
				break
			except Exception as e:
				print(e)
				"""
				Certain artist names are not allowed by openai, so this loop deletes artist names from the prompt
				one by one until the prompt retrieves a successful response
				"""
				ai_prompt = ai_prompt[::-1].split(",", 1)[1]
				ai_prompt = ai_prompt[::-1]
			i -= 1

		self.image_url = response['data'][0]['url']
		user.avatar_image_url = self.image_url

		return self.image_url

