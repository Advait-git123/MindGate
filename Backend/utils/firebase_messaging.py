import firebase_admin
from firebase_admin import credentials, messaging
import os

if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CREDENTIAL_PATH", "firebase_key.json")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def send_fcm(token: str, title: str, body: str):
    try:
        message = messaging.Message(
            notification=messaging.Notification(title=title, body=body),
            token=token
        )
        resp = messaging.send(message)
        return {"success": True, "response": resp}
    except Exception as e:
        return {"success": False, "error": str(e)}
