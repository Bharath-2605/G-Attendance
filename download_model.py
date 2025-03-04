import insightface
from insightface.app import FaceAnalysis

# Initialize FaceAnalysis with the required model
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

print("Model downloaded and ready!")
