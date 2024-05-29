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
            # try:
            #     uuid_test = UUID(job[0])
            # except ValueError:
            #     print(
            #         "UUID is not acceptable. Must be of the format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX."
            #     )
            #     return

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
