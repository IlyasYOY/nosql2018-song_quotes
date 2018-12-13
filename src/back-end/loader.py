import lyricscorpora as lc
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/songs')

if __name__ == "__main__":
    billboard = lc.Billboard(50)
    collection = client.get_database('songs').get_collection('songs')
    for i, song in enumerate(billboard.song_list, 1):
        print(i, len(billboard.song_list))
        try:
            text = song.get_lyrics()()
        except:
            print('skip')
            continue
        artist_name = song.artist.name
        title = song.title
        collection.insert_one({
            'title': title,
            'artist': artist_name,
            'text': text
        })