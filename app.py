#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request
from flask_cors import CORS
from camera_pi import Camera
from dht import readDHTSensor
from gas import readGasSensor
from wheels_dcmotor import moveDCMotor
from wheels_servo import turnDirectionServo

import atexit
import RPi.GPIO
atexit.register(RPi.GPIO.cleanup)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return Response('Health Check', mimetype='text/xml')


@app.route('/move', methods=['POST'])
def move():
    req_data = request.get_json()
    speed = req_data['speed']
    moveDCMotor(speed)
    return Response('sucess', mimetype='text/xml')


@app.route('/turn', methods=['POST'])
def turn():
    req_data = request.get_json()
    degrees = req_data['degrees']
    turnDirectionServo(degrees)
    return Response('sucess', mimetype='text/xml')


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
