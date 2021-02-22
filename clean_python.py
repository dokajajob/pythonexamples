f = open("python.py", "r")
output = open("python_last.py", "w")

output.write(f.read().replace("ads via Carbon","").replace("No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience.","").replace("ADS VIA CARBON",""))
f.close()
#output.close()

