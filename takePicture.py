#!/usr/bin/env python

import requests
import shutil


BASEURL = 'http://192.168.107.1/osc/'


data = {"name": "camera.startSession", "parameters": {} }

resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.startSession: {}'.format(resp.status_code))


sessionId = (resp.json()["results"]["sessionId"])


data = {"name": "camera.takePicture", "parameters": { "sessionId": sessionId} }


resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.takePicture: {}'.format(resp.status_code))


