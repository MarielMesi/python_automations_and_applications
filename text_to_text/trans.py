import googletrans
from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root =  tk.Tk()
translator = Translator()
root.title('Lnaguage Translator')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

def translate():
    lang_1 = text_entry1.get(1.0, END)
    cl = choose_language.get()

    if lang_1== '':
        messagebox.showerror('Language Translator', ' Enter the text to translate!')
    else:
        text_entry2.delete(1.0, END)
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert(END, output.text)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a = tk.StringVar()

auto_select = ttk.Combobox(frame1, width=27, textvariable = a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto Select',
                        )

auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable= l, state='randomly', font=('verdana', 10, 'bold'))

choose_language['values'] = (
                                'Afrikaans',
                                'Albanian',
                                'Amharic',
                                'Arabic',
                                'Armenian',
                                'Azerbaijani',
                                'Basque',
                                'Belarusian',
                                'Bengali',
                                'Bosnian',
                                'Bulgarian',
                                'Catalan',
                                'Cebuano',
                                'Chichewa',
                                'Chinese',
                                'Corsican',
                                'Croatian',
                                'Czech',
                                'Danish',
                                'Dutch',
                                'English',
                                'Esperanto',
                                'Estonian',
                                'Filipino',
                                'Finnish',
                                'French',
                                'Frisian',
                                'Galician',
                                'Georgian',
                                'German',
                                'Greek',
                                'Gujarati',
                                'Haitian Creole',
                                'Hausa',
                                'Hawaiian',
                                'Hebrew',
                                'Hebrew',
                                'Hindi',
                                'Hmong',
                                'Hungarian',
                                'Icelandic',
                                'Igbo',
                                'Indonesian',
                                'Irish',
                                'Italian',
                                'Japanese',
                                'Javanese',
                                'Kannada',
                                'Kazakh',
                                'Khmer',
                                'Korean',
                                'Kurdish',
                                'Kyrgyz',
                                'Lao',
                                'Latin',
                                'Latvian',
                                'Lithuanian',
                                'Luxembourgish',
                                'Macedonian',
                                'Malagasy',
                                'Malay',
                                'Malayalam',
                                'Maltese',
                                'Maori',
                                'Marathi',
                                'Mongolian',
                                'Myanmar',
                                'Somali',
                                'Nepali',
                                'Norwegian',
                                'Odia',
                                'Pashto',
                                'Persian',
                                'Polish',
                                'Portuguese',
                                'Punjabi',
                                'Romanian',
                                'Russian',
                                'Samoan',
                                'Scots Gaelic',
                                'Serbian',
                                'Sesotho',
                                'Shona',
                                'Sindhi',
                                'Sinhala',
                                'Slovak',
                                'Slovenian',
                                'Spanish',
                                'Sundanese',
                                'Swahili',
                                'Swedish',
                                'Tajik',
                                'Tamil',
                                'Telugu',
                                'Thai',
                                'Turkish',
                                'Ukrainian',
                                'Urdu',
                                'Uyghur',
                                'Uzbek',
                                'Vietnamese',
                                'Welsh',
                                'Xhosa',
                                'Yiddish',
                                'Yoruba',
                                'Zulu',
                            )

choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(frame1, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg="White", cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(frame1, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg="White", cursor="hand2")
btn2.place(x=300, y=300)

root.mainloop()