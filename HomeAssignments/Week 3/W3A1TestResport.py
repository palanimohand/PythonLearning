import numpy as np

class TestReport:

    execution_times = None

    def __init__(self, array):
        self.execution_times = array

    def average_time(self):
        print(np.mean(self.execution_times))
        return np.sum(self.execution_times)/len(self.execution_times)

    def max_time(self):
        return self.execution_times.max()

class RegressionReport(TestReport):

    def __init__(self,array):
        super().__init__(array)

    def slow_tests(self, threshold):
        slow_test = []
        for e_time in self.execution_times:
            # print(e_time)
            # print(type(e_time))
            if e_time > threshold :
                slow_test.append(e_time)
        return slow_test
    
    def slow_tests_filter(self, threshold):
        x = lambda a : a if a > threshold else None
        return list(filter(x, self.execution_times))
    
    def where_slow_tests(self, threshold):
        return np.where(self.execution_times > threshold)

if __name__ == "__main__":

# with constructor
    cons_regression = RegressionReport(np.array([1,5,3,2,10,1,9,11,30,12]))
    print(cons_regression.average_time())
    print(cons_regression.max_time())
    print(cons_regression.slow_tests(10))
    print(cons_regression.where_slow_tests(10))
    print(cons_regression.slow_tests_filter(10))
    a = cons_regression.execution_times
    condition = a>10
    # condition = [True,False,True,False,True,False,True] # Gives Error as the condition did not match the array size
    # filter1 = a[0] > 10 # Trying multiple conditions for a single array
    # filter2 = a[1] > 5
    # filter3 = a[2] % 2 == 0
    # filter4 = a[3] == 2
    # filter5 = a[4] < 15
    # filter6 = a[5] != 1
    # filter7 = a[6] >= 9
    # filter8 = a[7] < 20
    # filter9 = a[8] == 30
    # filter10 = a[9] > 0
    # condition = [filter1, filter2, filter3, filter4, filter5, filter6, filter7, filter8, filter9, filter10]
    print(a[condition])
    
 
# without constructor
    """
    regression = RegressionReport()
    regression_execution_times = np.array([1,5,3,2,10,1,9,11,30,12])
    regression.execution_times = regression_execution_times
    print(type(regression_execution_times))
    print(regression.average_time())
    print(regression.max_time())
    print(regression.slow_tests(10))
    print(regression.where_slow_tests(10))
    print(regression.slow_tests_filter(10))
    print([e_time for e_time in regression.execution_times if e_time > 10])
    """
    