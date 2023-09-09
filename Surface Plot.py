import matplotlib.pyplot as pl
import numpy as np
(Xg,Yg,Tg) = np.meshgrid(x,y,t)
ax = pl.axes(projection = "3d")
surf1 = ax.plot_surface(Xg[:,:,5],Yg[:,:,5],Tg[:,:,5])
pl.show()