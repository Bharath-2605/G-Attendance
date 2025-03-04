Face Recognition Attendance System 📸🎓
👋 Hey guys..!
I am Bollineni Bharath

This project is built using Python 🐍, OpenCV 🎥, and InsightFace for face recognition-based attendance marking.

📌 Features
✔ Live Face Recognition using InsightFace AI.
✔ Automatic Attendance Marking in an Excel sheet.
✔ First & Last Recognition Time Tracking ⏳.
✔ Time-based Presence Status (Present/Absent) 🏫.
✔ Excel-based Record Keeping 📊.

📂 Folder Structure
php
Copy
Edit
📁 FaceRecognition-Attendance  
 ┣ 📂 static  
 ┃ ┗ 📄 Attendance.xlsx   # Attendance records  
 ┣ 📂 scripts  
 ┃ ┣ 📄 train_model.py    # Training the face recognition model  
 ┃ ┗ 📄 recognize.py      # Live recognition & attendance marking  
 ┣ 📄 requirements.txt    # Required dependencies  
 ┗ 📄 README.md           # Project documentation  
⚙️ Setup & Installation
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/Bharath-2605/FaceRecognition-Attendance.git
cd FaceRecognition-Attendance
Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Train the Model 🏋️
Run the following command to train the model and generate face embeddings:

bash
Copy
Edit
python scripts/train_model.py
Step 4: Run Face Recognition 🎥
bash
Copy
Edit
python scripts/recognize.py
📝 How It Works?
✅ Open the webcam and detect faces in real-time.
✅ Compare detected faces with trained embeddings.
✅ If matched, mark attendance in static/Attendance.xlsx 📄.
✅ Track First & Last Recognition Time ⏳.
✅ Present if duration ≥ 35 minutes, else Absent.

🎮 Controls
🔄 Press "R" - Restart recognition session.
❌ Press "E" - Exit recognition & save attendance.

🐞 Troubleshooting
🔹 Error: Attendance.xlsx file not found!
📌 Ensure static/Attendance.xlsx exists before running recognize.py.

🔹 Error: Trained face embeddings not found!
📌 Run train_model.py first to generate face_embeddings.pkl.

🔹 Webcam Not Opening?
📌 Check if another application is using the camera.

📢 Contributing
Contributions are welcome! 🤝

Fork the repo.
Create a new branch (git checkout -b feature-branch).
Commit changes (git commit -m "Add new feature").
Push (git push origin feature-branch).
Create a Pull Request.
📜 License
📝 This project is licensed under the MIT License.

Happy Coding! 🚀
