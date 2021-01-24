import re
import stdiomask

# Must contain at least one uppercase, lowercase and numeric character. It can also contain special characters.
strongPassword = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,16}$')

# Logic for validating secure password.
validPassword = False
while (validPassword == False):
    print(f'''
Please create a secure password.

PASSWORD REQUIREMENTS -
- Between 8 and 16 characters.
- At least one uppercase and lowercase character.
- At least one numeric character.
- Special characters are allowed.
    ''')
    getPassword = stdiomask.getpass(prompt='-> ')
    while True:
        if len(getPassword) < 8:
            print('ERROR: Password too short. Please create a longer password.\n')
            break

        if len(getPassword) > 16:
            print('ERROR: Password too long. Please create a shorter password.\n')
            break

        try:
            password = strongPassword.search(getPassword).group()
            validPassword = True
            print('\nSUCCESS: Password securely stored.')
            break

        except AttributeError:
            print('\nERROR: Password does not meet the complexity requirements. Please create a more complex password.\n')
            break