import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account.
cred = credentials.Certificate(
    "./keyFolder/sneakhub-dev-firebase-adminsdk-j0eft-486b461e31.json"
)

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# # add data
# doc_ref = db.collection("users").document("user No1")
# doc_ref.set({"first": "Khang", "last": "Chau", "birthday": "2001"})
#
# doc_ref = db.collection("users").document("user No2")
# doc_ref.set({"first": "Trang", "last": "Chau", "birthday": "1991"})
#
#
# # read data
# users_ref = db.collection("users")
# docs = users_ref.stream()
#
# for doc in docs:
#     print(f"{doc.id}: {doc.to_dict()}")
#
# # delete data
# db.collection("users").document("alovelace").delete()

doc_ref = db.collection("todos").document("3a1a1142-c47c-41b7-b782-c6b8f82a186c")

print(doc_ref.get().to_dict())
