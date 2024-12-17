## This code belongs to Johan Nunez and Mohammed Mirza

class Doctor:
    def __init__(self, doctor_id, name, specialization, timing, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id:<5} {self.name:<20} {self.specialization:<15} {self.timing:<15} {self.qualification:<15} {self.room_number:<10}"


class Patient:
    def __init__(self, patient_id, name, disease, gender age):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.patient_id:<5} {self.name:<20} {self.disease:<15} {self.gender:<10} {self.age:<5}"


doctors_list = []
patients_list = []


def addDoctor():
    doctor_id = input("Enter the doctor's ID: ")
    name = input("Enter the doctor's name: ")
    specialization = input("Enter the doctor's specility: ")
    timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qualification = input("Enter the doctor's qualification: ")
    room_number = input("Enter the doctor's room number: ")

    doctors_list.append(Doctor(doctor_id, name, specialization, timing, qualification, room_number))
    print(f"\nDoctor whose ID is {doctor_id} has been added\n")


def displayDoctors():
    print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
    for doctor in doctors_list:
        print(doctor)


def searchDoctorByID():
    search_id = input("Enter the doctor Id: ")
    found = False
    for doctor in doctors_list:
        if doctor.doctor_id == search_id:
            print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
            print(doctor)
            found = True
    if not found:
        print("Can't find the doctor with the same ID on the system\n")


def addPatient():
    patient_id = input("Enter Patient id: ")
    name = input("Enter Patient name: ")
    disease = input("Enter Patient disease: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")

    patients_list.append(Patient(patient_id, name, disease, gender, age))
    print(f"\nPatient whose ID is {patient_id} has been added.\n")


def displayPatients():
    print("\nID   Name                   Disease         Gender          Age")
    for patient in patients_list:
        print(patient)


def searchPatientByID():
    search_id = input("Enter the Patient Id: ")
    found = False
    for patient in patients_list:
        if patient.patient_id == search_id:
            print("\nID   Name                   Disease         Gender          Age")
            print(patient)
            found = True
    if not found:
        print("Can't find the Patient with the same id on the system\n")


def main():
    print("Welcome to Alberta Hospital (AH) Management system")

    menu_option = 0
    while menu_option != 3:
        print("\nSelect from the following options, or select 3 to stop:")
        print("1 - \tDoctors\n2 - \tPatients\n3 -\tExit Program")
        menu_option = int(input(">>> "))

        if menu_option == 1:
            doctors_menu = 0
            while doctors_menu != 6:
                print("\nDoctors Menu:")
                print("1 - Display Doctors list")
                print("2 - Search for doctor by ID")
                print("3 - Search for doctor by name")
                print("4 - Add doctor")
                print("5 - Edit doctor info")
                print("6 - Back to the Main Menu")
                doctors_menu = int(input(">>> "))

                if doctors_menu == 1:
                    displayDoctors()
                elif doctors_menu == 2:
                    searchDoctorByID()
                elif doctors_menu == 4:
                    addDoctor()
                elif doctors_menu == 6:
                    print("Returning to the Main Menu...")

        elif menu_option == 2:
            patients_menu = 0
            while patients_menu != 5:
                print("\nPatients Menu:")
                print("1 - Display patients list")
                print("2 - Search for patient by ID")
                print("3 - Add patient")
                print("4 - Edit patient info")
                print("5 - Back to the Main Menu")
                patients_menu = int(input(">>> "))

                if patients_menu == 1:
                    displayPatients()
                elif patients_menu == 2:
                    searchPatientByID()
                elif patients_menu == 3:
                    addPatient()
                elif patients_menu == 5:
                    print("Returning to the Main Menu...")
        elif menu_option == 3:
            print("Thanks for using the program. Bye!")
main()
