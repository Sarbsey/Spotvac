
# Spotvac

This project is a simple program that uses spotipy to interface with the Spotify API. It collects 
songs from the user's public playlists as well as liked songs, and uses a simple ML model to categorize
each song into a playlist depending on "stress" levels. 


## Acknowledgements
I would like to aknowledge my friend Andrew who gave me this idea, Alex who gave it a good name, and
my girlfriend who is just great in general.

## Installation

Get your own Spotify API ID and secret [here](https://developer.spotify.com/dashboard/),
and then set redirect url to something like 'http://localhost:8000' in the settings.

Then just set up an .env like the following:

```bash
# .env

client_ID = "your-client_ID-here"
client_secret = "your-client_secret-here"
redirect_url = "your-redirect_uri-here"
username = "your-base64-username-here" 
#on your spotify profile, https://open.spotify.com/user/<username> 
```

Lastly set up the following modules (I would suggest doing this in a [venv](https://code.visualstudio.com/docs/python/environments))
- spotipy
- pandas
- ipython
- python-dotenv
- tensorflow
```bash
pip install <module>
```    
Or do it from the requirements.txt included
## Used By

Idiots

