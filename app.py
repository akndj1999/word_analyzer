
# from flask import Flask, render_template, request
# from collections import Counter

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     text = request.form['text']
#     words = text.split()
#     total_words = len(words)
#     unique_words = set(words)
#     words_count = Counter(words)
#     most_common = words_count.most_common(1)[0]

#     return render_template('result.html',
#                            total=total_words,
#                            unique=unique_words,
#                            most_common=most_common,
#                            original_text=text)

# if __name__ == '_main_':
#     app.run(debug=True)

from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    words = text.split()
    total_words = len(words)
    unique_words = set(words)
    word_counts = Counter(words)
    
    unique_words = [word for word, count in word_counts.items() if count == 1]
    most_common = word_counts.most_common(1)[0]

    return render_template('result.html',
                           total=total_words,
                           unique=unique_words,
                           most_common=most_common,
                           original_text=text)

if __name__ == '__main__':
    app.run(debug=True)
