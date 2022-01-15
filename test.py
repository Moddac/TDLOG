from ShazamAPI import Shazam

url='Luis Fonsi - Despacito ft. Daddy Yankee.mp3'

def recognize(url) :
    try :
        mp3_file_content_to_recognize = open(url, 'rb').read()

        shazam = Shazam(mp3_file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        a = next(recognize_generator)[1]['track']
        title = a['title']
        artist = a['subtitle']
        img = a['images']['coverarthq']
        return title,artist,img
    except
        return 'Not Found','Not found','Not found'

recognize(url)