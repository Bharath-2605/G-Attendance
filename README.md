📌 G-Attendance


👋 Hey Guys!

I am Bollineni Bharath. This project is mainly built using Python and OpenCV for Face Recognition-based Attendance System.



🚀 Project Overview

G-Attendance is an automated face recognition attendance system that uses computer vision to detect and mark attendance in an Excel sheet. It ensures accurate and efficient tracking of student or employee attendance.



🛠️ Features

📸 Live Face Recognition using OpenCV and InsightFace

📂 Stores Attendance Data in an Excel file

🔍 Automatically Marks Present/Absent based on recognition duration

✅ Easy to Use with a simple interface

🖥️ Real-Time Detection via webcam



📦 Installation

Clone the Repository

git clone https://github.com/Bharath-2605/G-Attendance.git

Navigate to the Project Directory

cd G-Attendance

Install Required Dependencies

pip install -r requirements.txt



🔧 How to Use

Train the Model (if not trained already):
python train_model.py

Run Face Recognition for Attendance:
python recognize.py

Press 'E' to stop recognition and save attendance.



📂 File Structure

train_model.py → Train the model and store face embeddings.

recognize.py → Runs real-time face recognition.

face_embeddings.pkl → Stores the trained face embeddings.

49/static/Attendance.xlsx → Stores the attendance records.

requirements.txt → Dependencies required to run the project.



⚠️ Troubleshooting

Error: Attendance.xlsx file not found!

Ensure that 49/static/Attendance.xlsx exists before running recognize.py.

Error: Face embeddings not found!

Run train_model.py before recognize.py.



📝 To-Do List

✅ Improve face recognition accuracy

🚀 Optimize the system for large datasets

🎨 Add a GUI for better usability



🏆 Contribution

Feel free to contribute to this project by raising issues or submitting pull requests! 😊



📜 License

This project is licensed under the MIT License.



📩 Contact

For any queries, reach out to me on GitHub.
