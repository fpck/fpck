import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.plot([3, 1, 4, 1, 5], 'ks-', mec='w', mew=5, ms=20)
plt.savefig('/data/aaaa.png')
