celebsBiographyFile = open("celebs-biography.txt", "r")
celebsBodyFile = open("celebs-measurements.txt", "w+")
lines = celebsBiographyFile.readlines()
name = ""
measurments = ""
corruptedCount = 0
for line in lines:
    line = line.strip()
    if line[0:3] == "$$$":
        name = line[4:]
    elif line[0:21] == "Measurements (inches)":
        measurments = (line[26:])[:-2]
        if '--' not in measurments:
            celebsBodyFile.write(name + " " + measurments + "\n")
        else:
            corruptedCount +=1
            print("corrupted #" + str(corruptedCount) + " measurments for: " + name)
