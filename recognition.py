from ShazamAPI import Shazam


def recognize(path) :
    try :
        mp3_file_content_to_recognize = open(path, 'rb').read()

        shazam = Shazam(mp3_file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        a = next(recognize_generator)[1]['track']
        title = a['title']
        artist = a['subtitle']
        img = a['images']['coverarthq']
        return title,artist,img
    except :
        return 'Not Found','Not found','Not found'

