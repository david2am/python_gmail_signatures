from __future__ import print_function
import pickle
import os.path
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pystache import Renderer

# set of permissions over gmail account
SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic',
          "https://www.googleapis.com/auth/gmail.settings.sharing"]


def get_credentials():
    creds = None

    # get credentials from token.pickle
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # if there are no credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('../credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def update_gmail_signature(creds, db_row):
    email, name, lastname, title, cellphone = db_row
    # calling gmail service
    gmail_service = build('gmail', 'v1', credentials=creds)

    # setting signature
    body = {
        'signature': Renderer().render_path('signature.mustache',
            {
                'name':      name,
                'lastname':  lastname,
                'title':     title,
                'cellphone': cellphone,
                'email':     email
            }
        )
    }

    # searching for primary email
    primary_alias = None
    aliases = gmail_service.users().settings().sendAs().list(userId='me').execute()
    for alias in aliases.get('sendAs'):
        if alias.get('isPrimary'):
            primary_alias = alias
            break

    # updating signature
    result = gmail_service.users().settings().sendAs().patch(
        userId='me',
        sendAsEmail=primary_alias.get('sendAsEmail'),
        body=body
    ).execute()

    print('Updated signature for: %s' % result.get('displayName'))

# open and read csv file
with open('users.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    creds = get_credentials()
    for row in reader:
        update_gmail_signature(creds, row)
