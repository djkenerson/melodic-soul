# melodic-soul
Ever wondered what your favorite music says about you? Melodic Soul analyzes your Spotify music tastes and behaviors using VADER sentiment analysis over the last 6 months. The program then feeds that data into the DALL-E text-to-image AI algo to generate an image of your personalized Melodic Soul. What does your Melodic Soul look like? Give it a try today!

## Examples
<p float="left">
  <img src="https://user-images.githubusercontent.com/25855913/215732211-30a7cbeb-14a4-4777-83f0-91b68e93061d.png" width="400" height="400">
  <img src="https://user-images.githubusercontent.com/25855913/215731379-6fa5d344-1852-43f9-8dfe-7ff0197d9e21.png" width="400" height="400">
</p>

### Spotify & Sentiment Analysis For Left Image

#### Top Tracks
- Something in the Orange by Zach Bryan;	 Sentiment: Extremely Negative
- Heading South by Zach Bryan;		 Sentiment: Neutral
- Goodbye Carolina by The Marcus King Band;		 Sentiment: Extremely Positive
- Stayin' Alive VS 50 C Tik Tok - Remix by ROSE BEAT;		 Sentiment: Positive
- Sunny Nelson (Edit) by Abel Tasman;		 Sentiment: Neutral

#### Sentiment
- The average sentiment of your most frequently played songs is: Neutral

#### Top Artists
- Tyler Childers
- Mumford & Sons
- Rage Against The Machine
- Cody Jinks
- The Marcus King Band

#### Top Genres
- rock
- stomp and holler
- outlaw country
- contemporary country
- edm

#### Top Albums
- Tribe
- Paranoid (Remaster)
- Infest
- Stranger Things, Vol. 1 (A Netflix Original Series Soundtrack)
- hail mary

## Five-Step Quickstart
1. Sign up for free [musixmatch developer account](https://developer.musixmatch.com/plans) and save API key to "musixmatch_secret.txt" file.
2. Sign up for free [openai developer account](https://openai.com/api/) and save API key to "openai_secret.txt" file.
3. Sign up for free [Spotify developer account](https://developer.spotify.com/). Create a new app. Click "Edit Settings". Set the "Redirect URI" to "http://localhost:8888/callback". Scroll down and click "Save". Navigate back to the app dashboard. You should see the "Client ID" and "Client Secret" on this page. Save the "Client ID" as the first line on the "spotify_secret.txt file" and the "Client Secret" as the second line.
4. Scan the list of packages below and install any missing ones.
5. Download the program files and run "main.py". Within a minute, you'll receive a summary of your Spotify listening stats and sentiment. You'll also receive a link to an image of your Melodic Soul. Make sure to download and save it since the hosted image will expire within one hour. If you don't like your image then run the program again or start listening to some new music! :)

### Required Packages
```
pip install spotipy
pip install statistics
pip install musixmatch
pip install vaderSentiment
pip install openai
pip install uuid
```
## Demo

https://user-images.githubusercontent.com/25855913/215750602-ff53d164-482b-483a-b074-5e2339d2d4c5.mp4
