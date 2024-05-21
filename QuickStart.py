
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self):
        if not self.isEmpty:
            return self.queue.pop(0)
        return

    def peek(self):
        if not self.isEmpty:
            return self.queue[0]
        return

    def isEmpty(self):
        return len(self.queue) == 0

    def __str__(self):
        return "{}, {}, {}".format(self.queue[0][0], self.queue[0][1], self.queue[0][2])


def sorting_key(e):
    return e[2]


def read_from_file(file_name, queue):
    try:
        file = open(file_name)
        lines = file.readlines()
        file.close()

        temp_job_list = []
        for line in lines:
            temp_list = line.split(",")
            if len(temp_list) != 3:
                continue
            try:
                temp_list[2] = int(temp_list[2])
                temp_job_list.append(temp_list)
            except ValueError:
                continue

        temp_job_list.sort(key=sorting_key)

        for job in temp_job_list:
            queue.enqueue(job)

        return queue

    except FileNotFoundError:
        return queue


if __name__ == '__main__':
    file_path = "jobs_small"
    q = Queue()
    q = read_from_file(file_path, q)

    for x in range(len(q.queue)):
        print("Running" + q.queue[x][1])
        q.dequeue()





