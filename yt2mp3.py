import os 
import re
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
from pytube import YouTube

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Cole a Url do Video do Youtube")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.urlLabel = Label(self.segundoContainer,text="URL", font=self.fontePadrao)
        self.urlLabel.pack(side=LEFT) 
        self.url = Entry(self.segundoContainer)
        self.url["width"] = 60
        self.url["font"] = self.fontePadrao
        self.url.pack(side=LEFT) 
        
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Download"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        

    def mtd(self): 
        self.mensagem["text"] = "aguarde..."  
        root.update()         
       


    #Método verificar senha
    def verificaSenha(self):
        self.mtd()
        
        yt = YouTube(self.url.get()) 
        file_name = yt.title 
        
        nome_limpo = re.sub('[^a-zA-Z0-9 ]', '', file_name)
        
        root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",initialfile = nome_limpo, filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
        mp4file = root.filename
        print("ppp>>>" + mp4file)
        #mp4file = r'C:\\Users\\enzo\\Desktop\\'
         
        yt.streams.get_highest_resolution().download(mp4file  , filename= nome_limpo + '.mp4')

        full_name = mp4file +'\\' + nome_limpo + '.mp4'
        
        
        print("pppffff>>>" + full_name)
        print(full_name)
        videoclip = VideoFileClip(full_name)
        audioclip = videoclip.audio
        end = audioclip.write_audiofile(mp4file + '\\' + nome_limpo + ".mp3")         
        videoclip.close()
        audioclip.close()
   
        self.mensagem["text"] = "SUCCESS!! FINISH!!"  
        
root = Tk()

Application(root)
root.mainloop()
 