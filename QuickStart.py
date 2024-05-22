"""
Instructions for running the Dockerized application

"""

import copy
from uuid import UUID


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self):
        # dequeues the element at the front unless the queue is empty

        return self.queue.pop(0)

    def peek(self):
        # returns the element at the front unless the queue is empty
        if not self.isEmpty:
            return self.queue[0]
        return None

    def isEmpty(self):
        return len(self.queue) == 0

    def __str__(self):
        return "{}, {}, {}".format(self.queue[0][0], self.queue[0][1], self.queue[0][2])


def sorting_key(e):
    return e[2]


def read_from_file(file_name, queue):
    try:  # try statement in order to catch a bad file name
        file = open(file_name)  # next 3 lines open, read, and then close the file
        lines = file.readlines()
        file.close()

        value_errors = 0

        # mechanism for splitting each line of the file into a list with 3 elements.
        temp_job_list = []
        for line in lines:
            temp_list = line.split(",")
            # checks if the list has too many or too few elements
            if len(temp_list) != 3:
                continue
            try:  # try statement to catch a priority value that isn't an integer
                # converts the 'priority' element into an int for easy sorting
                temp_list[2] = int(temp_list[2])
                temp_job_list.append(temp_list)
            except ValueError:
                value_errors += 1
                continue

        # sorts the list according to the priority values (lowest first)
        temp_job_list.sort(key=sorting_key)

        for job in temp_job_list:
            queue.enqueue(job)  # enqueues the jobs into a queue object

        print("Successfully read from " + file_name)
        print("Number of Value errors: " + str(value_errors))

        return queue

    except FileNotFoundError:
        return queue


if __name__ == "__main__":
    file_path = "jobs_small"
    q = Queue()
    q = read_from_file(file_path, q)

    print("-----------------------------")

    # my way of making the program interactive
    while True:

        request = input(
            "Type 'Enqueue' to add a job to the queue, 'Dequeue' to remove a job, 'Status' to view the current queue "
            "and queue size, or 'Quit' to exit the program.\n"
        )

        if request.lower() == "enqueue":
            new_job = input(
                "Enter a job with the format 'UUID, Task name, priority (int)'"
            )

            temp_list = new_job.split(",")
            # if the length of the list of elements entered is not 3, then there are either too many or too few elements
            if len(temp_list) != 3:
                print("Format is not correct.")

                # checks if the priority is an integer
            try:
                temp_list[2] = int(temp_list[2])

                # this is a way of checking if the uuid entered is of the correct format
                try:
                    uuid_test = UUID(temp_list[0])
                except ValueError:
                    print(
                        "UUID is not acceptable. Must be of the format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX."
                    )
                    continue

                q.enqueue(temp_list)
                print("task added successfully")

            except ValueError:
                print("priority entered is not acceptable. Must be an integer.")

        if request.lower() == "dequeue":
            # dequeues the front element and prints it out
            print("Running" + q.queue[0][1])
            q.dequeue()
            print("Successfully dequeued the first element.")

        if request.lower() == "status":
            # creates a copy of the queue, and then prints the size and full queue for reference.
            temp_queue = copy.deepcopy(q)
            for x in range(len(temp_queue.queue)):
                print(temp_queue.queue[0][1])
                temp_queue.dequeue()
            print("total size of queue: " + str(len(q.queue)))

        if request.lower() == "quit":
            break
