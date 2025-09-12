class Bug_Tracker:

    bugs = {}

    def add_bug(self, bug_id, description, severity):
        new_bug = {bug_id : {"description": description, "severity": severity, "status": "Open"}}
        self.bugs.update(new_bug)

    def update_status(self, bug_id, new_status):
        # update_bug = {bug_id : {"status": new_status}}
        self.bugs[bug_id]["status"] = new_status

    def list_all_bugs(self):
        return self.bugs

if __name__ == "__main__":

    my_bug_tracker = Bug_Tracker()
    my_bug_tracker.add_bug("Test1", "Description1", "Severity1")
    my_bug_tracker.add_bug("Test2", "Description2", "Severity2")
    my_bug_tracker.add_bug("Test3", "Description3", "Severity3")
    my_bug_tracker.update_status("Test2", "In Progress")
    my_bug_tracker.update_status("Test3", "Closed")
    print(my_bug_tracker.list_all_bugs())

