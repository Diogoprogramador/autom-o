# Envio de relatório por e-mail (automatizado com Python)

from pyautogui import *
from pymsgbox import alert
from pyperclip import copy
from pandas import read_excel
from time import sleep


alert(f'{"A automação vai começar!".center(70)} \nAperte "Ok" e não mexa em nada até o fim do processo')
sleep(3)
press('WIN')
sleep(5)
write('chrome')
sleep(5)
press('enter')
sleep(15)
click(x=290, y=51)
sleep(3)
copy(r'https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing')
hotkey('ctrl', 'v')
sleep(2)
press('enter')
sleep(8)
click(x=296, y=298, clicks=2)
sleep(8)
rightClick(x=1116, y=343)
sleep(8)
click(x=820, y=636)
sleep(30)
hotkey('ctrl', 'w')


vendas = read_excel(r'/home/idinaldo/Downloads/Vendas - Dez.xlsx')
faturamento = f'R${sum(vendas["Valor Final"]):,}'
faturamento = faturamento.replace(',', '.')
qtde_produtos = f'{sum(vendas["Quantidade"]):,}'
qtde_produtos = qtde_produtos.replace(',', '.')

sleep(8)
press('WIN')
sleep(5)
write('chrome')
sleep(5)
click(x=399, y=259)
sleep(15)
click(x=290, y=51)
sleep(5)
copy(r'https://mail.google.com/mail/u/0/#inbox')
hotkey('ctrl', 'v')
sleep(5)
press('enter')
sleep(5)
click(x=106, y=206)
sleep(8)
click(x=846, y=311)
sleep(5)
copy(r'testandoasminhasautomacoes@gmail.com')
hotkey('ctrl', 'v')
sleep(8)
click(x=837, y=366)
sleep(5)
copy(r'Relatório de vendas')
hotkey('ctrl', 'v')
sleep(5)
click(x=831, y=387)
copy('Prezados, bom dia \n'
     f'O faturamento de ontem foi de: {faturamento} \n'
     f'A quantidade de produtos vendidos foi de: {qtde_produtos} \n'
     f'\n'
     f'Abraços\n'
     f'Idinaldo, do GitHub')
hotkey('ctrl', 'v')
sleep(3)
hotkey('ctrl', 'enter')
sleep(3)
hotkey('ctrl', 'w')

# código feito por Idinaldo