class Patient:
    """Master class"""
    def __init__(self,  name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.expected_cost = 1000

    def discharge(self):
        print(self.name, "Emergency Patient")


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.expected_cost = 2000

    def discharge(self):
        print(self.name, "Hospital Patient")


class Hospital:

    def __init__(self):
        self.cost = 0
        self.patients = []  # brackets create empty list

    def admit(self, patients):
        self.patients.append(patients)  # continuously admitting patients

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.expected_cost

    def get_total_cost(self):
        return self.cost


# patients
P1 = HospitalizedPatient("P1")
P2 = HospitalizedPatient("P2")
P3 = EmergencyPatient("P3")
P4 = EmergencyPatient("P4")  # change for emergency vs admit
P5 = EmergencyPatient("P5")

# make hospital
YNHH = Hospital()  # empty hospital

YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)

YNHH.discharge_all()

print(YNHH.get_total_cost())

