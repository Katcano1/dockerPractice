from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from Queue import Queue
from QuickStart import read_from_file

file_path = "jobs_small"
q = Queue()
q = read_from_file(file_path, q)

app = Flask(__name__)
api = Api(app)

@app.route("/jobs", methods=["GET"])
def get_job():
    return jsonify(q.queue[0]), 200

@app.route("/jobs/<uuid>/<job_name>/<priority>", methods=["POST"])
def post_job(uuid, job_name, priority):
    # user_data = {
    #              "uuid": uuid,
    #              "name": "John Doe",
    #              "email": "john.doe@example.com"
    #          }
    new_job = [uuid, job_name, priority]
    q.enqueue(new_job)
    return jsonify(new_job), 201




if __name__ == "__main__":
    app.run(debug=True)