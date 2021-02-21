a_file = open("python.py", "r")

lines = a_file.readlines()
a_file.close()

new_file = open("spython.py", "w")
for line in lines:
    if line.strip("\n") != "ads via Carbon No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience. ADS VIA CARBON":

        new_file.write(line)

new_file.close()
