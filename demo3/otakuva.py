# Otetaan kayttoon kamera- ja aika-kirjastot
import picamera
import time

# Maaritetaan kamera
camera = picamera.PiCamera()

camera.capture('/var/www/html/latest.jpg')
