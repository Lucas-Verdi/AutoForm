import pyautogui as pag
from pyautogui import *
import tkinter as tk
from tkinter import *
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

def programa():

    #Clicar na tela do excel
    pag.moveTo(713, 21)
    pag.click()

    #Copiar e colar para planilha 1
    pag.moveTo(20, 310)
    sleep(0.2)
    pag.click()
    pag.rightClick()
    pag.moveTo(117, 383)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(512, 963)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(89, 332)
    sleep(0.2)
    pag.rightClick()
    sleep(0.2)
    pag.moveTo(137, 456)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(66, 339)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    #Separar as colunas necessárias
    pag.moveTo(373, 310)
    pag.sleep(0.2)
    pag.click()
    pag.keyDown('ctrl')
    sleep(0.2)
    pag.moveTo(470, 310)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(563, 309)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(760, 312)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(948, 309)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1044, 309)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1142, 308)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1336, 308)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1427, 308)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1620, 308)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1718, 308)
    pag.sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    pag.rightClick()
    sleep(0.2)
    pag.moveTo(1455, 611)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(953, 319)
    sleep(0.2)
    pag.click()
    pag.keyDown('ctrl')
    pag.sleep(0.2)
    pag.moveTo(1044, 307)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1137, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1235, 304)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1334, 306)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1432, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1526, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1620, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1715, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1816, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    pag.rightClick()
    pag.moveTo(1548, 618)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(956, 307)
    pag.sleep(0.2)
    pag.click()
    pag.keyDown('ctrl')
    pag.moveTo(1048, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1141, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1239, 321)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1439, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1522, 302)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1626, 306)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1718, 306)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1814, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    pag.rightClick()
    sleep(0.2)
    pag.moveTo(1521, 624)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1037, 312)
    sleep(0.2)
    pag.click()
    pag.keyDown('ctrl')
    sleep(0.2)
    pag.moveTo(1141, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1239, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1326, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1432, 311)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1518, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    pag.rightClick()
    pag.moveTo(1568, 621)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1229, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyDown('ctrl')
    pag.moveTo(1334, 305)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1434, 305)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1522, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1624, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1714, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1817, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    pag.rightClick()
    sleep(0.2)
    pag.moveTo(1597, 608)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1214, 319)
    sleep(0.2)
    pag.click()
    pag.rightClick()
    sleep(0.2)
    pag.moveTo(1324, 614)
    pag.click()
    sleep(0.2)

    #Arrastar todas as colunas
    pag.moveTo(281, 308) #qtditmsai
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(234, 478)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(84, 521)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(953, 318) #slditm
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(902, 507)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(157, 540)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(756, 310) #fanfor
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(715, 458)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(277, 520)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(752, 321) #nomitm
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(713, 524)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(357, 548)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(559, 319) #numero
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(517, 525)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(450, 591)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(850, 322) #fancli
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(811, 470)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(559, 493)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(946, 319) #grucli
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(904, 450)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(636, 473)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')

    pag.moveTo(953, 318) #atraso
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(899, 465)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.keyDown('shift')
    sleep(0.2)
    pag.moveTo(716, 460)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.keyUp('shift')


    #Selecionando as colunas para colocar as bordas
    pag.moveTo(84, 312)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyDown('ctrl')
    pag.moveTo(177, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(277, 305)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(375, 308)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(467, 309)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(562, 304)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(659, 313)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(756, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(852, 302)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(941, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1050, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1143, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.keyUp('ctrl')
    sleep(0.2)

    #Colocar todas as bordas
    pag.moveTo(364, 168)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(451, 442)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    #Reajustar espaçamento das colunas
    pag.moveTo(18, 311)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(129, 311)
    sleep(0.2)
    pag.doubleClick()
    sleep(0.2)
    pag.moveTo(76, 339)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    #Classificar de A a Z
    pag.moveTo(1480, 318) #numero
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1615, 192)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1691, 220)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1046, 600)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    pag.moveTo(1091, 318) #nomitm
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1615, 192)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1691, 220)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1046, 600)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    pag.moveTo(480, 318) #fanfor
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1615, 192)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1691, 220)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1046, 600)
    sleep(0.2)
    pag.click()
    sleep(0.2)

    #Adicionando subtotal
    pag.moveTo(18, 310)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(661, 78)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1497, 189)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(860, 700)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1150, 329)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(830, 420)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(762, 560)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(1147, 532)
    sleep(0.2)
    pag.mouseDown()
    sleep(0.2)
    pag.moveTo(1151, 470)
    sleep(0.2)
    pag.mouseUp()
    sleep(0.2)
    pag.moveTo(765, 454)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(958, 714)
    sleep(0.2)
    pag.click()
    sleep(0.2)
    pag.moveTo(41, 18)
    sleep(0.2)
    pag.click()
    sleep(0.2)

#Interface

janela = Tk()
janela.title('AutoForm')
Label1 = Label(janela, text='Selecione um modelo de formatação:')
Label1.grid(column=0, row=0, padx=10, pady=10)
Botao1 = Button(janela, text='Pendências')
Botao1.bind("<Button>",  lambda e: programa())
Botao1.grid(column=0, row=1, padx=10, pady=10)



janela.mainloop()