import time as t

time_now = t.localtime()

print(t.localtime())

#suppose we have to represent a transaction
print("Transaction completed at " + str(time_now.tm_hour) + "h" , str(time_now.tm_min) + "min")

print(t.time())

t.sleep(5)

print(t.time())

time_now = t.time()
print(time_now)

delivery_time = time_now + (84600 * 7)
print(t.localtime(delivery_time))
print("Delivery expected" + str(t.localtime(delivery_time).tm_mday) + str(t.localtime(delivery_time).tm_mon))

