from main.py import Distribution
import math
import matplotlib.pyplot as plt


class Binomial(Distribution):
    def __init__(self, p = 0, n = 1):
        Distribution.__init__(self)
        self.p = p
        self.n = n
    
    def calculate_mean(self):
        self.mean = self.p * self.n
        return self.mean
    
    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
    
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object."""
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n
    

    def plot_bar(self):

        plt.bar(self.data)
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
        n_f = math.factorial(self.n)
        k_f = math.factorial(k)
        nk_f = math.factorial(self.n-k)
        return (n_f/(k_f * nk_f)) * (self.p**k) * ((1-self.p)**(self.n-k))
    
    def plot_bar_pdf(self):
        
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        # calculate the x values to visualize
        for k in range(self.n + 1):
            x.append(k)
            y.append(self.pdf(k))
            
		# make the plots
        plt.bar(x,y)
        plt.title('Probability of Outcomes')
        plt.xlabel('probability')
        plt.ylabel('count')
        
        return x, y

    def __add__(self, other):
        try:
            assert self.p == other.p, 'p values are not equal'
        except:
            raise AssertionError
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        return result


    def __repr__(self):    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)


