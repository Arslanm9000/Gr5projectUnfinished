''''This code belongs to Johan Nunez and Mohammed Mirza in CPRG 216-G
Date: December 16, 2024. This code is unfinished, but we are submitting 
what we accomplished hoping to get some grades. Kind Regards: Johan and Mohammed 
   '''

# This program is for managing doctors and patients at a hospital

#Class Doctor with the constructor and its attributes 
class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", timing="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id:<5} {self.name:<20} {self.specialization:<15} {self.timing:<15} {self.qualification:<15} {self.room_number:<10}"

#Class Patient with the constructor and its attributes 
class Patient:
    def __init__(self, patient_id="", name="", disease="", gender="", age=""):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):    # Attempted to do return string for patient information 
        return f"{self.patient_id:<5} {self.name:<20} {self.disease:<15} {self.gender:<10} {self.age:<5}"


doctors_list = []
patients_list = []

#User is prompted to enter a doctor into the list 
def addDoctor():
    doctor_id = input("Enter the doctor's ID: ")
    name = input("Enter the doctor's name: ")
    specialization = input("Enter the doctor's specility: ")
    timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qualification = input("Enter the doctor's qualification: ")
    room_number = input("Enter the doctor's room number: ")

    doctors_list.append(Doctor(doctor_id, name, specialization, timing, qualification, room_number))
    print(f"\nDoctor whose ID is {doctor_id} has been added\n")
'''Add a new doctor with multiple inputs such as ID, name, specilization etc.
      and then update the list of doctors. 
'''
#Displays current doctors in the list if its update otherwise will be empty 
def displayDoctors():
    print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
    for doctor in doctors_list:
        print(doctor)

#Search doctor by ID function includes finding if the doctor ID is in the updated list 
def searchDoctorByID():
    search_id = input("Enter the doctor Id: ")
    for doctor in doctors_list:
        if doctor.doctor_id == search_id:
            print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
            print(doctor)     
        else:
            print("Can't find the doctor with the same ID on the system\n")

# Add Patient which will added to the empty list 
def addPatient():
    patient_id = input("Enter Patient id: ")
    name = input("Enter Patient name: ")
    disease = input("Enter Patient disease: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")

    patients_list.append(Patient(patient_id, name, disease, gender, age))
    print(f"\nPatient whose ID is {patient_id} has been added.\n")

#Patient display function, which will display whatever you added in the addpatient() function. 
def displayPatients():
    print("\nID   Name                   Disease         Gender          Age")
    for patient in patients_list:
        print(patient)

#Search patient ID, using a for loop to identify if patient is in the list 
def searchPatientByID():
    search_id = input("Enter the Patient Id: ")
    for patient in patients_list:
        if patient.patient_id == search_id:
            print("\nID   Name                   Disease         Gender          Age")
            print(patient)
        else:
            print("Can't find the Patient with the same id on the system\n")

#Main Function that displays Alberta Hospital Mangement system,calls upon the main menu, which the user will choose between 6 options. 
def main():
    print("Welcome to Alberta Hospital (AH) Management system")

    menu_option = 0
    while menu_option != 3:
        print("\nSelect from the following options, or select 3 to stop:")
        print("1 - \tDoctors\n2 - \tPatients\n3 -\tExit Program")
        menu_option = int(input(">>> "))

        if menu_option == 1:       # If statement for searching the menu 
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

                if doctors_menu == 1: #Input 1 will display the current list of doctors, however it will be empty if you click it first, it needs to be updated. 
                    displayDoctors()   
                elif doctors_menu == 2:  #If you are searching a doctor by their ID, it will display what you have updated in the list 
                    searchDoctorByID()
                elif doctors_menu == 4:  #Here you add the doctor to the empty list 
                    addDoctor()
                elif doctors_menu == 6:   #Return to Main Menu 
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

                if patients_menu == 1:# If input is 1, then you will use the display patients function, however in order for this to happen, it needs to be updated with patients
                    displayPatients() 
                elif patients_menu == 2: #If you are searching for an ID after the list is updated, it will display the patient info 
                    searchPatientByID()
                elif patients_menu == 3:  #Here you want to add a patient to the empty list 
                    addPatient()
                elif patients_menu == 5:   #Here you return to the main menu and click something new. 
                    print("Returning to the Main Menu...")
        elif menu_option == 3:    #Exit 
            print("Thanks for using the program. Bye!")
main()