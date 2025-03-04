from flask import Flask, send_from_directory, render_template, jsonify
import os
import subprocess
import signal

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

recognition_process = None  # Global process variable


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/train')
def train_model():
    script_path = os.path.join(SCRIPTS_DIR, "train_model.py")
    
    if not os.path.exists(script_path):
        return jsonify({"error": "train_model.py not found!"}), 500

    try:
        process = subprocess.run(["python3", script_path], check=True, text=True, capture_output=True)
        return jsonify({"message": "Training completed.", "output": process.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Training failed", "output": e.stderr}), 500


@app.route('/test')
def test_system():
    script_path = os.path.join(SCRIPTS_DIR, "test_face.py")
    
    if not os.path.exists(script_path):
        return jsonify({"error": "test_model.py not found!"}), 500

    try:
        process = subprocess.run(["python3", script_path], check=True, text=True, capture_output=True)
        return jsonify({"message": "Testing completed.", "output": process.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Testing failed", "output": e.stderr}), 500


@app.route('/recognize')
def start_recognition():
    global recognition_process
    script_path = os.path.join(SCRIPTS_DIR, "recognize.py")

    if not os.path.exists(script_path):
        return jsonify({"error": "recognize.py not found!"}), 500

    if recognition_process is None:
        recognition_process = subprocess.Popen(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify({"message": "Face recognition started."})
    else:
        return jsonify({"message": "Recognition is already running."})


@app.route('/stop-recognition')
def stop_recognition():
    global recognition_process

    if recognition_process is not None:
        recognition_process.terminate()
        recognition_process.communicate()
        recognition_process = None
        return jsonify({"message": "Face recognition stopped."})
    else:
        return jsonify({"message": "No recognition process running."})


@app.route('/view-attendance')
def view_attendance():
    file_name = "Attendance.xlsx"
    file_path = os.path.join(STATIC_DIR, file_name)

    if os.path.exists(file_path):
        return send_from_directory(STATIC_DIR, file_name, as_attachment=True)
    else:
        return jsonify({"error": "Attendance file not found"}), 404


if __name__ == '__main__':
    print("[INFO] Flask server running at http://127.0.0.1:5001")
    app.run(debug=True, port=5001)
