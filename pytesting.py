import json

import app
import pytest


def test_get_method():
    flask_app = app.app
    flask_app.config.update({
        "TESTING": True
    })

    response = flask_app.test_client().get('/jobs')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '["5cb139e2-2344-4ede-aa4c-4ec1e940ab28","Task 2",1,1]\n'


def test_get_status_method():
    flask_app = app.app
    flask_app.config.update({
        "TESTING": True
    })

    response = flask_app.test_client().get('/jobs/status')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == ('[{"Job:":["5cb139e2-2344-4ede-aa4c-4ec1e940ab28","Task 2",1,1],'
                                             '"Position:":0},{"Job:":["8b0f47f2-a833-4f12-bc9e-096e49c015ad",'
                                             '"Task 3",2,4],"Position:":1},{"Job:":['
                                             '"b0293ea7-f8bc-4c3a-af5e-9b1d858ed18a","Task 1",3,2],"Position:":2}]\n')


def test_post_method():
    flask_app = app.app
    flask_app.config.update({
        "TESTING": True
    })
    data = {"uuid": "uuid_tester", "job_name": "new job", "priority": "0", "execution_time": "1"}
    response = flask_app.test_client().post('/jobs', data=json.dumps(data))
    assert response.status_code == 201
    assert response.data.decode('utf-8') == ('{"execution_time":"1","job_name":"new job","priority":"0",'
                                             '"uuid":"uuid_tester"}\n')


def test_dequeue_method():
    flask_app = app.app
    flask_app.config.update({
        "TESTING": True
    })

    response = flask_app.test_client().delete('/jobs')

    assert response.status_code == 202
    assert response.data.decode('utf-8') == '{"Response:":"successfully executed new job Time taken: 1 seconds."}\n'


def test_dequeue_by_uuid_method():
    flask_app = app.app
    flask_app.config.update({
        "TESTING": True
    })

    response = flask_app.test_client().delete('/jobs/b0293ea7-f8bc-4c3a-af5e-9b1d858ed18a')

    assert response.status_code == 202
    assert response.data.decode('utf-8') == ('{"Response:":"successfully executed Task 1 with uuid '
                                             'b0293ea7-f8bc-4c3a-af5e-9b1d858ed18a. Time taken: 2 seconds"}\n')


