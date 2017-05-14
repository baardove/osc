# osc
Open Spherical Camera API level 1 - simple python script to take and grab an image from a spherical camera (Samsung Gear 360 2016)

By Bard Ove Myhr (baardove)
https://www.facebook.com/baardove
bard.myhr@gmail.com


A simple python script to take an 360-degree image and retrieve it and store it.


Prerequesites:

  * A 360 spherical camera supporting Open Spherical Camera API level 1 (tex. Samsung Gear 360)
  * Set camera in peer modus for Street view 
  * Connect to cameras wifi 
  * Run script takeAndGet.py
  
  If everything runs well the image should be taken and stored to you current directory.
  
  
Trouble shooting:
 
 My Samsung Gear gives an ip address in the range 192.168.107.X, and the cameras address is 192.168.107.1.
 Different firmware and different cameras might use different range and address. This address needs to be updated in the script.  The Api says you should use the gateway given by cameras DHCP-server as ip address.
 
 
 Scripts:
 
 takeAndGet.py - the main script that does it all. Takes a picture, waits for it to be ready, retrieves it and store it.
 takeAndGet2.py - a previous version that uses different approac to detect when the file is finished processing.
 takePicture.py - takes a pictures, but does not wait for it to be processed.
 getPicture.py - retrieves the latest processed image and stores it.
 
 
 
