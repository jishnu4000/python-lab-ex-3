from pyzbar.pyzbar import decode
from PIL import Image

# list of dictionaries storing user data
users = [
  {'name': 'John Jones', 'email': 'john@example.com'},
]

# lambda functions to create a user, insert a user to list and get all users in list
create_user = lambda new_name, new_email: { 'name': new_name, 'email': new_email }

insert_user = lambda user: users.append(user)

get_all_users = lambda: [print(f' Person: {user["name"]}, Email: {user["email"]}') for user in users]

# accept a QR code as input and return the encoded data
def smart_scan_decode(qrCodeImg):
  img = Image.open(qrCodeImg)
  data = decode(img)
  if data:
    return data[0].data.decode("utf-8")
  else:
    return None

# decodes user data, creates user, adds user to list and print all users data
def RegisterUserFromSmartScan(qrCode):
  user_data = smart_scan_decode(qrCode)
  if user_data:
    name, email = user_data.split(',')
    new_user = create_user(name, email)
    print(f'New user {name} with email {email} created.')
    insert_user(new_user)
    print(f'New user {name} added to the users list.')
    print('All users currently in the list:')
    get_all_users()
  else:
    print("No data found in the QR code.")
