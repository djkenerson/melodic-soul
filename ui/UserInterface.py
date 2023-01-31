class UserInterface:
	"""
	WIP: would like to standardize the user interface into a menu like below
	"""

	def __init__(self):
		self.running = True

	def display_summary_stats(self, user):

		print("\n---TOP TRACKS LAST 6 MONTHS---")
		for item in user.top_tracks[0:5]:
			if (item.sentiment is None):
				print(item.name + " by " + item.artists[0].name)
			else:
				print(item.name + " by " + item.artists[0].name + "\t\t Sentiment: " + item.sentiment)

		print("\n---SENTIMENT LAST 6 MONTHS---")
		print("The average sentiment of your most frequently played songs is: " + user.sentiment)

		print("\n---TOP ARTISTS LAST 6 MONTHS---")
		for item in user.top_artists[0:5]:
			print(item.name)

		print("\n---TOP GENRES LAST 6 MONTHS---")
		for item in user.top_genres[0:5]:
			print(item)

		print("\n---TOP ALBUMS LAST 6 MONTHS---")
		for item in user.top_albums[0:5]:
			print(item.name)

	def display_menu(self):
		print('\n---- PROGRAM ACTIONS ----')
		print('1. Show me my melodic soul')
		print("2. Show my melodic soul's sentiment")
		print('3. Show my favorite tracks')
		print('4. Show my favorite artists')
		print('5. Show my favorite genres')
		print('6. Show my favorite albums')
		print("Enter 'q' to quit.\n")

	def start(self, user):

		while(self.running):

			# display menu and ask for input
			self.displayMenu()
			input = input("\nAction Number: ")

			# check if input is valid
			try:
				integer = int(integer)
			except ValueError:
				print('The provided value is not an integer between 1 and 6. Please try again.')
				continue
			if (input >= 1 or input <= 6):
				print('The provided value is not an integer between 1 and 6. Please try again.')
				continue

			# quit on q input
			if (input == 'q'):
				print('Quitting. Thanks!')
				self.running = False
				break

			match input:
				case 1:
					print("\n---MELODIC SOUL IMAGE URL---")
					print(user.avatar_image_url)
				case 2:
					print("\n---SENTIMENT---")
					print("The average sentiment of your most frequently played songs is: " + u.sentiment)
				case 3:
					print("\n---TOP TRACKS---")
					for item in user.top_tracks[0:5]:
						if (item.sentiment is None):
							print(item.name + " by " + item.artists[0].name)
						else:
							print(item.name + " by " + item.artists[0].name + "\t\t Sentiment: " + item.sentiment)
				case 4:
					print("\n---TOP ARTISTS---")
					for item in user.top_artists[0:5]:
						print(item.name)
				case 5:
					print("\n---TOP GENRES ---")
					for item in user.top_genres[0:5]:
						print(item)
				case 6:
					print("\n---TOP ALBUMS ---")
					for item in user.top_albums[0:5]:
						print(item.name)






