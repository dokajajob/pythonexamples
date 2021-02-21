f = open("python.py", "r")
output = open("python_last.py", "w")

output.write(f.read().replace("ds via Carbon",""))
f.close()
output.close()