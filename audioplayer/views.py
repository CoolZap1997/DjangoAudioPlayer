import pyglet
import time
from django.http import HttpResponse
from gtts import gTTS
import os
import glob

# Function to play the sound
def play_sound(request):
    player = pyglet.media.Player()
    sound_file = "C:/Users/dw1093/Downloads/Alerts/output.wav"
    source = pyglet.media.StaticSource(pyglet.media.load(sound_file))
    player.queue(source)
    player.play()
    time.sleep(4)  # Wait for 5 seconds (adjust as needed)
    player.pause() 
    player.delete()
    return HttpResponse("Audio played successfully.")

# def play_any_sound(request):
#     audio_text = request.GET.get('audio_text')
#     # return HttpResponse(f'You submitted: {audio_text}')
#     language = "en"
#     tts = gTTS(text=audio_text, lang=language, slow=False)
#     tts.save("C:/Users/dw1093/Downloads/Alerts/custom.wav")
#     del tts
#     player = pyglet.media.Player()
#     sound_file = "C:/Users/dw1093/Downloads/Alerts/custom.wav"
#     source = pyglet.media.StaticSource(pyglet.media.load(sound_file))

#     player.queue(source)
#     player.play()
#     time.sleep(4)  # Wait for 5 seconds (adjust as needed)
#     player.pause() 
#     player.delete()
#     return HttpResponse("Audio played successfully.")


def play_any_sound(request):
    audio_text = request.GET.get('audio_text')
    language = "en"
    
    file_number = int(time.time())  # Use a timestamp as a unique number
    audio_filename = f"C:/Users/dw1093/Downloads/Alerts/audio_player_project/audioplayer/audios/custom{file_number}.wav"

    tts = gTTS(text=audio_text, lang=language, slow=False)
    tts.save(audio_filename)

    player = pyglet.media.Player()
    source = pyglet.media.StaticSource(pyglet.media.load(audio_filename))
    player.queue(source)
    player.play()
    time.sleep(4)  # Wait for 4 seconds (adjust as needed)
    player.pause() 
    player.delete()
    
    return HttpResponse("Audio played successfully.")
