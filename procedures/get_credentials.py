from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

# set of permissions over gmail account
SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic',
          "https://www.googleapis.com/auth/gmail.settings.sharing"]

def get_credentials():
    ''' use oauth2 to get credentials from gmail authorization API 
    '''
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
            flow = InstalledAppFlow.from_client_secrets_file('../../credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds