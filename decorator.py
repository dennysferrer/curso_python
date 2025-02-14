password = '12345678'

def password_required(func):
  def wrapper():
    password_input = input('Por favor digita la contraseña: ')
    if password_input == password:
      return func
    else:
      print('La contraseña no es correcta...')
  return wrapper()

@password_required
def needs_password():
  print('La constraseña es correcta...')


if __name__ == '__main__':
  needs_password()