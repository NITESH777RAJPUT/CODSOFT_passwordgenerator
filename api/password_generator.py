import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with specified length and character types.
    
    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: At least one character type must be selected"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Ensure at least one character of each selected type
    if use_uppercase:
        password = password[:-1] + random.choice(string.ascii_uppercase)
    if use_lowercase:
        password = password[:-1] + random.choice(string.ascii_lowercase)
    if use_digits:
        password = password[:-1] + random.choice(string.digits)
    if use_special:
        password = password[:-1] + random.choice(string.punctuation)
    
    # Shuffle the password to randomize the ensured characters
    password = ''.join(random.sample(password, len(password)))
    
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    error = ''
    length = 12
    use_uppercase = True
    use_lowercase = True
    use_digits = True
    use_special = True
    
    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            use_uppercase = 'uppercase' in request.form
            use_lowercase = 'lowercase' in request.form
            use_digits = 'digits' in request.form
            use_special = 'special' in request.form
            
            if length < 8:
                error = "Password length must be at least 8 characters"
            elif not any([use_uppercase, use_lowercase, use_digits, use_special]):
                error = "At least one character type must be selected"
            else:
                password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        except ValueError:
            error = "Please enter a valid number for password length"
    
    return render_template('index.html', password=password, error=error,
                         length=length, use_uppercase=use_uppercase,
                         use_lowercase=use_lowercase, use_digits=use_digits,
                         use_special=use_special)

if __name__ == '__main__':
    app.run(debug=True)