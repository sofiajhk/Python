class Patient(object):
    pat_count = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_num = None 
        self.id = Patient.pat_count

        Patient.pat_count += 1
    def display_info(self):
        print "Patient ID: {} \nBed Number: {} \nName: {} \nAllergies: {}".format(self.id, self.bed_num, self.name, self.allergies)
        return self


class Hospital(object):
    def __init__(self, hospital, capacity):
        self.hospital = hospital
        self.capacity = capacity
        self.patients = []
        self.bed = 0
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "We apologize, {}, but our hospital is at capacity!".format(patient.name)
        else:
            self.patients.append(patient)
            self.bed += 1
            patient.bed_num = self.bed
        return self
    def discharge(self, patient):
        for pat in self.patients:
            if pat == patient:
                self.patients.pop(self.patients.index(patient))
                patient.bed_num = None
                print "{}, congrats you're all better and can be discharged!".format(patient.name)
                break
        else:
            print "This patient is not in our records!"
        return self
    def info(self):
        print self.hospital, "currently holds the following patients" 
        for patient in self.patients:
            print patient.display_info()
        


patient1 = Patient("Cindy", "peanuts")
patient2 = Patient("Alex", "gluten")
patient3 = Patient("David", "none")
patient4 = Patient("Alison", "eggs")
patient5 = Patient("Harry", "none")

# patient1.display_info()
# patient2.display_info()
# patient3.display_info()

hospital1 = Hospital("Mercy Hospital", 4)
hospital2 = Hospital("St.Johns Hospital", 10)

hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).discharge(patient1).discharge(patient5).info()
