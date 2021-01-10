from googleapiclient.discovery import build
from pystache import Renderer

def set_signature(credentials, data, email):
    ''' updates corporate gmail account signatures
        Args:
        credentials: API credentials
        data: data dictionary {'column_name': current_value,...} '''

    try:
        # mapping data into the template
        body = {'signature': Renderer().render_path('signature_template.mustache', data)}

        # build gmail endpoint
        gmail_endpoint = build('gmail', 'v1', credentials=credentials).users().settings().sendAs()

        # get primary email alias
        primary_alias = None
        aliases = gmail_endpoint.list(userId=email).execute()
        for alias in aliases.get('sendAs'):
            if alias.get('isPrimary'):
                primary_alias = alias
                break

        # set signature with primary email alias
        gmail_endpoint.patch(
            userId=primary_alias.get('sendAsEmail'),
            sendAsEmail=primary_alias.get('sendAsEmail'),
            body=body
        ).execute()

        print('Signature updated for ' + primary_alias.get('sendAsEmail'))
    except Exception as error:
        print(error)
