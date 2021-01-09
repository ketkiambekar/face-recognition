import face_recognition
import os 
import cv2

KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR ="Unknown_faces"
TOLERANCE =0.6
FRAME_THICKNESS = 3
FONT_THICKNESS= 2
MODEL ="cnn"

print("Loading Known Faces....")

known_faces=[]
known_names=[]

for name in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
    image = face_recognition.face_encodings(image)
