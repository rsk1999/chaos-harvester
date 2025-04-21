import os
import html2text
import requests
from imapclient import IMAPClient
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email import message_from_bytes

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
INGEST_URL = os.getenv("INGEST_URL", "http://localhost:8000/ingest")

def fetch_emails():
    with IMAPClient(EMAIL_HOST) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.select_folder("INBOX", readonly=True)

        # Look for UNSEEN messages
        messages = server.search(["UNSEEN"])
        if not messages:
            return

        for uid, raw_message in server.fetch(messages, ["RFC822"]).items():
            msg = message_from_bytes(raw_message[b"RFC822"])
            subject = msg["subject"]
            from_ = msg["from"]
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/html":
                        html = part.get_payload(decode=True).decode(errors="ignore")
                        body = html2text.html2text(html)
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            full_payload = f"From: {from_}\nSubject: {subject}\n\n{body.strip()[:1000]}"

            print(f"🔄 Ingesting: {subject}")
            requests.post(INGEST_URL, json={"payload": full_payload})
