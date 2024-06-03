import json
import time

from flask import Flask, jsonify, request
from Queue import Queue
from QuickStart import read_from_file
from http import HTTPStatus

# Automatically reads from a file to give the queue a starting point.
# Also does this to prove that read_from_file works
file_path = "jobs_small"
q = Queue()
q = read_from_file(file_path, q)

app = Flask(__name__)


@app.route("/jobs", methods=["GET"])
def get_job():
    # Checks if the queue is empty.
    if q.is_empty():
        response = {"ERROR:": "Queue is currently empty. Please add a new job to view the first element"}
        return jsonify(response), HTTPStatus.BAD_REQUEST

    # returns the job at the front of the Queue
    return jsonify(q.queue[0]), 200


@app.route("/jobs/status", methods=["GET"])
def get_job_status():
    # Checks if the queue is empty.
    if q.is_empty():
        response = {"ERROR:": "Queue is currently empty. Please add a new job to view the queue"}
        return jsonify(response), HTTPStatus.BAD_REQUEST

    # Creates a json array consisting of the position of the job in the queue and the job itself
    position = []
    for x in range(len(q.queue)):
        position.append(x)
    json_array = [{"Position:": p, "Job:": j} for p, j in zip(position, q.queue)]
    return jsonify(json_array), 200


@app.route("/jobs", methods=["POST"])
def post_job():
    # checks if the request is empty or not
    try:
        job = json.loads(request.data)
    except json.decoder.JSONDecodeError:
        priority_response = {"ERROR:": "Request is either empty or not in json format"}
        return jsonify(priority_response), HTTPStatus.BAD_REQUEST

    try:
        temp_job = [job["uuid"], job["job_name"], job["priority"], job["execution_time"]]
    except (json.decoder.JSONDecodeError, KeyError):
        priority_response = {"ERROR:": "Format is not correct. Format: 'uuid', 'job name', 'priority', 'execution "
                                       "time'."}
        return jsonify(priority_response), HTTPStatus.BAD_REQUEST

    # checks if the uuid already exists in the queue.
    for x in range(len(q.queue)):
        if temp_job[0] == q.queue[x][0]:
            uuid_duplicate_response = {"ERROR:": "uuid already exists. Please use a different uuid."}
            return jsonify(uuid_duplicate_response), HTTPStatus.BAD_REQUEST

    try:
        q.enqueue(temp_job)
        return jsonify(job), 201
    except ValueError:
        priority_response = {"ERROR:": "Priority and execution time must be integers."}
        return jsonify(priority_response), HTTPStatus.BAD_REQUEST


@app.route("/jobs", methods=["DELETE"])
def dequeue_job():
    # checks if the queue is empty
    if q.is_empty():
        response = {"ERROR:": "Queue is currently empty. Please add a new job before trying to dequeue."}
        return jsonify(response), HTTPStatus.BAD_REQUEST

    # stores the uuid and time for printing reasons, then sleeps according to the execution time
    temp_job = q.queue[0]
    temp_exec_time = str(q.queue[0][3])
    time.sleep(int(q.queue[0][3]))
    q.dequeue()

    response = {"Response:": "successfully executed " + temp_job[1] + " Time taken: " + temp_exec_time + " seconds."}
    return jsonify(response), 202


@app.route("/jobs/<uuid>", methods=["DELETE"])
def delete_job(uuid):
    try:
        # stores the job for printing reasons and then deletes the job with the specified uuid and sleeps.
        temp_job = q.get_job_by_uuid(uuid)
        q.delete_by_uuid(uuid)
        time.sleep(int(temp_job[3]))

        response = {"Response:": 'successfully executed ' + temp_job[1] + " with uuid " + uuid + ". Time taken: " + str(temp_job[3]) + " seconds"}
        return jsonify(response), 202

    except Warning:
        response = {"ERROR:": "Could not find job with the specified uuid."}
        return jsonify(response), HTTPStatus.BAD_REQUEST


if __name__ == "__main__":
    app.run(debug=True)
