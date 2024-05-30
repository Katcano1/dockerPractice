import json
import time

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


@app.route("/jobs/status", methods=["GET"])
def get_job_status():
    position = []
    for x in range(len(q.queue)):
        position.append(x)
    json_array = [{"Position:": p, "Job:": j} for p, j in zip(position, q.queue)]
    return jsonify(json_array), 200


@app.route("/jobs", methods=["POST"])
def post_job():
    job = json.loads(request.data)

    temp_job = [job["uuid"], job["job_name"], job["priority"], job["execution_time"]]

    q.enqueue(temp_job)

    return jsonify(job), 201


@app.route("/jobs", methods=["DELETE"])
def dequeue_job():
    temp_exec_time = q.queue[0][3]
    time.sleep(int(q.queue[0][3]))
    q.dequeue()

    response = {"response": "successfully dequeued job at the front of the queue. Time taken: " + temp_exec_time + " seconds."}
    return jsonify(response), 202


@app.route("/jobs/<uuid>", methods=["DELETE"])
def delete_job(uuid):
    temp_exec_time = q.get_job_by_uuid(uuid)[3]
    q.delete_by_uuid(uuid)

    response = {"response": "successfully deleted job with uuid " + uuid + ". Time taken: " + temp_exec_time + " seconds"}
    return jsonify(response), 202


if __name__ == "__main__":
    app.run(debug=True)