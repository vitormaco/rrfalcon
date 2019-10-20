#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
from dht import readDHTSensor
from gas import readGasSensor

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def videogen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(videogen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/dht')
def dht():
    """Humidity and Temperature sensor."""
    return Response(readDHTSensor(), mimetype='text/xml')

@app.route('/gas')
def dht():
    """Humidity and Temperature sensor."""
    return Response(readGasSensor(), mimetype='text/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
