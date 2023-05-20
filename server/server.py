from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_location_names():
    response = jsonify({
        'manufacturers': util.get_manufacturer_names(),
        'categorys': util.get_category_names(),
        'screens': util.get_screen_names(),
        'cpus': util.get_cpu_names(),
        'storages': util.get_storage_names(),
        'gpus': util.get_gpu_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/', methods=['GET', 'POST'])
def predict_price():
    total_ss = float(request.form['total_ss'])
    ram = int(request.form['ram'])
    manufaturer = request.form['manufacturer']
    category = request.form['Category']
    screen = request.form['Screen']
    cpu = request.form['CPU']
    storage = request.form['Storage']
    gpu = request.form['GPU']

    response = jsonify({
        'estimated_price': util.get_estimated_price(total_ss,ram,manufaturer,category,screen,cpu,storage,gpu)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("start")
    util.load_saved_artifacts()
    app.run(debug=True, port=8000)
