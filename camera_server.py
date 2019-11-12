
from flask import Flask, render_template, Response, request
from flask_cors import CORS
from camera_pi import Camera


app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=3001)

def videogen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(videogen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')