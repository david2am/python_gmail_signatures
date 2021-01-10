![GitHub](https://img.shields.io/github/license/eberkund/gsuite-signature-manager.svg)

# Signature Update for G Suite Aministrators

Python app to change email signatures using a mustache template.

### Setup

Set the virtual environment `venv`,
```
python -m venv venv
```
Activate `venv` in Windows:
```
venv\Scripts\activate.bat
```
Activate `venv` in Mac/Linux:
```
source venv/bin/activate
```

Install the dependencies using `pip`,

```
pip install -r requirements.txt
```

You will also need to create,

- `users.csv` with the user info
- `credentials.json` from Google [service account credentials](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) available through [Developer Console](https://console.developers.google.com/iam-admin/serviceaccounts/)

And change,

- `signature_template.mustache` content

And finally, use [delegated domain-wide authority](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) to give permissions SCOPES to the app over Gmail service.

### Run

After setup you can just run the script,

```
python app.py
```

### License

[MIT License](https://choosealicense.com/licenses/mit/)