from cProfile import label
from tkinter import *
from turtle import clear
from mydb import Database
from tkinter import messagebox
from myapi import NLPAPI

class NLPApp:

    def __init__(self):
        self.allapi = NLPAPI()
        self.dbo = Database()
        self.root = Tk()
        self.root.title("SupaNLP")
        self.root.iconbitmap('res/favicon.ico')
        self.root.geometry("550x700")
        self.root.configure(bg = "#675ECF")
        self.logingui()
        self.root.mainloop()

    def logingui(self):

        self.clear()

        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))


        label1 = Label(self.root, text = "Enter E-Mail")
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root, width= 36)
        self.email_input.pack(pady = (10,10), ipady= 4)

    
        label2 = Label(self.root, text = "Enter Password")
        label2.pack(pady = (10,10))

        self.pass_input = Entry(self.root, width= 36, show = "*")
        self.pass_input.pack(pady = (10,10), ipady= 4)

        login_btn = Button(self.root, text = "Login" ,width= 10,  height= 1, command = self.login_input)
        login_btn.pack(pady= (40,20))
        login_btn.configure(font = (30))

        label3 = Label(self.root, text = "Not a member?", bg = "#675ECF", fg = "white")
        label3.pack(pady = (20,10))

        reg_btn = Button(self.root, text = "Register Now", command= self.register_gui)
        reg_btn.pack(pady= (1,20))


    def register_gui(self):
        self.clear()
        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))

        label1 = Label(self.root, text = "Enter Details", bg= "#675ECF", fg= "white")
        label1.pack(pady=(20,20))
        label1.configure(font =(15))

        label2 = Label(self.root,  text =" Enter Name")
        label2.pack(pady=(0,10))

        self.name_input =  Entry(self.root, width = "25")
        self.name_input.pack(pady=(0,20))

        label3 = Label(self.root,  text =" Enter E-Mail")
        label3.pack(pady=(0,10))

        self.email_input =  Entry(self.root, width = "25")
        self.email_input.pack(pady=(0,20))

        label4 = Label(self.root,  text =" Enter Password")
        label4.pack(pady=(0,10))

        self.pass_input =  Entry(self.root, width = "25", show="*")
        self.pass_input.pack(pady=(0,20))

        register_btn = Button(self.root, text = " Register", width = "20", height= "2", command = self.registration_input)
        register_btn.pack()

        label5= Label(self.root, text = "Already a member?", bg = "#675ECF", fg = "white")
        label5.pack(pady = (20,10))

        reg_btn = Button(self.root, text = "Login Now", command= self.logingui)
        reg_btn.pack(pady= (1,20))

    def clear (self):

        for i in self.root.pack_slaves():
            (i.destroy())

    def registration_input(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo("Success", "Registration successful")

        else:
            messagebox.showerror("Error", "Email already exists")
    
    def login_input(self):

        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.login_data(email, password)

        if response:
            messagebox.showinfo("Success", "Login successful")
            self.nlpoptions()

        else:
            messagebox.showerror("Error", "Invalid email or password")
        

    def nlpoptions(self):
        self.clear()
        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))

        sentiment_btn = Button(self.root, text = "Sentiment Analysis", command= self.sentimentgui)
        sentiment_btn.pack(pady=(60,10))
        sentiment_btn.configure(font= ("Helvetica", 20))

        ner_btn = Button(self.root, text = "NER", command=self.nergui)
        ner_btn.pack(pady=(10,10))
        ner_btn.configure(font= ("Helvetica", 20))

        translate_btn = Button(self.root, text = "Translator", command=self.translategui)
        translate_btn.pack(pady=(10,30))
        translate_btn.configure(font= ("Helvetica", 20))

        logout_btn = Button(self.root, text = "LogOut", command= self.logingui)
        logout_btn.pack(pady= (30,20))

        
        
    def sentimentgui(self):

        self.clear()
        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))

        heading2 = Label(self.root, text = "Sentiment Analysis", bg = "#675ECF", fg = "white")
        heading2.pack(pady = (10,20))
        heading2.configure(font = ("verdana", 18, "bold"))

        label1 = Label(self.root,  text ="Enter Text Here: ",bg = "#675ECF", fg="white")
        label1.pack(pady=(0,10))

        self.sentiment_input =  Entry(self.root, width = "25")
        self.sentiment_input.pack(pady=(0,20))

        sentanalayze_btn = Button(self.root, text = "Analayze", command=self.do_sentiment_analysis)
        sentanalayze_btn.pack(pady=(10,20))
        sentanalayze_btn.configure(font= ("Helvetica", 10))

        self.sentiment_result = Label(self.root, text = "", bg = "#675ECF", fg="white")
        self.sentiment_result.pack()
        self.sentiment_result.configure(font = (16))

        back_btn = Button(self.root, text = "Back",  command = self.nlpoptions)
        back_btn.pack(pady=(0,30))
        back_btn.configure(font= ("Helvetica", 9))


    def translategui(self):

        self.clear()
        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))

        heading2 = Label(self.root, text = "Translator", bg = "#675ECF", fg = "white")
        heading2.pack(pady = (10,20))
        heading2.configure(font = ("verdana", 18, "bold"))

        label1 = Label(self.root,  text ="Enter Text Here: ",bg = "#675ECF", fg="white")
        label1.pack(pady=(0,10))

        self.translate_input =  Entry(self.root, width = "30")
        self.translate_input.pack(pady=(0,20))

        label2 = Label(self.root,  text ="Enter Target Language: ",bg = "#675ECF", fg="white")
        label2.pack(pady=(0,10))

        self.langinput = Entry(self.root,width = "20")
        self.langinput.pack()

        translate_btn = Button(self.root, text = "Translate", command=self.do_translate)
        translate_btn.pack(pady=(10,20))
        translate_btn.configure(font= ("Helvetica", 10))

        self.translate_result = Label(self.root, text = "", bg = "#675ECF", fg="white")
        self.translate_result.pack()
        self.translate_result.configure(font = (16))

        back_btn = Button(self.root, text = "Back",  command = self.nlpoptions)
        back_btn.pack(pady=(0,30))
        back_btn.configure(font= ("Helvetica", 9))


    def nergui(self):

        self.clear()
        heading = Label(self.root, text = "Welcome to SupaNLP", bg = "#675ECF", fg = "#191363")
        heading.pack(pady = (30,20))
        heading.configure(font = ("verdana", 25, "bold", "italic"))

        heading2 = Label(self.root, text = "NER Entity Extraction", bg = "#675ECF", fg = "white")
        heading2.pack(pady = (10,20))
        heading2.configure(font = ("verdana", 18, "bold"))

        label1 = Label(self.root,  text ="Enter Text Here: ",bg = "#675ECF", fg="white")
        label1.pack(pady=(0,10))

        self.ner_text =  Entry(self.root, width = "25")
        self.ner_text.pack(pady=(0,20))

        label2 = Label(self.root,  text ="Enter Entity name: ",bg = "#675ECF", fg="white")
        label2.pack(pady=(0,10))

        self.ner_entity =  Entry(self.root, width = "25")
        self.ner_entity.pack(pady=(0,20))

        sentanalayze_btn = Button(self.root, text = "Extract", command=self.do_ner)
        sentanalayze_btn.pack(pady=(10,20))
        sentanalayze_btn.configure(font= ("Helvetica", 10))

        self.ner_result = Label(self.root, text = "", bg = "#675ECF", fg="white")
        self.ner_result.pack()
        self.ner_result.configure(font = (16))

        back_btn = Button(self.root, text = "Back",  command = self.nlpoptions)
        back_btn.pack(pady=(0,30))
        back_btn.configure(font= ("Helvetica", 9))

    def do_sentiment_analysis(self):

        self.text_response = self.sentiment_input.get()

        senti = self.allapi.sentiment_api(self.text_response)
        self.sentiment_result ["text"] = senti


    def do_ner(self):

        self.text = self.ner_text.get()
        self.entity = self.ner_entity.get()

        ner = self.allapi.ner_api(self.text, self.entity)
        self.ner_result ["text"] = ner


    def do_translate(self):

        self.inputran = self.translate_input.get()
        self.target_lang = self.langinput.get()

        translated = self.allapi.translate_api(self.inputran, self.target_lang)
        self.translate_result ["text"] = translated


akshat = NLPApp()