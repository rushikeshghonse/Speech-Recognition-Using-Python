import speech_recognition as sr


def recognize_speech():
    # Create a recognizer object
    recognizer = sr.Recognizer()
    #recognizer.energy_threshold = 300                  # use only If environment is fixed
    recognizer.dynamic_energy_threshold=True

    try:
        # Use microphone as input source
        with sr.Microphone() as source:                                               # this with block starts microphone listen for 15 sec then close it.
            print("🎤 Listening... Please speak")
            recognizer.adjust_for_ambient_noise(source,duration=0.8)                               # Adjust for background noise
            audio = recognizer.listen(source,timeout=5,phrase_time_limit=15)           # Listen to the audio

        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio,language="en-IN")
        print("✅ You said:", text)
        return text
    
    except sr.WaitTimeoutError:
        print("⏱️  Listening timed out. Please speak faster.")
        return "⏱️  Listening timed out. Please speak faster."

    except sr.UnknownValueError:
        print("❌ Could not recognize speech from the audio input")
        return "❌ Could not recognize speech from the audio input"

    except sr.RequestError:
        print("❌ Could not request results (check internet)")
        return "❌ Could not request results (check internet)"
    
    except Exception as e:
        print("⚠️ Unexpected error:", e)
        return "⚠️ Unexpected error:", e

    


if __name__ == "__main__":
    recognize_speech()

