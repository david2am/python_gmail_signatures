![GitHub](https://img.shields.io/github/license/eberkund/gsuite-signature-manager.svg)

# Bulk Signature Update

Python app that allows G Suite administrators to change email signatures using a mustache template.

### Setup

Set the virtual environment `venv`,
```
python -m venv venv
```
Activate it
```
venv\Scripts\activate.bat
```

Install the dependencies using `pip`,

```
pip install -r requirements.txt
```

You will also need to create,

- `users.csv` with the user info
- `credentials.json` Google [service account credentials](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) available through [Developer Console](https://console.developers.google.com/iam-admin/serviceaccounts/)
- your own custom template, updating the `template.mustache` content
- This app requires [delegated domain-wide authority](https://developers.google.com/admin-sdk/directory/v1/guides/delegation)

### Usage

After setup you can just run the script,

```
python app.py
```