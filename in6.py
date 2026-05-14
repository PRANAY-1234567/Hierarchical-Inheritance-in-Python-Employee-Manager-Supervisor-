class Employee:
    def __init__(self):
        self.name = ""
        self.code = 0

    def set_data(self, name, code):
        self.name = name
        self.code = code

    def put_data(self):
        print("Name   :", self.name)
        print("Code   :", self.code)

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.teamsize = 0

    def set_data(self, name, code, teamsize):
        super().set_data(name, code)
        self.teamsize = teamsize

    def put_data(self):
        super().put_data()
        print("Team   :", self.teamsize)


class Supervisor(Employee):
    def __init__(self):
        super().__init__()
        self.discipline = ""

    def set_data(self, name, code, discipline):
        super().set_data(name, code)
        self.discipline = discipline

    def put_data(self):
        super().put_data()
        print("Discipline :", self.discipline)


class Inh6:
    @staticmethod
    def main():
        manager = Manager()
        supervisor = Supervisor()

        manager.set_data("Awez Sheikh", 423, 10)
        supervisor.set_data("Nabil Khan", 877, "Civil constr.")

        print("Manager details")
        print("------------------")
        manager.put_data()

        print("\nSupervisor details")
        print("------------------")
        supervisor.put_data()


# Calling main method
Inh6.main()
