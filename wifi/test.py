from subprocess import check_output

scanoutput = check_output(["iwlist","wlan0","scan"])

print "hi!"

for line in scanoutput.split():

    if line.startswith("ESSID"):
      line=line[7:-1]
      print line

