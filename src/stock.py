PK�����PíZ¿*´íÔ��Ô�����main.pyfrom flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_number = 'whatsapp:+14155238886'

recipients = [
    'whatsapp:+919901849885',
    'whatsapp:+918546979139'
]

client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return "âœ… Stock Alert Bot Running"

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '')
    response_msg = "ðŸ¤– Automated Stock Alert Bot. Please wait for updates."
    return response_msg, 200

@app.route('/send-dummy-alert', methods=['GET'])
def send_dummy_alert():
    msg = (
        "ðŸ“¢ *Dummy Stock Alert*
"
        "ðŸ—‚ï¸ Sample Filing
"
        "ðŸ•’ 13 Jul 2025, 11:00 AM
"
        "ðŸ“Ž https://dummy-link.com"
    )
    for to in recipients:
        client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to)
    return "âœ… Dummy alert sent"

@app.route('/send-yesterday-stock-updates', methods=['GET'])
def send_yesterday_stock_updates():
    messages = [
        (
            "ðŸ§¾ *Fineotex Chemicals â€“ 12 Jul 2025*

"
            "ðŸ“¢ *Fineotex Chemicals*
"
            "ðŸ—‚ï¸ Regulation 30 â€“ Director Reappointments
"
            "ðŸ“‹ Re-appointed: Bindu Darshan Shah, Sunil Waghmare, Sanjay Tibrewala & Surendra Tibrewala
"
            "ðŸ•’ Filing Time: 3:26 PM
"
            "ðŸ“Ž https://www.bseindia.com/xml-data/corpfiling/AttachLiveLink1.pdf"
        ),
        (
            "ðŸ§¾ *GPT Healthcare â€“ 12 Jul 2025*

"
            "ðŸ“¢ *GPT Healthcare*
"
            "ðŸ—‚ï¸ Annual Report & AGM Notice (36th AGM)
"
            "ðŸ—“ï¸ AGM Date: 5 Aug 2025
"
            "ðŸ•’ Filing Time: 5:30 PM
"
            "ðŸ“Ž https://nsearchives.nseindia.com/corporate/GPTHEALTHCARE_12072025173015_GHLSubmissionofLetter36_1_12072025.pdf"
        )
    ]

    for msg in messages:
        for to in recipients:
            client.messages.create(body=msg, from_='whatsapp:+14155238886', to=to)

    return "âœ… Yesterday's stock updates sent via WhatsApp!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)PK�����PíZ˜¼cz$���$������requirements.txtflask
twilio
requests
beautifulsoup4PK�����PíZ-œ7Ä���������Procfileweb: python main.pyPK�����PíZ¿*´íÔ��Ô�������������¤����main.pyPK�����PíZ˜¼cz$���$��������������¤ù��requirements.txtPK�����PíZ-œ7Ä�����������������¤K	��ProcfilePK������©���„	����
