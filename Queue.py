import copy
import time
from uuid import UUID


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        if len(job) != 4:
            print("Format is not correct.")
            return

            # checks if the priority is an integer
        try:
            job[2] = int(job[2])
            job[3] = int(job[3])

            for x in range(len(self.queue)):
                if job[2] < self.queue[x][2]:
                    self.queue.insert(x, job)
                    print("task added successfully")
                    return

            self.queue.append(job)

            print("task added successfully")
        except ValueError:
            raise ValueError

    def get_job_by_uuid(self, uuid):
        for x in range(len(self.queue)):
            if uuid == self.queue[x][0]:
                return self.queue[x]

    def delete_by_uuid(self, uuid):
        """
        Deletes the first object with the specified uuid
        :return:
        """
        for x in range(len(self.queue)):
            if uuid == self.queue[x][0]:
                self.queue.pop(x)
                return

        raise Warning

    def dequeue(self):
        """
        Dequeues the element at the front unless the queue is empty
        :return:
        """

        return self.queue.pop(0)

    def peek(self):
        # returns the element at the front unless the queue is empty
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return "{}, {}, {}".format(self.queue[0][0], self.queue[0][1], self.queue[0][2])
