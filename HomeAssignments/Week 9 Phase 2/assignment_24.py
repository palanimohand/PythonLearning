import pandas as pd

class TestCase:

    def __init__(self, test_id, test_name, module, status="Not Executed"):
        self.test_id = test_id
        self.test_name = test_name
        self.module = module
        self.status = status

    def execute_test(self, result):
        self.status = result

    def display_test_case(self):
        print(self.test_id, self.test_name, self.module, self.status)

    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status]

class AutomatedTestCase(TestCase):

    def __init__(self, test_id, test_name, module, automation_tool, status="Not Executed"):
        self.automation_tool = automation_tool
        super().__init__(test_id, test_name, module, status)

    def display_test_case(self):
        print(self.test_id, self.test_name, self.module, self.status, self.automation_tool)

    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status, self.automation_tool]

class TestSuite:

    test_cases = []

    def __init__(self, suite_name):
        self.suite_name = suite_name

    def add_test(self, test_case:TestCase):
        self.test_cases.append(test_case)

    def run_all_tests(self):
        for test_case in self.test_cases:
            test_case.status = input(f"Enter Status for {test_case.test_id}: ")

    def save_results_to_csv(self, file_name):
        columns = ["Test ID", "Test Name", "Module", "Status", "Automation Tool"]
        rows = [test_case.to_csv_row() for test_case in self.test_cases]
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv(file_name)

    def summary_report(self):
         for test_case in self.test_cases:
            test_case.display_test_case()


if __name__ == "__main__":
    
    print("Happy")
    test_case_1 = TestCase("Test_ID1", "Manual_Test_1", "Payments")
    test_case_2 = TestCase("Test_ID2", "Manual_Test_2", "Payments")
    test_case_3 = AutomatedTestCase("Test_ID3", "Automation_Test_1", "Payments", "Playwright")
    test_case_4 = AutomatedTestCase("Test_ID4", "Automation_Test_2", "Payments", "Playwright")
    my_test_suite = TestSuite("Payments_Test_Suite")
    my_test_suite.add_test(test_case_1)
    print(my_test_suite.test_cases)
    my_test_suite.add_test(test_case_2)
    print(my_test_suite.test_cases)
    my_test_suite.add_test(test_case_3)
    print(my_test_suite.test_cases)
    my_test_suite.add_test(test_case_4)
    print(my_test_suite.test_cases)
    my_test_suite.run_all_tests()
    my_test_suite.save_results_to_csv(r"HomeAssignments\Week 9 Phase 2\Output.csv")
    my_test_suite.summary_report()
