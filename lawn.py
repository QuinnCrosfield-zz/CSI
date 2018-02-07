#f5 to run
speed = 2
ratio = 7/15

def timeToMow(depth, width):
    time = (depth * width) / speed  / 3600 
    return time


def roundedTimeToMow(depth):
   roundedTime = (timeToMow(depth, depth/ratio))
   return roundedTime

def roundedTimeToMowTable():
   print("Depth  Time")
   for x in range(100, 200, 10):
       depth = x
       print(str(depth) + "    " + str(roundedTimeToMow(depth)))
