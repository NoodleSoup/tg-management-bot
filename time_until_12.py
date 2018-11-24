from time import gmtime, strftime
a = strftime("%Y-%m-%d %H:%M:%S", gmtime())
time = (a.split(" ",1)[1].split(":",2))
totaltime = int(time[0])*3600+int(time[1])*60+int(time[2])+5*3600+30*60 
totaltime = 86400 - totaltime
print(totaltime)
