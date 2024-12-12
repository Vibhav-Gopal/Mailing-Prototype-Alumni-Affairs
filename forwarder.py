import os
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set up your Google Cloud Console project and enable the Gmail API
# Instructions: https://developers.google.com/gmail/api/quickstart/python

# Path to the file containing the credentials (downloaded from Google Cloud Console)
CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://mail.google.com/']

# ID of the email you want to forward
MESSAGE_ID = 'CA+5Ue-Kn26NqEJkUG-uWQZ9vOtpymANQ-3_E_tjYOpZOGHkdEg@mail.gmail.com'

# List of subscribers' email addresses
SUBSCRIBERS = ['vibhavgopal2004+test@gmail.com']

def create_gmail_service():

    """Create Gmail service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentifor als the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    creds = Credentials.from_authorized_user_file("token.json")
    print("Created GMAIL Service")
    return build('gmail', 'v1', credentials=creds)

def get_message(service, user_id, msg_id):
    """Get a specific message."""
    var = "Rfc822msgid:" + msg_id
    try:
        print("Searching for Message")
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        print("Message found")
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def forward_message(service, user_id, msg_id, to_list):
    """Forward a message to a list of recipients."""
    message = get_message(service, user_id, msg_id)
    if message:
        msg_str = message['raw']
        message['raw'] = None  # Clearing raw to avoid conflicts
        
        forwarded_message = {
            'raw': base64.urlsafe_b64encode(msg_str.encode()).decode(),
            'headers': {
                'To': ', '.join(to_list),
                'Subject': 'Fwd: ' + message['payload']['headers'][0]['value']  # Prefixing subject with 'Fwd:'
            }
        }

        try:
            print("Message forward started")
            service.users().messages().send(userId=user_id, body=forwarded_message).execute()
            print('Message forwarded successfully.')
        except Exception as e:
            print(f'An error occurred: {e}')

def main():
    service = create_gmail_service()
    if service:
        forward_message(service, 'me', MESSAGE_ID, SUBSCRIBERS)

if __name__ == '__main__':
    main()
