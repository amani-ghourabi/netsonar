from flask import Flask, jsonify, request, send_from_directory

from src.scanner import scan_cidr

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/api/scan")
def api_scan():
    network = request.args.get("network", "")
    try:
        devices = scan_cidr(network)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return jsonify({"network": network, "devices": devices})


if __name__ == "__main__":
    app.run(debug=True)