# from classes.main import Main
from datetime import timedelta
from django.shortcuts import render, redirect
from classes.account import Account
from classes.main import Main
from iqoptionapi.stable_api import IQ_Option
import secrets
from multiprocessing import Process, Manager
from django.shortcuts import render, redirect
from classes.operate import Operate

account = Main()

def menu(request):
    my_token = request.session.get('token')
    if not my_token:
        print('Error: No se ha iniciado sesión')
        return redirect('login')
    else:
        
        request.session.set_expiry(timedelta(minutes=5))
        balancePrueba = account.get_balance
        balanceReal = account.get_real_balance
        email = account.get_email
        nombre = account.get_name

        if request.method == 'POST':
            account.type('PRACTICE' if request.POST.get('account') == 'practice' else 'REAL')
            account.option('BINARY' if request.POST.get('option') == 'binary' else 'DIGITAL')
            account.favourable('MAJORITY' if request.POST.get('favourable') == 'majority' else 'MINORITY')
            account.value(float(request.POST.get('value').replace(',','.')))
            account.stop_win(float(request.POST.get('stop_win').replace(',','.')))
            account.stop_loss(float(request.POST.get('stop_loss').replace(',','.')))
            account.martingale(int(request.POST.get('martingale')))
            account.exchange(request.POST.get('exchange').upper())

            # Iniciar proceso de trading
            manager = Manager()
            return_dict = manager.dict()
            trading_ = Process(target=Operate, args=(account.get_email, account.get_password, 
                                account.get_stop_win_complete, account.get_stop_loss_complete, 
                                account.get_exchange, account.get_option, account.get_favourable, 
                                account.get_martingale, account.get_value, account.get_type, 
                                return_dict, 'trading_'))
            trading_.start()

            # Agregar proceso de trading a la lista de trabajos activos
            jobs = request.session.get('jobs', [])
            jobs.append(trading_)
            request.session['jobs'] = jobs

            # Actualizar estado de operación
            request.session['operating_state'] = True

            # Redireccionar a página de trading
            return redirect('trading')
        else:
            context = {'balance': balancePrueba, 'balanceReal': balanceReal, 'email': email, 'nombre': nombre}

            return render(request, 'menu/menu.html', context)




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Conectarse a IQ Option
        account.connect(email, password)
        
        # Verificar si la conexión fue exitosa y guardar el token en la sesión
        if account.check_connect():
            # Crear un token aleatorio utilizando la biblioteca secrets
            token = secrets.token_hex(16)
            # Guardar el token en la sesión
            request.session['token'] = token
            
            # Conectar a la API de IQ Option
            account.API = IQ_Option(email, password)
            account.API.connect()
            
            print('Sesión iniciada con éxito')
            return redirect('menu')
        else:
            context = {'error': 'Nombre de usuario o contraseña incorrectos'}
            return render(request, 'registrar/login.html', context)
    else:
        return render(request, 'registrar/login.html')


def logout(request):
    request.session.pop('token', None)
    return redirect('login')


def terminos(request):
    return render(request, 'terminos.html')