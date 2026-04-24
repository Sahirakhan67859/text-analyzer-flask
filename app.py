from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    word_count = len(text.split())
    char_count = len(text)
    return jsonify({'words': word_count, 'chars': char_count})

if __name__ == '__main__':
    app.run(debug=True)