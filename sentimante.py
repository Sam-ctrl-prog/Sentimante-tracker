from flask import Flask, request, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sentimante.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity: -1 (negative) to +1 (positive)
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    
    return jsonify({'text': text, 'polarity': polarity, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
