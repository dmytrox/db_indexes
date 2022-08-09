import pymysql
import filldb 
import time

db = pymysql.connect(host='localhost', user='root', passwd='Qwerty123', db='indexes')
cursor = db.cursor()


start = int(round(time.time() * 1000))

x = 20000
while(x > 0):
    x -= 1
    filldb.insert(cursor)
db.commit()

end = int(round(time.time() * 1000))

result = end - start

print("Time Elapsed", result)