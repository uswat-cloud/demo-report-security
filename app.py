from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16384


@app.post("/report")
def report():
    try:
        data = yaml.safe_load(request.get_data(as_text=True))
    except yaml.YAMLError:
        return jsonify(error="Invalid YAML"), 400

    if not isinstance(data, dict):
        return jsonify(error="Expected a mapping"), 400

    if set(data) != {"service", "status"}:
        return jsonify(error="Expected service and status only"), 400

    if (
        not isinstance(data["service"], str)
        or not data["service"].strip()
    ):
        return jsonify(error="Service must be a nonblank string"), 400

    if data["status"] not in (
        "healthy",
        "degraded",
        "unavailable",
    ):
        return jsonify(error="Unknown status"), 400

    return jsonify(
        service=data["service"].strip(),
        status=data["status"],
    )
