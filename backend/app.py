from flask import Flask, jsonify
from flask_cors import CORS

from aws_services import get_aws_snapshots

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "project": "SnapGuard",
        "message": "Backend is running successfully!",
        "status": "online"
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "success": True,
        "project": "SnapGuard",
        "backend": "Flask",
        "status": "healthy",
        "message": "SnapGuard backend is running successfully"
    }), 200




@app.route("/api/dashboard", methods=["GET"])
def dashboard():
    return jsonify({
        "success": True,
        "project": "SnapGuard",
        "data": {
            "total_snapshots": 24,
            "active_snapshots": 20,
            "lifecycle_policies": 3
        },
        "mode": "demo",
        "message": "Demo data is displayed. AWS integration is pending."
    }), 200

@app.route("/api/snapshots", methods=["GET"])
def snapshots():
    """Fetch EBS snapshots from AWS."""

    result = get_aws_snapshots()

    if not result.get("success"):
        return jsonify({
            "success": False,
            "message": "Unable to retrieve AWS snapshots.",
            "error": result.get("error", "Unknown AWS error"),
            "region": result.get("region", "ap-south-1")
        }), 503

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )