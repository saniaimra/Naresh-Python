class Patient:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age 
        self.history = []

    def get_id(self):
        return self.id


    def get_name(self):
        return self.name


    def get_age(self):
        return self.age


    def get_history(self):
        return self.history


    def add_history(self, record):
        self.history.append(record)

class Doctor:
    def __init__(self,name,specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def get_name(self):
        return self.name


    def get_specialization(self):
        return self.specialization


    def get_appointments(self):
        return self.appointments
    def add_appointment(self, appointment):
        self.appointments.append(appointment)

class Appointment:


    def __init__(self,id, patient, doctor, date):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.patient_id_counter = 1
        self.appointment_id_counter = 1

    def add_patient(self, name, age):
        patient = Patient(self.patient_id_counter, name, age)
        self.patients.append(patient)
        self.patient_id_counter += 1
        return patient
    
    def add_doctor(self,name,specialization):
        doctor = Doctor(name,specialization)
        self.doctors.append(doctor)
        return doctor
    
    def schedule_appointment(self, patient, doctor, date):
        appointment = Appointment(self.appointment_id_counter, patient, doctor, date)
        self.appointments.append(appointment)
        doctor.add_appointment(appointment)
        patient.add_history(f"Appointment with Dr.{doctor.get_name()} on {date}")
        self.appointment_id_counter += 1
        return appointment
    
    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.get_id() == patient_id:
                return patient
        return None
    
    def generate_report(self):
        return {
            "Total Patients": len(self.patients),
            "Total Doctors": len(self.doctors),
            "Total Appointments": len(self.appointments)
        }
''' 

hospital = Hospital("City Hospital")

p1 = hospital.add_patient("Alice", 30)
d1 = hospital.add_doctor("Dr. Smith", "Cardiologist")

a1 = hospital.schedule_appointment(p1, d1, "2025-10-05")
print()
print("Report:", hospital.generate_report())
'''    
if __name__ == "__main__":
    hospital = Hospital("City Hospital")

    # Add patients
    p1 = hospital.add_patient("Alice", 30)
    p2 = hospital.add_patient("Bob", 40)

    # Add doctors
    d1 = hospital.add_doctor("Dr. Smith", "Cardiologist")
    d2 = hospital.add_doctor("Dr. Brown", "Dermatologist")

    # Schedule appointments
    a1 = hospital.schedule_appointment(p1, d1, "2025-10-05")
    a2 = hospital.schedule_appointment(p2, d2, "2025-10-06")

    # View patient history
    print("Patient History:", p1.get_history())

    # View doctor schedule
    print("Doctor Schedule for Dr. Smith:")
    for app in d1.get_appointments():
        print(f"Appointment ID {app.id} with {app.patient.get_name()} on {app.date}")

    # Search patient
    found = hospital.search_patient(1)
    print("Searched Patient:", found.get_name() if found else "Not Found")

    # Generate report
    print("Hospital Report:", hospital.generate_report())   
    

