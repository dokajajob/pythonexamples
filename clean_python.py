f = open(home/dokaja/ed/pythonexamples/python.py, "r")
output = open(home/dokaja/ed/pythonexamples/python_last.py, "w")

output.write(f.read().replace("ds via Carbon","").replace("No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience.","").replace("ADS VIA CARBON"))
f.close()
output.close()