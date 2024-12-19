from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
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
    }
]


random.shuffle(questions)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-question', methods=['GET'])
def get_question():
    question = 10
    current_question_index = int(request.args.get('index', 0))
    if current_question_index < len(questions):
        question = questions[current_question_index]
        return jsonify({
            "question": question["question"],
            "options": question["options"],
            "index": current_question_index
        })
    else:
        return jsonify({"end": True, "score": request.args.get('score', 0)})


@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data.get("index")
    selected_option = data.get("selected")

    if questions[question_index]["answer"] == selected_option:
        return jsonify({"correct": True})
    else:
        return jsonify({"correct": False, "correct_answer": questions[question_index]["answer"]})
    
if __name__=='_main_':
    
    app.run(debug=True)