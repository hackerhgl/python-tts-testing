from gtts import gTTS
import pyttsx3
import os

TMP_DIR = "tmp"

def safe_mkdir():
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)


def s_pyttsx3():
    engine = pyttsx3.init()
    # print(engine.getProperty('voices'))
    voices = engine.getProperty('voices')
    neuter = 'VoiceGenderNeuter'
    print(voices[0])
    # filtered = [voice for voice in voices if voice.languages[0].find("en") > -1 and voice.gender != neuter]
    # filtered = [voice for voice in voices if voice.languages[0] == 'en_US' and voice.gender != neuter]
    # print(filtered[0].gender)
    # for voice in filtered:
    #     print(voice)
    #     engine.setProperty('voice', voice.id)  # changes the voice
    #     engine.say('The quick brown fox jumped over the lazy dog.')
    #     engine.runAndWait()

    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

    # engine.say("Men of Reddit, what’s the best response to \"Haha you have a small penis?\"")
    # engine.setProperty('rate', 175)
    # engine.say("Men of Reddit, what’s the best response to \"Haha you have a small penis?\"")
    # engine.runAndWait()
    # engine.say("That's my clitoris ma'am.")
    # engine.runAndWait()

def s_gtts():
    blabla = "Men of Reddit, what’s the best response to \"Hey champ, how's it going? anything good?\""
    tts = gTTS(text=blabla, lang='en', tld="co.uk")
    safe_mkdir()
    tts.save(os.path.join(TMP_DIR, "test-1.mp3"))
def main():
    s_gtts()
    # s_pyttsx3()


if __name__ == "__main__":
    main()