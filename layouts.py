from PySimpleGUI import PySimpleGUI as sg
import variables

def window_astroend():
    sg.theme('DarkBlack1')
    layout_column = [
        [sg.Text('ALBERT BOT', size=(20,1), font='ANY 20', justification='center')],
        [sg.Text('por ASTROEND', size=(20,1), font='ANY 8', justification='right')],
        [sg.Text('')],
        [sg.Button('Términos') ,sg.Button('Aceptar los términos', button_color=('white', 'green'))]
    ]   
    layout = [[sg.Column(layout_column, element_justification='right')]]
    return sg.Window('Astroend', layout=layout, finalize=True, size=(275,160),margins=(20,15,20,20))

def window_login():
    sg.theme('DarkBlack1')
    layout_column = [
        [sg.Text('Correo: ', size=(5,1), font='ANY 11'), sg.Input(key='login', size=(20,2))],
        [sg.Text('Contraseña: ', size=(5,1), font='ANY 11'), sg.Input(key='password', size=(20,2), password_char='*')],
        [sg.Text('')],
        [sg.Button('Entrar', button_color=('white', 'green'), size=(10,2))]
    ]   
    layout = [[sg.Column(layout_column, element_justification='right')]]
    return sg.Window('Login', layout=layout, finalize=True, size=(275,150),margins=(20,15,20,20))

def window_loading():
    sg.theme('DarkBlack1')
    layout = [  
        [sg.Text('Cargando....', font='ANY 15')],
        [sg.Image(data=variables.gif, key='_IMAGE_')],
    ]
    return sg.Window('Loading', layout=layout, size=(225,130),margins=(20,15,20,20))

def pop_up():
    sg.popup('Erro de conexão/Senha ou Login incorretos')

def window_option():
    sg.theme('DarkBlack1')
    layout_column = [
        [sg.Text('Elegir cuenta: ', size=(40,1), justification='center', font='ANY 12')],
        [sg.Radio('Entrenamiento', group_id='account', key='account_practice'), 
            sg.Radio('Real', group_id='account', key='account_real')],
        [sg.Text('Elija el tipo de opción: ', size=(40,1), justification='center', font='ANY 12')],
        [sg.Radio('Binario', group_id='option', key='option_binary'), 
            sg.Radio('Digital', group_id='option', key='option_digital')],
        [sg.Text('Elige mayoría o minoría: ', size=(40,1), justification='center', font='ANY 12')],
        [sg.Radio('Mayoría', group_id='favourable', key='favourable_majority'), 
            sg.Radio('Minoría', group_id='favourable', key='favourable_minority')],
        [sg.Text('Valor inicial:', size=(18,1), font='ANY 11'), sg.Spin([i for i in range(1,1000)], initial_value = 2,key='value', size=(12,1))],
        [sg.Text('Detener Ganar: ', size=(18,1), font='ANY 11'), sg.Spin([i for i in range(1,1000)], initial_value = 10,key='stop_win', size=(12,1))],
        [sg.Text('Detener la pérdida: ', size=(18,1), font='ANY 11'), sg.Spin([i for i in range(1,1000)], initial_value = 20,key='stop_loss', size=(12,1))],
        [sg.Text('Martingala: ', size=(18,1), font='ANY 11'), sg.Spin([i for i in range(0,10)], key='martingale', size=(12,1))],
        [sg.Text('Ingrese un PAR abierto: ', font='ANY 11')], 
        [sg.Input(key='exchange', size=(30,2), font='ANY 11', justification='center')],
        [sg.Text('')],
        [sg.Button('Funcionar', button_color=('white', 'green'), size=(10,2))]
    ]
    layout = [[sg.Column(layout_column, element_justification='center')]]
    return sg.Window('Opción', layout=layout, finalize=True, size=(350,425))

def window_trading(type,balance,value, exchange, martingale, option, favourable, stop_win, stop_loss):
    status = '#00994D' if type == 'PRACTICE' else 'yellow'
    color = '#00994D' if balance == stop_win else '#D93F07' if balance == stop_loss else status if balance > 0 else 'white'
    sg.theme('DarkBlack1')
    layout_column = [  
        [sg.Text(('Cuenta: Real' if type == 'REAL' else 'Conta: Treino'), font='ANY 15', text_color= status, justification='right', size = (40,1))],
        [sg.Text('')],
        [sg.Text('Bancario: '+ str(balance), font='ANY 15', text_color='#64929E', justification='right', key = '-balance-')],
        [sg.Text('Entrada: '+ str(value) + ' (' + 
            str('Mayoría)' if favourable == 'MAJORITY' else 'Minoria)'), font='ANY 15', justification='left')],
        [sg.Text('PAR: '+ str(exchange) +'/'+ str(option), font='ANY 15', justification='left')],
        [sg.Text('Martingala: '+ str(martingale), font='ANY 15', justification='left')],
        [sg.Text('Stop Win: '+ str(stop_win), font='ANY 15', text_color='#00994D', justification='left', key = '-stop_win-')],
        [sg.Text('Stop Loss: '+ str(stop_loss), font='ANY 15', text_color='#D93F07', justification='left',key = '-stop_loss-')],
        [sg.Text('')],
        [sg.Text('Cargando ...', font='ANY 15', text_color=color, key = '-status-')],
        [sg.Text('')],
        [sg.Button('Finalizar', button_color=('white', 'green'), size=(10,2))]
    ]
    layout = [[sg.Column(layout_column, element_justification='center')]]
    return sg.Window('Trading', layout=layout, finalize=True, size=(350,410),margins=(20,15,20,20))

def window_finalize(balance):
    sg.theme('DarkBlack1')
    layout_column = [  
        [sg.Text(('Banca Final: ' + str(balance)), font='ANY 15', text_color='#64929E')],
        [sg.Text(('O relatorio final esta salvo na pasta:'), font='ANY 15')],
        [sg.Text(('/%appdata%/.astroend/registers'), font='ANY 15')],
        [sg.Button('Cerrar', button_color=('white', 'green'))]
    ]
    layout = [[sg.Column(layout_column, element_justification='center')]]
    return sg.Window('Trading', layout=layout, finalize=True, size=(375,175),margins=(20,15,20,20))
