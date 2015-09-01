from getpass import getpass;


def login():
    username = raw_input();
    password = getpass();
    print("Username: " + username);
    print("Password: " + password);

login()