from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/deals")
def get_deals():
    return jsonify([
        {
            "store": "Test Store",
            "name": "Test Product",
            "original": "$49.99",
            "sale": "$19.99",
            "discount": "60%",
            "url": "https://example.com/deal"
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)
