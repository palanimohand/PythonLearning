import numpy as np

class ManualTester:

    def analyze(self, data):
        print(data)
        return data[:5]

class AutomationTester(ManualTester):

    def analyze(self, data):
        print(data)
        return data.min()

class PerformanceTester(AutomationTester):

    def analyze(self, data):
        print(data)
        return np.percentile(data, 95)
    
def show_analysis(tester, data):
    return tester.analyze(data)

if __name__ == "__main__":

    mt = ManualTester()
    print(show_analysis(mt, np.array([1,4,10,11,15,20,22,53,22,55,50,14])))
    mt = AutomationTester()
    print(show_analysis(mt, np.array([1,4,10,11,15,20,22,53,22,55,2,3])))
    mt = PerformanceTester()
    print(show_analysis(mt, np.array([1,4,10,11,15,20,22,53,22,50,2,3])))