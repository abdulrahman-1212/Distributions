import math
import matplotlib.pyplot as plt


class Distribution:
    def __init__(self, mu, sigma):
        self.mean = mu
        self.stdev = sigma
        self.data = []
    
    def calculate_mean(self):
        return (self.data.sum() / len(self.data))
    
    def calculate_stdev(self, sample = True):
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        squared_diffs = [(i - self.mean)**2 for i in self.data]
        variance = sum(squared_diffs) / n
        self.stdev = math.sqrt(variance)
    

    def read_data(self, file_name, sample = True):
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list += int(line)
                file.readline()
        file.close()
        self.data = data_list
    
    def get_mean(self):
        return self.mean

    def get_stdev(self):
        return self.stdev






