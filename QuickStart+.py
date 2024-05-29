import json

from flask import Flask, jsonify, request
from Queue import Queue
from QuickStart import read_from_file

file_path = "jobs_small"
q = Queue()
q = read_from_file(file_path, q)

app = Flask(__name__)

@app.route("/jobs", methods=["GET"])
def get_job():
    return jsonify(q.queue[0]), 200

@app.route("/jobs", methods=["POST"])
def post_job():
    job = json.loads(request.data)

    temp_job = [job["uuid"], job["job_name"], job["priority"]]

    q.enqueue(temp_job)

    return jsonify(job), 201




if __name__ == "__main__":
    app.run(debug=True)