from data.ReadSpotifyData import ReadSpotifyData
from util.Album import Album
from util.Artist import Artist
from util.Track import Track
from util.User import User
from processor.AIPrompt import AIPrompt
from processor.Sentiment import Sentiment
from processor.SpotifyAvatar import SpotifyAvatar
from ui.UserInterface import UserInterface
import time


if __name__ == '__main__':

    # TODO: Build a frontend
    # TODO: Add menu in 'UserInterface'
    # TODO: Error handling
    # TODO: Unit tests
    # TODO: Better documentation and comments

    print()
    print("Welcome to the melodic soul generator! "
          "We'll analyze your Spotify music tastes and the answers to the following questions to generate your own "
          "unique Spotify avatar. Enjoy!")
    print()

    # Retrieve input from user
    while (True):
        firstname = input("What is your first name? ")
        if (firstname is None or type(firstname) != str):
            print("String input only. Please try again.")
            continue
        break

    while (True):
        lastname = input("What is your last name? ")
        if (lastname is None or type(lastname) != str):
            print("String input only. Please try again.")
            continue
        break

    while (True):
        gender = input("What is your gender from the following list? Female, Male, Non-binary, "
                         "Intersex, Two-Spirit, Gender non-conforming, Transgender, Other, Prefer not to disclose. ")
        if (gender is None or type(gender) != str):
            print("String input only. Please try again. ")
            continue
        if (gender not in ['Female','Male','Non-binary','Intersex','Two-Spirit','Gender non-conforming','Transgender','Other','Prefer not to disclose']):
            print("Please choose from the list.")
            continue
        break

    while (True):
        age = input("What is your age? Enter -1 if you prefer not to disclose. ")
        try:
            age = int(age)
        except:
            print("Integer input only. Please try again.")
            continue
        if age == -1:
            break
        if (age <= 0):
            print("Please choose a real age :)")
            continue
        break

    # Initialize user
    u = User(firstname, lastname, gender, age)

    print("\nAnalyzing your Spotify music tastes and generating your melodic soul using AI! Hold tight, this will take less than a minute.")

    # Auth into spotify and initialize spotify object
    rds = ReadSpotifyData('spotify_secret.txt')
    sp = rds.spotify_object

    # Retrieve Spotify tracks and albums that the user listened to the most over last 6mo and assign them to user object
    rds.top_tracks(u, 'medium_term')

    # Retrieve Spotify artists and genres that the user listened to the most over last 6mo and assign them to user object
    rds.top_artists(u, 'medium_term')

    # Determine sentiment of user by averaging VADER sentiment scores of most frequently played tracks
    s = Sentiment('musixmatch_secret.txt')
    s.user_sentiment_score(u)

    # Generate a text-to-image AI prompt describing the Melodic Soul based on the user's music tastes, attributes and sentiment
    a = AIPrompt()
    prompt = a.ai_prompt(u)
    # print(prompt)

    # Pass the prompt to DALL-E AI model and retrieve the Spotify Melodic Soul image url - click to see the image!
    sa = SpotifyAvatar('openai_secret.txt')
    spotify_avatar_image_url = sa.spotify_avatar(u, prompt)
    print("\nAlmost finished...")
    time.sleep(3)
    print("\nClick the link below!")
    print(spotify_avatar_image_url)

    print("\nHere's all the data that we used to generate your melodic soul:")

    # Print summary stats about the user's Spotify musical tastes and sentiment
    ui = UserInterface()
    ui.display_summary_stats(u)



