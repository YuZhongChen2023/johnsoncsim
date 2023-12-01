import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection("人選之人─造浪者")
#docs = collection_ref.where(filter=FieldFilter("name","==", "王淨")).get()
docs = collection_ref.where(filter=FieldFilter("birth",">=", 1980)).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
