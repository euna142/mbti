from flask import Flask, request, jsonify

app = Flask(__name__)

# MBTI 계산 함수
def calculate_mbti(answers):
    scores = {'I': 0, 'E': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    for i, answer in enumerate(answers):
        if i < 4:  # E/I 질문
            scores['I' if answer == 'A' else 'E'] += 1
        elif i < 8:  # S/N 질문
            scores['S' if answer == 'A' else 'N'] += 1
        else:  # T/F 질문
            scores['T' if answer == 'A' else 'F'] += 1

    mbti = (
        ('I' if scores['I'] > scores['E'] else 'E') +
        ('S' if scores['S'] > scores['N'] else 'N') +
        ('T' if scores['T'] > scores['F'] else 'F') +
        ('J' if scores['J'] > scores['P'] else 'P')
    )
    result_image = f"/static/images/{mbti.lower()}.jpg"
    return mbti, result_image

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.get_json()
    answers = data.get('answers', [])
    result, result_image = calculate_mbti(answers)
    return jsonify({"result": result, "result_image": result_image})

if __name__ == '__main__':
    app.run(debug=True)
