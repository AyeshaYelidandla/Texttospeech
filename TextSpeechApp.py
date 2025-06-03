import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import speech_recognition as sr

class TextSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text <-> Speech Converter")
        master.geometry("400x350")
        master.configure(bg="#e3f2fd")

        tk.Label(master, text="Text to Speech", font=("Arial", 14, "bold"), bg="#e3f2fd", fg="#1565c0").pack(pady=8)
        self.text_entry = tk.Text(master, height=5, width=40, font=("Arial", 11))
        self.text_entry.pack(pady=5)
        tk.Button(master, text="Speak Text", command=self.text_to_speech, bg="#90caf9", fg="#0d47a1", font=("Arial", 11, "bold")).pack(pady=5)

        tk.Label(master, text="Speech to Text", font=("Arial", 14, "bold"), bg="#e3f2fd", fg="#2e7d32").pack(pady=8)
        tk.Button(master, text="Record Speech", command=self.speech_to_text, bg="#a5d6a7", fg="#1b5e20", font=("Arial", 11, "bold")).pack(pady=5)
        self.speech_result = tk.StringVar()
        tk.Label(master, textvariable=self.speech_result, wraplength=350, font=("Arial", 11), bg="#e3f2fd", fg="#4e342e").pack(pady=5)

    def text_to_speech(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("No Text", "Please enter text to speak.")
            return
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.speech_result.set("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                self.speech_result.set("Recognizing...")
                text = recognizer.recognize_google(audio)
                self.speech_result.set(f"You said: {text}")
            except sr.WaitTimeoutError:
                self.speech_result.set("No speech detected. Try again.")
            except sr.UnknownValueError:
                self.speech_result.set("Could not understand audio.")
            except sr.RequestError:
                self.speech_result.set("Could not request results; check your internet connection.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextSpeechApp(root)
    root.mainloop()
