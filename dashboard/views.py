import os
import uuid
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from distutils.util import strtobool
import paho.mqtt.client as mqtt
from .forms import CarControlForm

broker = os.getenv('MQTT_BROKER', 'ts.rdy.one')
port =  int(os.getenv('MQTT_PORT', 11883))
pub_name = os.getenv('HOSTNAME', ('publisher-' + uuid.uuid4().hex.upper()[0:6]))
websocket = strtobool(os.getenv('MQTT_SOCKET', 'False'))
wait_timer = int(os.getenv('MQTT_WAITTIME', 1))

def dashboard(request):
    if request.method == 'POST':
        form = CarControlForm(request.POST)
        if form.is_valid():

            broker = os.getenv('MQTT_BROKER', 'ts.rdy.one')
            port =  int(os.getenv('MQTT_PORT', 11883))
            pub_name = os.getenv('HOSTNAME', ('publisher-' + uuid.uuid4().hex.upper()[0:6]))
            websocket = strtobool(os.getenv('MQTT_SOCKET', 'False'))
            wait_timer = int(os.getenv('MQTT_WAITTIME', 1))

            if websocket:
                messages.info(request, f'Connecting to {broker}:{port} as {pub_name} via websocket')
                client = mqtt.Client(pub_name,transport='websockets')
            else:
                messages.info(request, f'Connecting to {broker}:{port} as {pub_name}')
                client = mqtt.Client(pub_name)

            client.connect(broker, port, 60)
            client.loop_start()

            speed = form.cleaned_data.get('speed')
            angle = form.cleaned_data.get('angle')

            message = {
                    'counter': 0,
                    'speed': 0,
                    'steering': 0,
                    'hostname': pub_name,
                    }
            
            message['speed'] = speed
            message['steering'] = angle
            client.publish('test/host', json.dumps(message))
            messages.success(request, f'Instructions Transmitted. Speed: {speed}%, Steeringangle: {angle}%')
            client.disconnect()
            messages.info(request, f'Disconnected from Server.')
            return redirect('dashboard')
    else: 
        form = CarControlForm()
    return render(request, 'dashboard/dashboard.html', {'form': form})
