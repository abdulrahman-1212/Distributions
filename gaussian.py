from main.py import Distribution
import math
import matplotlib.pyplot as plt


class Gaussian(Distribution):
    def __init__(self, mu = 0, sigma = 1):
        Distribution.__init__(mu, sigma)
    
    
    

    def plot_hist(self):
        plt.hist(self.data)
        plt.x_label('data')
        plt.y_label('count')
        plt.title('Histogram of the data')
    

    def pdf(self, n_spaces):
        min_val = min(self.data)
        max_val = max(self.data)

        interval = (max_val - min_val) / n_spaces

        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_val + interval + i
            x.append(tmp)
            y.append(self.pdf(tmp))
        
            fig, axes = plt.subplots(2,sharex=True)
            fig.subplots_adjust(hspace=.5)
            axes[0].hist(self.data, density=True)
            axes[0].set_title('Normed Histogram of Data')
            axes[0].set_ylabel('Density')

            axes[1].plot(x, y)
            axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
            axes[0].set_ylabel('Density')
            plt.show()

            return x, y


    
    
    def __add__(self, gaus):
        result = Gaussian()
        result.mean = self.get_mean() + gaus.get_mean()
        result.stdev = math.sqrt(self.get_stdev() ** 2 + gaus.get_stdev() ** 2)
        return result
    
    def __repr__(self):
        return 'mean {}, standard deviation {}'.format(self.mean, self.stdev)
