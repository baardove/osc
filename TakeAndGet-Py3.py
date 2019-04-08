#!/usr/bin/env python

import requests
import shutil
import time
import sys

BASEURL = 'http://192.168.107.1/osc/'


resp = requests.get(BASEURL + 'info')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /osc/info/ {}'.format(resp.status_code))

print('Manufacturer: {}'.format(resp.json()["manufacturer"]))
print('Model: {}'.format(resp.json()["model"]))
print('Firmware: {}'.format(resp.json()["firmwareVersion"]))
print('Serial: {}'.format(resp.json()["serialNumber"]))


resp = requests.post(BASEURL + 'state')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /osc/state/ {}'.format(resp.status_code))

print('batteryLevel: {}'.format(resp.json()["state"]["batteryLevel"]*100))




data = {"name": "camera.startSession", "parameters": {} }

resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.startSession: {}'.format(resp.status_code))


sessionId = (resp.json()["results"]["sessionId"])
print ('SessionId: {}'.format(sessionId))



# TAKE A NEW IMAGE

print ('Say cheese!')

data = {"name": "camera.takePicture", "parameters": { "sessionId": sessionId} }
resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.takePicture: {}'.format(resp.status_code))
pictureId = (resp.json()["id"])

print ('Click!')

# WAIT FOR LAST IMAGE TO CHANGE

# IF YOU ARE USING PYTHON V.2
"""
sys.stdout.write('Waiting for image processing')
sys.stdout.flush()

for x in range(1, 30):
    sys.stdout.write('.')
    sys.stdout.flush()
    data = {"id": pictureId } 
    resp = requests.post(BASEURL + 'commands/status', json=data)
    if format(resp.json()["state"])=='done': 
        break
    time.sleep(0.5)

print ('')
uri = resp.json()["results"]["fileUri"]
#print ('uri: {}'.format(uri))
"""

sys.stdout.write('Waiting for image processing')
sys.stdout.flush()

for x in xrange(1, 30):
    sys.stdout.write('.')
    sys.stdout.flush()
    data = {"id": pictureId } 
    resp = requests.post(BASEURL + 'commands/status', json=data)
    if format(resp.json()["state"])=='done': 
        break
    time.sleep(0.5)

print ('')
uri = resp.json()["results"]["fileUri"]
#print ('uri: {}'.format(uri))



# GET NEW IMAGE

name="OSC_" + pictureId+".JPG"

data = {"name": "camera.getImage", "parameters": { "fileUri": uri} }

resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.getImage: {}'.format(resp))


# SAVE NEW IMAGE

# IF YOU ARE USING PYTHON V.2
"""
resp.raw.decode_content = True

with open(name,'w') as ofh:
	for chunk in resp:
            ofh.write(chunk)
        
print ('Image stored as: {}'.format(name))
"""

resp.raw.decode_content = True

with open(name,'wb') as ofh:
	for chunk in resp:
            ofh.write(chunk)
        
print ('Image stored as: {}'.format(name))



