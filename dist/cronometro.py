from tkinter import * 

janela = Tk()
janela.title('Cronômetro')

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela.geometry('300x180')
janela.config(bg=cor1)
janela.resizable(width=False,height=False)

# funcoes
global tempo
global rodar
global contador
global limite

tempo = "00:00:00"
rodar = False
contador = -5
limite = 59

def play():
    global tempo
    global rodar
    global contador
    global limite

    if rodar:
        if contador <= -1:
            incio = 'Começando em ' + str(contador)
            tempo_L['text'] = incio
            tempo_L['font'] = 'Arial 10'


        else:
            tempo_L['font'] = 'Times 50 bold'
            temporario = str(tempo)
            h,m,s = map(int,temporario.split(":"))
            h = int(h); m = int(m); s = int(contador)

            if(s>=limite):
                contador = 0
                m += 1
            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

            # Atualiza valores
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            tempo_L['text'] = temporario
            tempo = temporario

        tempo_L.after(1000,play)
        contador += 1

def start():
    global rodar
    # if(rodar == True):
    #     return False
    rodar = True
    tempo_L['fg'] = cor3
    play()

def pausar_buttom():
    global rodar
    rodar = False
    tempo_L['fg'] = cor4

def reiniciar_buttom():
    tempo_L['text'] = "00:00:00"
    tempo_L['fg'] = cor3
    global contador
    contador = 0 


# Criando labels ------------

cronometro_L = Label(janela,text='Cronômetro',font="Arial 10",bg=cor1,fg=cor2)
cronometro_L.place(x=20,y=5)

tempo_L = Label(janela,text=tempo,font="Times 50 bold",bg=cor1,fg=cor3)
tempo_L.place(x=20,y=30)

# Criando botoes -----------

iniciar = Button(janela,command=start,text='Iniciar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 8 bold',relief=RAISED,overrelief=RIDGE)
iniciar.place(x=20,y=130)

pausar = Button(janela,command=pausar_buttom,text='Pausar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 8 bold',relief=RAISED,overrelief=RIDGE)
pausar.place(x=105,y=130)

reiniciar = Button(janela,command=reiniciar_buttom,text='Reiniciar',width=10,height=2,bg=cor1,fg=cor2,font='Ivy 8 bold',relief=RAISED,overrelief=RIDGE)
reiniciar.place(x=190,y=130)

janela.mainloop()
