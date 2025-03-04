import cv2
import numpy as np
import pickle
import os
import pandas as pd
from datetime import datetime
from insightface.app import FaceAnalysis

# Load face recognition model
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)

# Load trained embeddings
embedding_file = "face_embeddings.pkl"
if not os.path.exists(embedding_file):
    print("Error: Trained face embeddings not found. Train the model first!")
    exit()

with open(embedding_file, "rb") as f:
    known_faces = pickle.load(f)

# Excel file path
excel_path = "/Users/bharathbollineni/Desktop/49/static/Attendance.xlsx"


# Load existing attendance data
if os.path.exists(excel_path):
    df = pd.read_excel(excel_path)
else:
    print("Error: Attendance.xlsx file not found!")
    exit()

# Ensure correct column names
expected_columns = ["Registration No.", "Name", "Date", "First Recognition", "Last Recognition", "Duration", "Status"]
if list(df.columns) != expected_columns:
    print("Error: Column names in Attendance.xlsx do not match expected format!")
    print("Found columns:", df.columns)
    exit()

# Convert Name column to lowercase for case-insensitive matching
df["Name"] = df["Name"].str.strip().str.lower()

# Tracking first and last recognition per session
first_recognition = {}
last_recognition = {}

# Open webcam
cap = cv2.VideoCapture(0)

print("Press 'E' to stop recognition and save attendance.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)
    current_time = datetime.now()
    sys_date = current_time.strftime("%Y-%m-%d")  # System date

    for face in faces:
        bbox = face.bbox.astype(int)
        embedding = face.normed_embedding

        # Find best match
        best_match = None
        min_distance = float("inf")

        for stored_name, stored_embedding in known_faces.items():
            distance = np.linalg.norm(embedding - stored_embedding)
            if distance < min_distance:
                min_distance = distance
                best_match = stored_name.strip().lower()  # Convert to lowercase

        # Recognition threshold
        if min_distance < 1.2:
            label = best_match
            color = (0, 255, 0)  # Green for recognized face
        else:
            label = "Unknown"
            color = (0, 0, 255)  # Red for unknown face

        # Draw bounding box and label
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
        cv2.putText(frame, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        if label != "Unknown":
            key = label  # Only use name for lookup

            # Record first recognition
            if key not in first_recognition:
                first_recognition[key] = current_time

            # Update last recognition
            last_recognition[key] = current_time

    # Show webcam feed
    cv2.imshow("Face Recognition", frame)

    # Press 'E' to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("e"):
        print("E pressed. Stopping recognition...")
        break

cap.release()
cv2.destroyAllWindows()

# Final attendance marking (Update existing names)
recognized_names = set(first_recognition.keys())  # Names that were detected

for name, first_time in first_recognition.items():
    last_time = last_recognition.get(name, first_time)
    total_time = (last_time - first_time).total_seconds() / 60  # Convert to minutes

    # Case-insensitive matching for names
    mask = df["Name"].str.lower() == name.lower()

    if mask.any():
        df.loc[mask, "Date"] = sys_date
        df.loc[mask, "First Recognition"] = first_time.strftime("%H:%M:%S")
        df.loc[mask, "Last Recognition"] = last_time.strftime("%H:%M:%S")
        df.loc[mask, "Duration"] = round(total_time, 2)

        # Mark status based on time spent
        if total_time >= 35:
            df.loc[mask, "Status"] = "Present"
        else:
            df.loc[mask, "Status"] = "Absent"

        print(f"✅ Attendance updated for {name}")

# **Mark students who were NOT recognized as Absent**
for i, row in df.iterrows():
    student_name = row["Name"].strip().lower()
    if student_name not in recognized_names:
        df.loc[i, "Date"] = sys_date
        df.loc[i, "First Recognition"] = "N/A"
        df.loc[i, "Last Recognition"] = "N/A"
        df.loc[i, "Duration"] = 0
        df.loc[i, "Status"] = "Absent"
        print(f"❌ Marked {row['Name']} as Absent (Not recognized)")

# Save the updated attendance
df.to_excel(excel_path, index=False)
print("📁 Attendance sheet updated successfully!")
