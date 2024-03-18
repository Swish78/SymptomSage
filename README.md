# SymptomSage

SymptomSage is a health advisor application that uses a deep learning model to predict potential diseases based on user's symptoms, and provides health advice and answers to user's queries through a chatbot.

## Table of Contents

1. [Features](#features)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- User registration and login
- Symptom input
- Disease prediction
- Health advice
- Chatbot for health-related queries

## Technologies

- React
- Django
- Django REST Framework
- Djoser
- PostgreSQL
- TensorFlow
- Pandas
- NumPy
- Scikit-learn
- OpenAI's GPT-3

## Installation

1. Clone the repository:
```
git clone https://github.com/Swish78/symptomsage.git
```
2. Install the dependencies:
```
cd symptomsage
pip install -r requirements.txt
npm install
```
3. Set up the database and create a .env file with the necessary environment variables.
4. Run the migrations:
```
python manage.py migrate
```
5. Start the Django server:
```
python manage.py runserver
```
6. Start the React server:
```
npm start
```

## Usage

1. Register or log in to the application.
2. Input your symptoms.
3. View the predicted diseases and health advice.
4. Ask health-related queries to the chatbot.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
