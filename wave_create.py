import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "name": "謝盈萱",
  "role": "公正黨文宣部副主任兼發言人",
  "birth": 1979
},


{
  "name": "黃健瑋",
  "role": "公正黨文宣部主任",
  "birth": 1981
},

{
  "name": "王淨",
  "role": "公正黨文宣部黨工",
  "birth": 1998
},

{
  "name": "戴立忍",
  "role": "民和黨籍現任立法院院長",
  "birth": 1966
},

{
  "name": "陳昱中",
  "role": "靜宜大學學生",
  "birth": 2003
}

]

collection_ref = db.collection("人選之人─造浪者")
for doc in docs:
  collection_ref.add(doc)