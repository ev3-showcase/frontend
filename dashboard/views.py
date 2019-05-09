import os
import uuid
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from distutils.util import strtobool
import requests
from .forms import CarControlForm

api = os.getenv('API_SERVER', 'http://localhost:5000')

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


            return redirect('dashboard')
    else: 
        form = CarControlForm()
    return render(request, 'dashboard/dashboard.html', {'form': form})
