from __future__ import print_function
import pandas as pd
from procedures.get_credentials import get_credentials
from procedures.set_signature import set_signature

def main():
    # get credentials from gmail service
    credentials = get_credentials()

    # read .csv file
    df = pd.read_csv('users.csv', sep=',')
    df.columns = [label.replace(' ', '_') for label in df.columns]

    # set signature per user in db
    for row in df.to_dict(orient='records'):
        set_signature(credentials, row)


if __name__ == '__main__':
    main()
