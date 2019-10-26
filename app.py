#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from camera_pi import Camera
from dht import readDHTSensor
from gas import readGasSensor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def videogen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(videogen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/dht')
def dht():
    return Response(readDHTSensor(), mimetype='text/xml')


@app.route('/gas')
def gas():
    return Response(readGasSensor(), mimetype='text/xml')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
