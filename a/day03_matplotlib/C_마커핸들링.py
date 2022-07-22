from matplotlib import markers
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np

yp = np.array([2,8,1,9,5,7])

#print(Line2D.markers.items())

plt.plot(yp,'ro--')                              # 빨간 동그라미 + 점선

plt.plot(yp,'ro--',ms=30)                         # 빨간 동그라미 + 점선 + 마커크기 30

plt.plot(yp,'ro--',ms=30, mec= 'b' )              # 빨간 동그라미 + 점선 +  마커크기 30 + 마커 엣지 블루

plt.plot(yp,'ro--',ms=30, mec= 'b' , mfc= 'y')     # 빨간 동그라미 + 점선 +  마커크기 30 + 마커 엣지 블루 + 마커 (페이스)내용 옐로우


plt.show()

from matplotlib import markers
plt.plot(yp, 'o-.', ms=25, mec='#23db98', mfc='#eb15cb') # colorpicker

# https://codetorial.net/matplotlib/set_marker.html