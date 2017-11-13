'''This is the jarvis thread implemementation'''


import Audio_to_text_translator as AudioConverter
import Jarvis_WebPage as JWeb
from threading import Thread
import queue
import File_operations as operations
import Text_Audio_converter as txt_audio


q = queue.Queue()

def get_voice():

    while(1):
        print('thread1')
        Audio_Txt = AudioConverter.main()
        print('Audio is putted in queue->',Audio_Txt)
        q.put(Audio_Txt)


def run_command(q):

    while True:
        Audio_Txt=q.get()
        print('thread2')
        print('Audio tet to get from queue',Audio_Txt)
        if 'jarvis' in Audio_Txt.lower():
            Audio_list = Audio_Txt.split(' ')
            print('Audio_Txt-->',Audio_Txt)
            if 'play' in Audio_list:
                txt = ' '.join(Audio_list[2:])
                print('play')
                print(txt)
                txt_audio.text_to_audio('Playing %s'%txt )
                JWeb.youtubeSearch(txt)
            elif 'search' in Audio_Txt:
                txt = ' '.join(Audio_list[2:])
                print('search')
                print(txt)
                JWeb.websearch(txt)
            elif 'lock my system' in Audio_Txt:
                print('inside lock')
                operations.LockMySystem()



        q.task_done()



t1 = Thread(target=get_voice ,args=())
t2 = Thread(target=run_command, args=(q,))
t1.start()
t2.start()


