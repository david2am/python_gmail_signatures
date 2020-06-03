from __future__ import print_function
import pandas as pd
from procedures.credentials import get_credentials
from procedures.signature import set_signature

def main():
    # get service credentials
    credentials = get_credentials()

    # read .csv file
    df = pd.read_csv('../users.csv', sep=',')
    df.columns = [label.replace(' ', '_') for label in df.columns]

    # set signature per user in db
    for data in df.to_dict(orient='records'):
        set_signature(credentials, data, data['Email_Address'])


if __name__ == '__main__':
    main()
