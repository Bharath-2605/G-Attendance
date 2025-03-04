📌 Face Recognition Attendance System

📝 Overview

This is an AI-powered Face Recognition Attendance System that uses InsightFace for detecting and recognizing faces in real-time. It automatically logs attendance in an Excel sheet (Attendance.xlsx) based on facial recognition.

⚡ Features

✅ Real-time Face Detection & Recognition using InsightFace 🏆✅ Face Embeddings Storage for matching known faces 🔐✅ Automatic Attendance Marking based on recognition duration 🕒✅ Excel Integration for attendance tracking 📊✅ Works with a Webcam 🎥

🏗️ How It Works

1️⃣ Train the Model: Generate face embeddings and store them in face_embeddings.pkl 🧠2️⃣ Run Face Recognition: Capture video, detect faces, and compare with stored embeddings 🖼️3️⃣ Attendance Logging: Update 49/static/Attendance.xlsx based on recognition time 📝4️⃣ Determine Status: Present if detected for ≥35 minutes, otherwise Absent ❌✅


🚀 Installation & Setup

1️⃣ Install Dependencies

pip install opencv-python numpy pandas insightface onnxruntime albumentations openpyxl

2️⃣ Train the Model (Register Faces)

Run the following script to generate face embeddings for known individuals:

python scripts/train_model.py

This will create face_embeddings.pkl file, which stores facial features.

3️⃣ Start Face Recognition

Ensure your webcam is connected, then run:

python scripts/recognize.py

Press 'E' to stop recognition and save attendance.

🛠️ Troubleshooting

❌ Error: `` not found!🔹 Run train_model.py to generate embeddings.

❌ Error: `` not found!🔹 Ensure 49/static/Attendance.xlsx exists. If not, create an empty Excel sheet with columns:

Registration No.

Name

Date

First Recognition

Last Recognition

Duration

Status

❌ Recognition is not accurate🔹 Try lowering the threshold (min_distance < 1.2) in recognize.py.

🎯 Future Enhancements

✨ Add support for multiple cameras 🎥✨ Improve recognition accuracy with better embeddings storage 📈✨ Build a web interface for easy attendance monitoring 🌍

📞 Contact

💡 Need help or want to contribute? Reach out via GitHub! 😊
