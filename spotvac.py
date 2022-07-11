from Spotvac_functions import *
import numpy as np
from tensorflow import keras
from dotenv import load_dotenv
load_dotenv()

# Load HSM
#model = keras.models.load_model('./HSM')


client_id = os.environ['client_ID']
client_secret = os.environ['client_secret']
redirect_uri = os.environ['redirect_url']
username = '22mdb5fhocl2fobpsjbxvvkra'


# Get important user data
#print("Hello, please input the 64-bit user identifier")
#print("From your spotify profile url: open.spotify.com/user/<user_id>")
#user_id = input()


#print("Now importing song data:")
plylst = download_user_playlists(username)
plylst = plylst.reset_index(drop=True)
id_playlist = plylst['playlist_id']


i = 0
psongs_list = pd.DataFrame()
for entry in id_playlist:
    name = plylst['name'][i]
    print(f"Now downloading songs from: {name}")
    playlist_songs = download_playlist(entry, 500)
    psongs_list = pd.concat([psongs_list, playlist_songs])
    i += 1
#print(psongs_list)    

#print("Prepping song data")
lsongs_list = download_liked_songs().drop_duplicates().reset_index(drop=True)
#print(lsongs_list)
dataset = pd.concat([lsongs_list,psongs_list]).drop_duplicates().reset_index(drop=True)
#dataset.to_csv('dataset')
#print(dataset)

i = 0
print('Now obtaining song features from spotify (this may take a while)')
preprocessed_dataset = pd.DataFrame()
for entry in range(len(dataset)):
    ids = dataset['song_id'][i]
    preprocessed_data = get_songs_features(ids)
    #print(preprocessed_data)
    preprocessed_dataset = pd.concat([preprocessed_data, preprocessed_dataset.loc[:]]).reset_index(drop=True)
    #print(preprocessed_dataset)
    i += 1
#print(preprocessed_dataset)
preprocessed_dataset.to_csv('prep.csv', index=False)


spotvac_playlist_list = create_spotipy_playlists()
final = evaluate_stress(preprocessed_dataset)
#results = pd.concat([results, lsongs_list.loc[2]]).reset_index(drop=True)
final.to_csv('final.csv')
#print(results)


#final = pd.read_csv('final.csv')




#create playlists and upload songs
upload_songs(final,spotvac_playlist_list)

print('------------------------------------')
print('\n')
print("All done, enjoy the playlists!")
