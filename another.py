from tkinter import *
from googletrans import Translator, LANGUAGES  # Correct import
import customtkinter
from tkinter import messagebox

WIN = customtkinter.CTk()
WIN.title("DXM - TRANSLATOR")
WIN.config(bg="#121212")
WIN.geometry("1060x300")
WIN.resizable(False, False)

def translate_it():
    translated_text.delete(1.0, END)
    try:
        from_language_key = next((key for key, value in LANGUAGES.items() if value == original_combo.get()), None)
        to_language_key = next((key for key, value in LANGUAGES.items() if value == translated_combo.get()), None)

        if from_language_key and to_language_key:
            translator = Translator()
            text = original_text.get(1.0, END).strip()
            translation = translator.translate(text, src=from_language_key, dest=to_language_key)
            translated_text.insert(1.0, translation.text)
        else:
            messagebox.showerror("Translator", "Please select valid languages.")
    except Exception as e:
        messagebox.showerror("Translator", f"Translation Error: {e}")

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

language_list = list(LANGUAGES.values())

# APP DESIGN 
main_frame = customtkinter.CTkFrame(WIN, width=970, height=620, corner_radius=10, fg_color="#212124")
main_frame.grid(row=1, column=0, padx=17)

original_frame = customtkinter.CTkFrame(main_frame, width=650, height=50, corner_radius=10, fg_color="#2d2d31")
original_frame.grid(row=1, column=0, padx=17)

original_combo = customtkinter.CTkComboBox(original_frame, width=300, values=language_list, border_color="#45454c", fg_color="#45454c", button_color="#45454c", button_hover_color="#5915E4")
original_combo.grid(row=0, column=0, padx=17, pady=15)
original_combo.set("Select Source Language")

clear_button = customtkinter.CTkButton(original_frame, text="CLEAR TEXT", font=("Helvetica", 13), text_color="#c3c3c9", border_color="#8f8f9a", fg_color=None, hover_color="#212124", border_width=2, height=30, width=50, command=clear)
clear_button.grid(row=0, column=1, padx=15)

original_frame1 = customtkinter.CTkFrame(main_frame, width=600, height=230, corner_radius=10, fg_color="#2d2d31")
original_frame1.grid(row=3, column=0, padx=17)

original_text = Text(original_frame1, height=7, width=56, bd=0, font=("Helvetica", 14), wrap=WORD, bg="#2d2d31", fg="#E3E6EA", highlightthickness=0)
original_text.pack(pady=10, padx=10)

translated_frame = customtkinter.CTkFrame(WIN, width=970, height=620, corner_radius=10, fg_color="#212124")
translated_frame.grid(row=1, column=1)

translated_frame1 = customtkinter.CTkFrame(translated_frame, width=650, height=50, corner_radius=10, fg_color="#2d2d31")
translated_frame1.grid(row=1, column=0, padx=17)

translated_combo = customtkinter.CTkComboBox(translated_frame1, width=300, values=language_list, border_color="#45454c", fg_color="#45454c", button_color="#45454c", button_hover_color="#5915E4")
translated_combo.grid(row=0, column=0, padx=17, pady=15)
translated_combo.set("Select Target Language")

translate_button = customtkinter.CTkButton(translated_frame1, text="TRANSLATE", font=("Helvetica", 13), fg_color="#5915E4", hover_color="#4318AC", width=50, height=30, command=translate_it)
translate_button.grid(row=0, column=1, padx=17)

translated_frame2 = customtkinter.CTkFrame(translated_frame, width=600, height=200, corner_radius=10, fg_color="#2d2d31")
translated_frame2.grid(row=3, column=0, padx=17)

translated_text = Text(translated_frame2, height=7, width=55, bd=0, font=("Helvetica", 14), wrap=WORD, bg="#2d2d31", fg="#E3E6EA", highlightthickness=0)
translated_text.pack(pady=10, padx=10)

WIN.mainloop()
