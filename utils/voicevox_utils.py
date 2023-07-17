from dotenv import load_dotenv, find_dotenv
import os 
_ = load_dotenv(find_dotenv())
BASE_URL=f"http://127.0.0.1:{os.getenv('VOICEVOX_PORT')}"
import urllib.parse as up
import requests

SYSTEM="WINDOWS"


#text 2 audio function 
def speak(sentence,speach_filename,base_url=BASE_URL,save_audio=False):
    speaker_id=os.getenv("speaker_id")
    params_encoded=up.urlencode({"text":sentence,"speaker": speaker_id})
    r = requests.post(f"{base_url}/audio_query?{params_encoded}")
    print(r) 
    #Raylene defulat audio settins 
    voicevox_query = r.json()
    voicevox_query["volumeScale"] = os.getenv("volumeScale")
    voicevox_query["intonationScale"] = os.getenv("intonationScale")
    voicevox_query["prePhonemeLength"]= os.getenv("prePhonemeLength")
    voicevox_query["postPhonemeLength"]= os.getenv("postPhonemeLength")

    #Sythesize voice as wav file
    params_encoded = up.urlencode({"speaker":speaker_id})
    
    r = requests.post(f"{base_url}/synthesis?{params_encoded}",json=voicevox_query)

    with open(speach_filename+".wav", "wb") as f:
        f.write(r.content)
    f.close()

    #play audio 
    if SYSTEM=="WINDOWS":
        import winsound
        winsound.PlaySound(speach_filename+".wav",winsound.SND_FILENAME)
        if not save_audio: #Delate speach filename after use 
            os.remove(speach_filename+".wav")
        else: #Save the text file as well
            #Save text 
            with open(speach_filename+".txt","w",encoding="utf-8") as f:
                f.write(sentence)
            f.close()
    else:
        import wave,pyaudio
        #Non windows audo code to finish 
        wf = wave.open(speach_filename+".wav")
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        # 音声を再生
        chunk = 1024
        data = wf.readframes(chunk)
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)
            stream.close()
            p.terminate()
