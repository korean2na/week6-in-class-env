from app import app
from flask import render_template

# Create 3 new routes, they can return whatever text
# Contact, Blog, Shop
# @app.route('/contact')
# def contact():
#     return 'NO SOLICITORS!'

# @app.route('/blog')
# def blog():
#     dicto = {
#         1: '12/3/22: Entry 1',
#         2: '12/4/22: Entry 2',
#         3: '12/5/22: Entry 3'
#     }
#     return dicto
    
# @app.route('/shop')
# def shop():
#     num1 = 1
#     num2 = 2
#     num3 = num1 + num2
#     return f'Shopping is easy as 1, 2 ,3:\n{num1} + {num2} = {num3}'

user_data = { # mock user table
    'dylans': {
        'user_id': 1,
        'email': 'dylans@gmail.com',
        'name': 'Dylan Smith',
        'favorite_color': 'Purple',
        'is_active': True,
        'reviews': ['Dylan is a great dev!', 'He\'s the best']
    },
    'jdoe': {
        'user_id': 2,
        'email': 'afemaledeer@gmail.com',
        'name': 'Jane Doe',
        'favorite_color': 'Green',
        'is_active': True,
        'reviews': ['Jane failed me', 'Jane is the best!']
    },
    'jcena': {
        'user_id': 3,
        'email': 'peacemaker@aol.com',
        'name': 'Jon Cena',
        'favorite_color': 'Freedom',
        'is_active': False,
        'reviews': ['Jon did the job well.']
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<username>')
def display_profile(username):
    return render_template('profile.html.j2', **user_data[username])

# Functions/Endpoints
# Get all users and their data
@app.route('/api/users')
def get_users():
    return user_data

# Get all user emails
@app.route('/api/users/emails')
def get_user_emails():
    emails = []
    for user in user_data.values():
        emails.append(user['email'])

    return emails

# Get a user by their username
@app.route('/api/user/<username>')
def get_user_by_username(username):
    if username in user_data:
        return user_data[username]
    
    return f'User with username {username} not found.'

# Get a user by their email
@app.route('/api/user/email/<email>')
def get_user_by_email(email):
    for user in user_data.values():
        if user['email'] == email:
            return user
    
    return f'User with email {email} not found.'

# Find all users with a specified favorite color
@app.route('/api/user/favorite_color/<favorite_color>')
def get_user_by_favorite_color(favorite_color):
    users = []

    for user in user_data.values():
        if user['favorite_color'].lower() == favorite_color.lower():
            users.append(user)
    
    return users

# Find specified review of a specified user
@app.route('/api/user/<username>/reviews/<review_idx>')
def get_user_review(username, review_idx):
    return user_data[username]['reviews'][int(review_idx)]


# Write an endpoint, similar to the previous one
# that returns a list of active user's names.
@app.route('/api/users/active')
def get_active_users():
    actives = []
    for user in user_data.values():
        if user['is_active']:
            actives.append(user['name'])

    return actives


car_data = {
    '0': {
        "name": "Maruti Swift Dzire VDI",
        "year": 2014,
        "selling_price": 450000
    },
    '1': {
        "name": "Skoda Rapid 1.5 TDI Ambition",
        "year": 2014,
        "selling_price": 370000
    },
    '2': {
        "name": "Honda City 2017-2020 EXi",
        "year": 2006,
        "selling_price": 158000
    },
    '3': {
        "name": "DMC DeLorean 2.85L V6 5-Speed",
        "year": 1983,
        "selling_price": 88000000
    }
}

# Get all cars
# @app.route('/api/cars')
# def get_cars():
#     return car_data

# Get cars in a dictionary separated by year, for example:
# car_year_result = {
#     2014: ["Maruti Swift Dzire VDI","Skoda Rapid 1.5 TDI Ambition"],
#     2006: ["Honda City 2017-2020 EXi"]
# }
@app.route('/api/cars/years')
def get_cars_by_years():
    car_year_result = {}
    for car in car_data.values():
        if car['year'] not in car_year_result:
            car_year_result[car['year']] = [car['name']]
        else:
            car_year_result[car['year']].append(car['name'])

    return car_year_result

# Get a car by it's ID (it's ID is just the key in the car data dictionary)
# @app.route('/api/cars/id/<id>')
# def get_car_by_id(id):
#     if int(id) in car_data:
#         return car_data[int(id)]
    
#     return f'Car with ID {id} not found.'

# Get all cars below a given price point, so if the user enters 380000, you'd show the second and third cars
@app.route('/api/cars/price/<price>')
def get_cars_below_price(price):
    cars_below = []
    for car in car_data.values():
        if car['selling_price'] < int(price):
            cars_below.append(car)
    
    return cars_below


# Create 2 routes/templates:
# - Display all cars using a for loop and their information (not dynamic)
@app.route('/cars')
def get_cars():
    return render_template('cars.html.j2', car_data = car_data)

# - Display a specific car and it's information (Will be dynamic, you can use the car's ID in the car_data dict)
@app.route('/cars/id/<id>')
def get_car_by_id(id):
    return render_template('car_profile.html.j2', **car_data[id])