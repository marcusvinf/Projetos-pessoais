import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os, shutil
from PIL import Image, ImageTk

x = " "
def pasta_backup(caminho):
    pbp = caminho+'/Backup/'
    print(pbp)
    try:
        if not os.path.exists(pbp):
            os.makedirs(pbp)
    except OSError:
        print ('Erro ao criar diretório. ' +  pbp)
    for filename in os.listdir(caminho):
        shutil.copy(filename, pbp)


def renomear(caminho, nome):
    pasta_backup(caminho)    
    for filename in os.listdir(caminho):
        temp = filename.split(" ")
        temp2 = temp[-1]
        temp2 = temp2.split(".")
        temp[-1]=temp2[0]
        dst = ' '.join(temp)
        dst = dst +" " + nome + ".pdf"
        src = caminho+ '/'+filename 
        dst =caminho+'/' +dst 
        os.rename(src, dst)
        
def selecionar_pasta():
    global folder_path
    global x
    filename = filedialog.askdirectory()
    x = filename
    folder_path.set(filename)
    list = os.listdir(x) # dir is your directory path
    number_files = str(len(list))
    lb_arq= Label(window,text=("A pasta tem "+number_files+" arquivos."),bg='#D43A24')
    lb_arq.place(x=0, y=88)

def alterar_pdf():
    nome = entrada.get()
    
    if x != " ":
        if nome != "":
            renomear(x, nome)
            lb_renome= Label(window,text="Arquivos alterados com sucesso.",bg='#D43A24')
            lb_renome.place(x=0, y=170)
        else:
            lb_renome= Label(window,text="Digite um nome válido para o arquivo.",bg='#D43A24')
            lb_renome.place(x=0, y=170)
    elif x == " ":
        lb_renome= Label(window,text="Escolha o caminho do arquivo.",bg='#D43A24')
        lb_renome.place(x=0, y=170)
        
    



    

     

########BACKGROUND##########3
window = tk.Tk()
window.title("Renomear pdf - Connectoway")
window.geometry("700x500")
image = Image.open('cwaybg.png')
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(window, image = photo_image)
label.pack()
folder_path = StringVar()


############ LABEL BUTAO ############
bt = Button(window, width=20, text="Selecione a Pasta", command=selecionar_pasta)
bt.place(x=0,y=25)

########LABEL DIRETORIO########
lb1= Label(window,text="Diretório: ",bg='#D43A24')
lb1.place(x=0, y=50)
########LABEL CAMINHO##########
lb2 = Label(window,textvariable=folder_path,bg='#D43A24')
lb2.place(x=0, y=70)


########### ENTRADA DE TEXTO ##########

entrada = Entry(window)
entrada.place(x=0, y= 120)


##############BOTAO DE CONFIRMACAO############
btconf = Button(window,width=20,text="Confirmar",command=alterar_pdf)
btconf.place(x=0,y=140)

###############LABEL DE CORREÇÃO############


##########BOTAO DE CORREÇÃO#############






window.mainloop()
