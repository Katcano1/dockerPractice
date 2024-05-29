import copy
from Queue import Queue


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
