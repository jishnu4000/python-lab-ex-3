from smartscan_registration_module import *
import pyqrcode
import re

# create a QR cde with the data encoded in it
def create_user_qrcode(name, email):
  # put data in required format
  data = f'{name},{email}'

  # create QR code
  qr = pyqrcode.create(data)

  # save QR code as PNG image
  qr.png(fr'./qr-images/{name}-qrcode.png', scale=8)

  return qr.terminal(quiet_zone=1)

# validate name with regex
def name_validation(name):
  pattern = r'^[A-Za-z]+([-\' ][A-Za-z]+)*$'
  return bool(re.match(pattern, name))

# validate email with regex
def email_validation(email):
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return bool(re.match(pattern, email))

# get valid choice as input
def choice():
  choices = ['y', 'n']
  choice = input('Do you want to register a new user? (y/n): ').lower()

  while (choice not in choices):
    choice = input('Type "y" for yes or "n" for no: ')

  return choice

# main function
if __name__ == '__main__':
  print('User Registration')
  print('------------------------------------------------------')
  user_choice = choice()

  while user_choice == 'y':

    user_name = input('Enter user name: ')
    while (not name_validation(user_name)):
      user_name = input('Enter a valid user name: ')

    user_email = input('Enter user email address: ')
    while (not email_validation(user_email)):
      user_email = input('Enter a valid user email address: ')

    new_user_qr = create_user_qrcode(user_name, user_email)

    RegisterUserFromSmartScan(fr'./qr-images/{user_name}-qrcode.png')

    print('------------------------------------------------------')
    print()

    user_choice = choice()
    if user_choice == 'y': continue
    else: break

  print('User Registration has ended.')
