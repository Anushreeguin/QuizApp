questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
     {
        "question": "What is your college name?",
        "options": ["UIT BU", "IIT Bombay", "'IIT KGP", "NIT"],
        "answer": "UIT BU"
    },
    {
        "question": "Which programming language is known as the language of the web?",
        "options": ["Python", "JavaScript", "Java", "C++"],
        "answer": "JavaScript"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
       "question" : "Which of the three banks will be merged with the other two to create India’s third-largest bank?",
       "options" : ["Punjab National Bank", " Bank of Baroda  " , "Indian Bank" , "Dena Bank"],
        "answer" : "Indian Bank"
    },
    {
        "question": "What is the name of the weak zone of the earth’s crust?",
        "options": ["Seismic", "Cosmic", "Formic", "Anaemic"],
        "answer": "Seismic"
    },
    {
        "question": "Where was India’s first national Museum opened?",
        "options": ["Delhi", "Hyderabad", "Rajasthan", "Mumbai"],
        "answer": "Mumbai"
    },
    {
        "question": "In 2019, Which popular singer was awarded the Bharat Ratna award?",
        "options": ["Lata Mangeshkar", "Asha Bhosle", "Bhupen Hazarika", "Manna Dey"],
        "answer": "Bhupen Hazarika"
    },
    {
        "question": "The world’s first 5G mobile network was launched by which country?",
        "options": ["Japan", "Asia", "South Korea", "Malaysia"],
        "answer": "South Korea"
    },
    {
        "question": "When was Pravasi Bhartiya Divas held in Varanasi?",
        "options": ["2017", "2015", "2019", "2020"],
        "answer": "2019"
    },
    {
        "question": "Vijay Singh (golf player) is from which country?",
        "options": ["UK", "USA", "India", "Fiji"],
        "answer": "Fiji"
    },
    {
        "question": "What is the full form of DRDL?",
        "options": [
            "Differential Research and Documentation Laboratory",
            "Department of Research and Development Laboratory",
            "Defense Research and Development Laboratory",
            "None of the above"
        ],
        "answer": "Department of Research and Development Laboratory"
    },
    {
        "question": "The green planet in the solar system is?",
        "options": ["Mars", "Uranus", "Venus", "Earth"],
        "answer": "Uranus"
    },
    {
        "question": "The father of Indian missile technology is?",
        "options": ["Dr Homi Bhabha", "Dr Chidambaram", "Dr U.R. Rao", "Dr A.P.J. Abdul Kalam"],
        "answer": "Dr A.P.J. Abdul Kalam"
    },
    {
        "question": "What is the reason behind the Bats flying in the dark?",
        "options": [
            "they produce high-pitched sounds called ultrasonics",
            "the light startles them",
            "they have a perfect vision in the dark",
            "none of the above"
        ],
        "answer": "they produce high-pitched sounds called ultrasonics"
    },
    {
        "question": "Which of these is the small-scale industry in India?",
        "options": ["Jute industry", "Paper Industry", "Textile Industry", "Handloom Industry"],
        "answer": "Handloom Industry"
    },
    {
        "question": "Which of these is the plant important in sericulture?",
        "options": ["Cassia", "Legumes", "Pea", "Mulberry"],
        "answer": "Mulberry"
    },
    {
        "question": "The largest public sector undertaking in the country is?",
        "options": ["Railways", "Airways", "Roadways", "Iron and Steel Plants"],
        "answer": "Railways"
    },
    {
        "question": "At which place on earth are there days & nights of equal length always?",
        "options": ["Equator", "Poles", "Prime Meridian", "Nowhere"],
        "answer": "Equator"
    },
    {
        "question": "In 2017, Who was appointed as the new Brand Ambassador for Swachh Bharat Mission?",
        "options": ["Kangana Ranaut", "Priyanka Chopra", "Anushka Sharma", "Shilpa Shetty"],
        "answer": "Shilpa Shetty"
    },
    {
        "question": "The study of Heavenly bodies is Known as _________?",
        "options": ["Astrophysics", "Astronautics", "Astrology", "Astronomy"],
        "answer": "Astronomy"
    },
    {
        "question": "Why is the color of papaya yellow?",
        "options": ["Lycopene", "Papain", "Carotene", "Caricaxanthin"],
        "answer": "Caricaxanthin"
    },
    {
        "question": "What is the name of the first Indian woman who wins the Man Booker Prize?",
        "options": ["Salman Rushdie", "Arundhati Roy", "V.S. Naipaul", "Kiran Desai"],
        "answer": "Arundhati Roy"
    }
]

import random

def ask_question(question):
    print(question['question'])
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")
    
    while True: 
        try:
            user_answer = int(input("Select your answer (1/2/3/4): "))
            if 1 <= user_answer <= len(question['options']):
                break
            else:
                print("Please select a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
    
    correct_answer = question['answer']
    if question['options'][user_answer - 1] == correct_answer:
        return True
    else:
        return False

def run_quiz():
    score = 0
    total_questions = len(questions)
    random.shuffle(questions)
     
    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {question['answer']}\n")
    
    print(f"Your final score: {score}/{total_questions}")


run_quiz()