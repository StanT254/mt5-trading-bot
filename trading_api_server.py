from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/economic_calendar', methods=['GET'])
def economic_calendar():
    # This would normally fetch data from an economic calendar API
    data = {
        "events": [
            {"date": "2026-02-28", "event": "GDP Release", "impact": "High"},
            {"date": "2026-03-01", "event": "Interest Rate Decision", "impact": "Medium"},
        ]
    }
    return jsonify(data)

@app.route('/api/sentiment_analysis', methods=['GET'])
def sentiment_analysis():
    # This would normally fetch data from a news API for sentiment analysis
    data = {
        "latest_news": [
            {"headline": "Market shows signs of recovery", "sentiment": "Positive"},
            {"headline": "Inflation worries persist", "sentiment": "Negative"},
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)