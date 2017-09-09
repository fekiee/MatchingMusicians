Spotify API credentials must be set as environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

Source code include database connector to insert the user-top-read into database in order to create the matching algorithm.

To run the source code the following libraries must be installed previously:

 - JSON library for python
 - call library
 - Spotipy
 - flask.

A local database was set to run the code and store the data retrieved


