
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import sys

if __name__ == "__main__":

	if '-n' in sys.argv:
		p = sys.argv.index('-n')
		samples = int(sys.argv[p+1])
	else:
		samples = 10

	sns.histplot(random.normal(loc=50, scale=5, size=samples), element = 'step', label='normal', color = 'aqua')
	sns.histplot(random.binomial(n=100, p=0.5, size=samples),element = 'step', label='binomial', color = 'salmon')
	plt.legend()
	plt.show() 
