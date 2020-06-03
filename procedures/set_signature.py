from googleapiclient.discovery import build
from pystache import Renderer

def set_signature(credentials, data):
    ''' updates corporate gmail account signatures
        Args:
        credentials: API credentials
        data: data dictionary {'column_name': current_value,...}
    '''

    try:
        # mapping data into the template
        body = {'signature': Renderer().render_path('template.mustache', data)}

        # build gmail endpoint
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
