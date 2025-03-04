import os
import cv2
import numpy as np
import pickle
from insightface.app import FaceAnalysis

# Initialize InsightFace model
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)

# Path to dataset
dataset_path = "dataset"
embedding_file = "face_embeddings.pkl"

# Dictionary to store embeddings
face_embeddings = {}

# Loop through each person's folder in dataset
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue  # Skip if not a folder

    embeddings_list = []

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        # Read and process the image
        img = cv2.imread(image_path)
        if img is None:
            print(f"Skipping {image_path}, unable to load image.")
            continue

        faces = app.get(img)
        if len(faces) == 0:
            print(f"No face detected in {image_path}, skipping.")
            continue

        # Extract and normalize embedding
        embedding = faces[0].normed_embedding
        embeddings_list.append(embedding)

    # Average embeddings to get a single vector per person
    if len(embeddings_list) > 0:
        avg_embedding = np.mean(embeddings_list, axis=0)
        face_embeddings[person_name] = avg_embedding
        print(f"✅ Stored embeddings for {person_name}")

# Save embeddings to a file
with open(embedding_file, "wb") as f:
    pickle.dump(face_embeddings, f)

print("\n🎉 Training complete! Embeddings saved to", embedding_file)
