# Bhai paise dede

- bhaipaisedede.com is a website that allows you track and request the money owed to you by your friends.

## Tech stack 

- flask with jinja2 templating engine
- local postgress


### Folder Structure
```bash
bhai_paise_dede/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── group.py
│   │   └── expense.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── groups.py
│   │   └── expenses.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   ├── main/
│   │   │   ├── index.html
│   │   └── components/
│   │       ├── header.html
│   │       ├── footer.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

### Colors and designs 

- Black & white
- Finance inspired
- Bootstrap CSS framework
