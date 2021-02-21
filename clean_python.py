a_file = open("python.py", "r")

lines = a_file.readlines()
a_file.close()

new_file = open("spython.py", "w")
for line in lines:
    if line.strip("\n") != "ads via Carbon":

        new_file.write(line)

new_file.close()
