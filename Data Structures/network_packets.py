# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def process(self, request):
        while self.finish_time_:
            if self.finish_time_[0] <= request.arrival_time:
                self.finish_time_.pop(0)
            else:
                break
        if len(self.finish_time_) == self.size:
            return Response(True, -1)
        if not self.finish_time_:
            self.finish_time_ = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)
        last_element = self.finish_time[-1]
        self.finish_time_.append(last_element + request.process_time)
        return Response(False, last_element)



def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()