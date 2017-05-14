#!/usr/bin/env python

import requests
import shutil


BASEURL = 'http://192.168.107.1/osc/'


data = {"name": "camera.listImages", "parameters": { "entryCount": 1} }

resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.listImages: {}'.format(resp.status_code))

name = (resp.json()["results"]["entries"][0]["name"])
uri = (resp.json()["results"]["entries"][0]["uri"])




data = {"name": "camera.getImage", "parameters": { "fileUri": uri} }

resp = requests.post(BASEURL + 'commands/execute', json=data)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('camera.getImage: {}'.format(resp))

resp.raw.decode_content = True

with open(name,'w') as ofh:
	for chunk in resp:
            ofh.write(chunk)
        
print ('Image: {}'.format(name))
