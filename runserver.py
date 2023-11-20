# load env
from dotenv import load_dotenv
# load .env
load_dotenv()

from flask import Flask, request, jsonify, abort

from src.constants import PYTHONANYWHERE_IP
from src.ner import generate_ner_tags

app = Flask(__name__)

def check_ip(f):
    def decorator(*args, **kwargs):
        if request.remote_addr != PYTHONANYWHERE_IP:
            abort(403)  # Forbidden access
        return f(*args, **kwargs)
    return decorator

@app.route('/ner', methods=['POST'])
@check_ip
def ner():
    try:
        # gen ner tags
        articles = request.json
        ner_tags = generate_ner_tags(articles)
        return jsonify(ner_tags), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)