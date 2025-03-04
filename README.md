📌 G-Attendance
👋 Hey everyone! I'm Bollineni Bharath, and this project is designed to provide an automated face recognition-based attendance system using Python 🐍, OpenCV 🎥, and InsightFace.

🚀 Project Overview
G-Attendance is a face recognition-based attendance system that captures and records attendance using a webcam. This project helps in automating attendance marking with real-time face detection.
🔹 Features
✔️ Real-time face recognition using InsightFace 🤖
✔️ Automatic attendance marking in an Excel file 📂
✔️ Stores first and last recognition timestamps ⏳
✔️ Marks attendance as "Present" or "Absent" based on recognition duration ✅❌
✔️ Works with live webcam feed 📸

🛠️ Installation & Setup
📌 Prerequisites
Ensure you have Python 3.8+ installed along with the required dependencies.
📥 Clone the Repository
$ git clone https://github.com/Bharath-2605/G-Attendance.git
$ cd G-Attendance
📦 Install Dependencies
$ pip install -r requirements.txt

🔧 Usage
🎬 Running the Application
1️⃣ Train the model by running:
$ python train_model.py
2️⃣ Start the face recognition process:
$ python recognize.py
🎮 Controls
🟢 Press 'E' to exit and save attendance.
🔄 Press 'R' to restart recognition.

📊 Attendance Data
Attendance is stored in 49/static/Attendance.xlsx 📑
Updates include Date, First Recognition, Last Recognition, Duration, and Status (Present/Absent) 📌

🖥️ Tech Stack
🔹 Python 🐍
🔹 OpenCV 🎥
🔹 InsightFace 🤖
🔹 Pandas 📊
🔹 NumPy 🔢

💡 Future Enhancements
🚀 Improve accuracy with advanced models
📈 Implement a web-based UI for attendance tracking
📂 Store attendance records in a database instead of an Excel file

📜 License
This project is open-source and available under the MIT License.

🙌 Contributions
Feel free to fork this repo, raise issues, and submit pull requests to improve this project!
📧 Contact: Bharath-2605
🔗 GitHub Repository: G-Attendance
