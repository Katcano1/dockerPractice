"""
Instructions for running the Dockerized application
* Docker compose up -d
- creates a docker container and runs it in the background
* Docker attach <container name>
- attaches the terminal's input to the container
"""

import copy
from uuid import UUID


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        if len(job) != 3:
            print("Format is not correct.")
            return

            # checks if the priority is an integer
        try:
            job[2] = int(job[2])

            # this is a way of checking if the uuid entered is of the correct format
            # sample uuid: 550e8400-e29b-41d4-a716-446655440000
            try:
                uuid_test = UUID(job[0])
            except ValueError:
                print(
                    "UUID is not acceptable. Must be of the format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX."
                )
                return

            temp_enqueue = copy.deepcopy(self)

            for x in range(len(self.queue)):
                if job[2] < self.queue[x][2]:
                    temp_enqueue.queue.insert(x, job)
                    print("task added successfully")
                    return temp_enqueue

            temp_enqueue.queue.append(job)

            print("task added successfully")
            return temp_enqueue
        except ValueError:
            print("priority entered is not acceptable. Must be an integer.")
            return self

    def dequeue(self):
        # dequeues the element at the front unless the queue is empty
        return self.queue.pop(0)

    def peek(self):
        # returns the element at the front unless the queue is empty
        if not self.isEmpty():
            return self.queue[0]
        return

    def isEmpty(self):
        return len(self.queue) == 0

    def __str__(self):
        return "{}, {}, {}".format(self.queue[0][0], self.queue[0][1], self.queue[0][2])


def read_from_file(file_name, queue):
    try:  # try statement in order to catch a bad file name
        file = open(file_name)  # next 3 lines open, read, and then close the file
        lines = file.readlines()
        file.close()

        # mechanism for splitting each line of the file into a list with 3 elements.
        for line in lines:
            temp_list = line.split(",")
            # checks if the list has too many or too few elements
            queue = queue.enqueue(temp_list)

        print("Successfully read from " + file_name)

        return queue

    except FileNotFoundError:
        print("File not found.")
        return queue


if __name__ == "__main__":
    # I have 3 different sized files with jobs for testing purposes
    file_path = "jobs_small"
    q = Queue()
    q = read_from_file(file_path, q)

    print("-----------------------------")

    # my way of making the program interactive
    while True:

        request = input(
            "Type 'Enqueue' to add a job to the queue, 'Dequeue' to run a job, 'Status' to view the current queue "
            "and queue size, or 'Quit' to exit the program.\n"
        )

        if request.lower() == "enqueue":
            new_job = input(
                "Enter a job with the format 'UUID, Task name, priority (int)'"
            )

            temp_list = new_job.split(",")
            # if the length of the list of elements entered is not 3, then there are either too many or too few elements
            q = q.enqueue(temp_list)

        if request.lower() == "dequeue":
            # dequeues the front element and prints it out
            if not q.isEmpty():
                print("Running" + q.queue[0][1])
                q.dequeue()
                print("Successfully dequeued the first element.")
            else:
                print("Queue is empty.")

        if request.lower() == "status":
            # creates a copy of the queue, and then prints the size and full queue for reference.
            temp_queue = copy.deepcopy(q)
            for x in range(len(temp_queue.queue)):
                print(
                    "Job name:"
                    + temp_queue.queue[0][1]
                    + "   Priority: "
                    + str(temp_queue.queue[0][2])
                )
                temp_queue.dequeue()
            print("total size of queue: " + str(len(q.queue)))

        if request.lower() == "quit":
            break
