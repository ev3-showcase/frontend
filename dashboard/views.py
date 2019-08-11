import os
import uuid
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from distutils.util import strtobool
import requests
from .forms import CarControlForm

API_SERVER = os.getenv('API_SERVER', 'echo-api-fk-sc.aotp012.mcs-paas.io')
API_PORT = os.getenv('API_PORT', '80')
api = f'http://{API_SERVER}:{API_PORT}'



def dashboard(request):
    if request.method == 'POST':
        form = CarControlForm(request.POST)
        if form.is_valid():

            speed = form.cleaned_data.get('speed')
            angle = form.cleaned_data.get('angle')

            message = {
                    'speed': 0,
                    'steering': 0,
                    }
            
            message['speed'] = speed
            message['steering'] = angle

            #publish messages
            url = f'{api}/api/v1/publish/message'
            payload = message
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            messages.success(request, f'Instructions Transmitted. Speed: {speed}%, Steeringangle: {angle}%')
            messages.info(request, f'Message Posted to {url}')
            messages.info(request, f'Request Response: {r}')
    
    else: 
        form = CarControlForm()
    return render(request, 'dashboard/dashboard.html', {'form': form})
