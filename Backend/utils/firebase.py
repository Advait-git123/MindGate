# backend/utils/firebase.py
import firebase_admin
from firebase_admin import credentials, messaging
import os

# Path to your Firebase service account JSON file
FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH", "firebase_service_account.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)

def send_push_notification(token: str, title: str, body: str):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    try:
        response = messaging.send(message)
        print(f"Sent to {token[:10]}... → {response}")
    except Exception as e:
        print(f"Failed to send to {token[:10]}... → {e}")
