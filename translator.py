from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import gtts
from gtts import gTTS
import speech_recognition as spr
import os
import time
import playsound

# Initialize Tkinter Window
root = Tk()
root.title("Language Translator")
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Language Dictionary
lang_dict = {
    'English': 'en', 'Afrikaans': 'af', 'Albanian': 'sq', 'Arabic': 'ar',
    'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be',
    'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
    'Chinese': 'zh', 'French': 'fr', 'German': 'de', 'Hindi': 'hi',
    'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko', 'Malayalam': 'ml',
    'Spanish': 'es', 'Tamil': 'ta', 'Telugu': 'te', 'Urdu': 'ur'
}

# Function to Translate Text
def translate():
    try:
        input_text = t1.get("1.0", "end-1c")
        if not input_text.strip():
            messagebox.showerror("Error", "Please enter text to translate!")
            return

        src_lang = lang_dict.get(combo1.get(), 'en')
        dest_lang = lang_dict.get(combo2.get(), 'en')

        translator = googletrans.Translator()
        translated_text = translator.translate(input_text, src=src_lang, dest=dest_lang).text

        t2.delete("1.0", "end")
        t2.insert("end", translated_text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function for Text-to-Speech
def speak():
    text = t2.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showerror("Error", "No translated text to speak!")
        return

    dest_lang = lang_dict.get(combo2.get(), 'en')

    if dest_lang not in gtts.lang.tts_langs():
        messagebox.showerror("Error", f"Text-to-Speech not supported for {combo2.get()}")
        return

    try:
        tts = gTTS(text=text, lang=dest_lang, slow=False)
        filename = f"voice_{int(time.time())}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        messagebox.showerror("Speech Error", str(e))

# Function for Speech-to-Text
def speechtotext():
    try:
        recognizer = spr.Recognizer()
        with spr.Microphone() as source:
            messagebox.showinfo("Info", "Speak now...")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language=lang_dict.get(combo1.get(), 'en'))
        t1.insert("end", text)
    except spr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio!")
    except spr.RequestError:
        messagebox.showerror("Error", "Could not connect to the speech service!")

# UI Components
Label(root, text="From Language", font=("Arial", 14, "bold"), bg="#f4f4f4").place(x=100, y=30)
combo1 = ttk.Combobox(root, values=list(lang_dict.keys()), font=("Arial", 12))
combo1.place(x=100, y=60)
combo1.set("English")

Label(root, text="To Language", font=("Arial", 14, "bold"), bg="#f4f4f4").place(x=550, y=30)
combo2 = ttk.Combobox(root, values=list(lang_dict.keys()), font=("Arial", 12))
combo2.place(x=550, y=60)
combo2.set("French")

t1 = Text(root, font=("Arial", 12), height=6, width=40, wrap=WORD)
t1.place(x=100, y=100)

t2 = Text(root, font=("Arial", 12), height=6, width=40, wrap=WORD)
t2.place(x=550, y=100)

Button(root, text="Translate", font=("Arial", 12, "bold"), bg="blue", fg="white", command=translate).place(x=400, y=250)
Button(root, text="Speak", font=("Arial", 12, "bold"), bg="green", fg="white", command=speak).place(x=550, y=250)
Button(root, text="Speech to Text", font=("Arial", 12, "bold"), bg="orange", fg="white", command=speechtotext).place(x=100, y=250)

root.mainloop()
