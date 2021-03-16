# write a python program to convert seconds to day,hour,minutes and seconds.

seconds=int(input("enter the value for seconds:"))
day=(((seconds//60)//60)//24)
print(f"total day for given seconds:{day}")
hour=((seconds//60//60))
print(f"total hours for given seconds:{hour}")
minute=(seconds//60)
print(f"total minute for given seconds:{minute}")