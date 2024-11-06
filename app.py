from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo', methods=['GET'])
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_results.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-yo with toppings {users_froyo_toppings}!'

@app.route('/favorites', methods=['GET'])
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return render_template('favorites.html')

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_color = request.args.get('color')
    user_animal = request.args.get('animal')
    user_city = request.args.get('city')
    return f"Wow, I didn't know {user_color} {user_animal} lived in {user_city}."

@app.route('/secret_message', methods=['GET'])
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return render_template('secret_message.html')

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_message = sort_letters(request.form.get('message'))
    return f"Here's your secret message! {user_message}"



@app.route('/calculator', methods=['GET'])
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_results.html')

@app.route('/calculator_results', methods=['POST'])
def calculator_results():
    """Shows the user the result of their calculation."""
    pick_operand1 = int(request.form.get('operand1'))
    pick_operand2 = int(request.form.get('operand2'))
    pick_operation = request.form.get('operation')

    if pick_operation == 'add':
        user_result = pick_operand1 + pick_operand2
    elif pick_operation == 'subtract':
        user_result = pick_operand1 - pick_operand2
    elif pick_operation == 'multiply':
        user_result = pick_operand1 * pick_operand2
    elif pick_operation == 'divide':
        user_result = pick_operand1 / pick_operand2

    return f'You chose to {pick_operation} {pick_operand1} and {pick_operand2}. Your result is: {user_result}'


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    user_name = request.args.get('users_name')
    
    horoscope_sign = request.args.get('horoscope_sign')

    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    lucky_number = random.randint(1, 99)

    context = {
        'user_name': user_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(port=8000, debug=True)