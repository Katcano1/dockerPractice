"""
Instructions for running the Dockerized application

"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self):
        # dequeues the element at the front unless the queue is empty
        if not self.isEmpty:
            return self.queue.pop(0)
        return

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

    print("Printing queue to terminal...")
    print("-----------------------------")
    for x in range(len(q.queue)):
        print("Running" + q.queue[x][1])
        q.dequeue()
