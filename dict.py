###using del
d={1:20,2:30,"s":40}
del(d["s"])
print(d)
###clear()
d={1:20,2:30,"s":40}
d.clear()
print(d)
###del
d={1:20,2:30,"s":40}
del d
print(d)
###keys()
d={1:20,2:30,"s":40}
print(d.keys())
###values()
d={1:20,2:30,"s":40}
print(d.values())
##both keys and values it can use "items"
d={1:20,2:30,"s":40}    
s=d.items()
print(s)

d={1:20,2:30,"s":40}    
print(d.items())
###key values
d={1:20,2:30,"s":40}
for i in d:
    print(i)
###keys()
d={1:20,2:30,"s":40}
for k in d.keys():
    print(k)
###values()
d={1:20,2:30,"s":40}
for v in d.values():
    print(v)
###items it can both keys and values
d={1:20,2:30,"s":40}
for i in d.items():
    print(i)                                                        
##sum
d={"r":20,"i":30,"h":70,"a":80}
s=0
for v in d.values():
    s=s+v
print(s)

d={"r":20,"i":30,"h":70,"a":80}
s=""
for k in d.keys():
    s=s+k
print(s)

d={"r":"s","i":"p","h":"l","a":"d"}
s=""
for v in d.values():
    s=s+v
print(s)
for v in d.values():
    s=s+v
print(S)
