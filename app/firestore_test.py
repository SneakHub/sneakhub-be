import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate(r"D:\BK\hk232\project\sneakhub-be\keyFolder\sneakhub-dev-firebase-adminsdk-j0eft-486b461e31.json")

app = firebase_admin.initialize_app(cred)

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