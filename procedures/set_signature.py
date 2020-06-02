from googleapiclient.discovery import build
from pystache import Renderer

def set_signature(creds, row):
    ''' Updates signatures in a gmail account
        Args:
            creds: the credentials to acces the API
            row: dict of values {'column_name_0': value,...} 
    '''

    # setting signature
    body = {'signature': Renderer().render_path('signature.mustache', row)}

    # calling gmail service
    gmail_endpoint = build('gmail', 'v1', credentials=creds).users().settings().sendAs()

    # get primary email
    primary_email = None
    emails = gmail_endpoint.list(userId='me').execute()
    
    for alias in emails.get('sendAs'):
        if alias.get('isPrimary'):
            primary_email = alias
            break

    # set signature with primary email
    result = gmail_endpoint.patch(
        userId='me',
        sendAsEmail=primary_email.get('sendAsEmail'),
        body=body
    ).execute()

    print('Updated signature for: %s' % result.get('displayName'))