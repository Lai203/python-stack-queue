from collections import deque

queue = deque([1,2,3,4,5])
print ("Antrian Sekarang : ", queue)

queue.append(6)
print ("Antrian Masuk : ", 6)
print ("Antrian Sekarang : ", queue)

queue.append(7)
print ("Antrian Masuk : ", 7)
print ("Antrian Sekarang : ", queue)

out = queue.popleft()
print ("Antrian Keluar : ", out)
print ("Antrian Sekarang : ", queue)