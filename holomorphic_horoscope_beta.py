## 12.08.2024 funny functions
import numpy as np
import complexplorer as cx
import matplotlib.pyplot as plt
import re
import os.path

##
a = int(input('Tag eingeben:'))
b = int(input('Monat eingeben:'))
c = int(input('Jahr eingeben:'))
#
h = float(input('Ausschnitt horizontal:'))
v = float(input('Ausschnitt vertikal:'))
##
func = lambda z: a*np.log(z**b)/c
## plot
plt.rcParams["figure.figsize"] = (4, 4) 
domain = cx.Rectangle(7, 7) ## h v
cx.plot(domain, func)
plt.show()

