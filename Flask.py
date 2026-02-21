from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# دیکشنری ساده
dictionary = {
    'hello': 'سلام',
    'world': 'دنیا',
    'example': 'نمونه'
}

@app.route('/')
def home():
    return render_template('dic.html', dictionary=dictionary)

@app.route('/search')
def search():
    word = request.args.get('word', '')
    definition = dictionary.get(word, None)
    return jsonify({'definition': definition})

if __name__ == '__main__':
    app.run(debug=True)