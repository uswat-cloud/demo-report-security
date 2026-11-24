from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)


@app.post("/report")
def report():
    data = yaml.load(
        request.get_data(as_text=True),
        Loader=yaml.Loader,
    )
    return jsonify(data)
