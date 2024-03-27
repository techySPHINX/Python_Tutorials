# Python program to reverse first k elements of a queue using dequeue.
from collections import deque

def reverseFirstK(q, k):
	d = deque()

	# Dequeue the first k elements of the queue and push
	# them onto a deque
	for i in range(k):
		d.appendleft(q.popleft())

	# Pop the elements from the deque and enqueue them back
	# into the queue
	while d:
		q.append(d.popleft())

	# Dequeue the remaining elements from the queue and
	# enqueue them back into the queue
	for i in range(len(q) - k):
		q.append(q.popleft())

# Driver code.
q = deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.append(50)
q.append(60)
q.append(70)
q.append(80)
q.append(90)
q.append(100)

k = 5

# function call.
reverseFirstK(q, k)

print(*q)
