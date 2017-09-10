#Importing Libraries needed
# @fekiee
import pymysql
import pprint
import sys
import spotipy
import spotipy.util as util
import simplejson as json

#-----------------Database connector------------------------------
#Creating connection to localhost
connection = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='databasename',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
 
cursor = connection.cursor()
#----------------------------------------------------------------

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #ranges = ['medium_term', 'long_term']
    #for range in ranges:
       # print "range:", range
    results = sp.current_user_top_artists(limit=8)
    for i, item in enumerate(results['items']):
      #print statement
        print i, " Artist Name: ", item['name'], "   Genre: ", item['genres'][0], "-", item['genres'][1], "-", item['genres'][2]

            

else:
    print("Can't get token for", username)

#------------------------------Database insert--------------------------------
#Query to insert information into 'artists' database 

query = "INSERT INTO `artists` (aName, aGenre, aGenre2, aGenre3) VALUES (%s, %s, %s,%s)"


#------------------------------Setting Values--------------------------------

aName = item['name']
aGenre = item['genres'][0]
aGenre2 = item['genres'][1]
aGenre3 = item['genres'][2]
addData = (aName, aGenre, aGenre2, aGenre3)

#To Execute 
cursor.execute(query, addData)
 
connection.commit()



#----------------- Spotify App Credentials --------------------------
#   export SPOTIPY_CLIENT_ID='your-spotify-client-id'
#   export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
#   export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
