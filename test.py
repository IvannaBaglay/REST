from run import *
import requests

r=requests.get("http://127.0.0.1:5000/tasks")
data=r.json()
print(data)

print("\nrequsts.get")
s="20-12-2019"
r = requests.get("http://127.0.0.1:5000/tasks/" + s)
data = r.json()
print(data)

s="20-12-2019"
r = requests.get("http://127.0.0.1:5000/tasks/" + s)
data = r.json()
print(data)


print("\nrequsts.delete")
s="20-12-2019"
r = requests.delete("http://127.0.0.1:5000/tasks/" + s)
data = r.json()
print(data)

s="20-12-2019"
r = requests.delete("http://127.0.0.1:5000/tasks/" + s)
data = r.json()
print(data)

data= {
	"date": "20-12-2019",
	"temperature": -2,
	"precipitation": 19
}
headers = {'content-type': 'application/json'}
print("\nrequsts.post")
r = requests.post("http://127.0.0.1:5000/tasks",data=json.dumps(data), headers=headers)
data = r.json()
print(data)
data= {

	"temperature": 2,
	"precipitation": 19
}
print("\nrequsts.put")
s="20-12-2019"
r = requests.put("http://127.0.0.1:5000/tasks/"+s,data=json.dumps(data), headers=headers)
data = r.json()
print(data)




