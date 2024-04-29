import firebase_admin
from firebase_admin import credentials
from config import get_settings
from base64_decode import base64_decode
import json
import base64

# Load the Firebase Admin SDK credentials from the environment variable
settings = get_settings()

print(settings.google_application_credentials, end="\n")

# Decode the google_application_credientals
google_application_credientals = json.loads(base64_decode(settings.google_application_credentials))
print(google_application_credientals)
print(type(google_application_credientals))

# google_application_credientals = json.loads(google_application_crediental s)
# print(google_application_credientals)
# print(type(google_application_credientals))

# Initialize the Firebase Admin SDK
firebase_admin_cred = credentials.Certificate(google_application_credientals)
firebase_app = firebase_admin.initialize_app(firebase_admin_cred)


