import firebase_admin
from firebase_admin import credentials, firestore
from config import get_settings
from base64_decode import base64_decode
import json

# Load the Firebase Admin SDK credentials from the environment variable
settings = get_settings()
# print(settings.google_application_credentials, end="\n")

# Decode the google_application_credientals
# because firebase_admin.initialize_app() take argument typed DICT
# after decoding the credentials variable (string type) -> json.loads() it
google_application_credientals = json.loads(base64_decode(settings.google_application_credentials))
# print(google_application_credientals)
# print(type(google_application_credientals))

# google_application_credientals = json.loads(google_application_credientals)
# print(google_application_credientals)
# print(type(google_application_credientals))

# Initialize the Firebase Admin SDK
firebase_admin_cred = credentials.Certificate(google_application_credientals)
firebase_app = firebase_admin.initialize_app(firebase_admin_cred)

db = firestore.client()

# add data
doc_ref = db.collection("users").document("user No1")
doc_ref.set({"first": "Khang", "last": "Chau", "birthday": "2001"})

doc_ref = db.collection("users").document("user No2")
doc_ref.set({"first": "Trang", "last": "Chau", "birthday": "1991"})


# read data
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id}: {doc.to_dict()}")


