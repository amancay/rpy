import itertools

sws_set = set([2,3,4,5,6,7,8]) - set([])
 
class SwsTup:
  def __init__(self,tup):
    self.tup = tup
  def sum(self):
    a = 0
    for e in self.tup:
      a += e
    return a

class SwsLine:
  def __init__(self,su):
    self.su = su
    self.tups = []
    self.ntups = 0
    self.tup_list = ''
  def add_tup(self, tu):
    self.tups.append(tu)
    self.ntups = len(self.tups)
  def list_tups(self):
    li = ''
    for tu in self.tups:
      li = li + ' ' + str(tu.tup)
    return li
sws_lines = []
for i in range(0,sum(sws_set) + 1):
	sws_lines.append(SwsLine(i))
	
for n in range(1,len(sws_set) + 1):
  for t in itertools.combinations(sws_set, n):
    st = SwsTup(t)
    st_sum = st.sum()
    sws_lines[st_sum].add_tup(st)

xa = []
ya = []

for li in sws_lines:
  print('sum: ',li.su,' part:',li.ntups)
  xa.append(li.su)
  ya.append(li.ntups)
  for tu in li.tups:
    print(list(tu.tup))
  print('---')

with open('/home/alejeng/test.html', 'w') as f:
  f.write('<table>')
  for li in sws_lines:
    f.write('<tr><td>'+str(li.su)+'</td><td>'+str(li.list_tups())+'</td><td>'+str(li.ntups)+'</td></tr>')
  f.write('</table>')

import webbrowser
new = 2 # open in a new tab, if possible

# open an HTML file on my own (Windows) computer
url = "file:///home/alejeng/test.html"
webbrowser.open(url,new=new)


import matplotlib.pyplot as plt

plt.plot(xa, ya)
plt.show()
