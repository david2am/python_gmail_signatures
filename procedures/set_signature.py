from googleapiclient.discovery import build
from pystache import Renderer

def set_signature(credentials, row):
    ''' updates a bulk of signatures in a gmail account
        Args:
            credentials: the credentials to acces the API
            row: dict of values {'column_name': value,...} to map in the blueprint '''

    try:
        # signature blueprint
        body = {'signature': Renderer().render_path('signature.mustache', row)}

        # building gmail endpoint
        gmail_endpoint = build('gmail', 'v1', credentials=credentials).users().settings().sendAs()

        # get primary email
        primary_email = None
        emails = gmail_endpoint.list(userId='me').execute()
        
        for alias in emails.get('sendAs'):
            if alias.get('isPrimary'):
                primary_email = alias
                break

        # set signature with primary email
        gmail_endpoint.patch(
            userId='me',
            sendAsEmail=primary_email.get('sendAsEmail'),
            body=body
        ).execute()

        print('Signature updated')
    except:
        print("An exception occurred")
