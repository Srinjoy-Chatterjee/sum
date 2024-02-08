from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide valid integer values for num1 and num2.'}), 400

if __name__ == '__main__':
    app.run()
