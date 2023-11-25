from flask import Flask, render_template, request, jsonify
import redis

app = Flask(__name__, static_url_path='/static')
redis_db = redis.StrictRedis(host='redis', port=6379, db=0)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_data', methods=['POST'])
def set_data():
    data = request.form['data']
    redis_db.set('example_key', data)
    return jsonify({'message': 'Data stored successfully'})

@app.route('/get_data', methods=['GET'])
def get_data():
    value = redis_db.get('example_key')
    return jsonify({'data': value.decode('utf-8') if value else None})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

