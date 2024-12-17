"""
Part 2: Patients Management

This part includes the `Patient` class, `Manager` base class, `PatientManager` class, 
and the functionality for managing patient records, including displaying, searching, 
adding, and editing patients. 
"""

# ========== Patient Class ==========
class Patient:
    """
    Represents a patient.
    Attributes:
    - patient_id: Attribute for the patient.
    - name: Name of the patient.
    - Disease: Patient's illness or condition.
    - Gender: Gender of the patient.
    - Age: Age of the patient.
    """
    def __init__(self, patient_id, name, disease, gender, age):  # Constructor for patient class 
        self.__patient_id=patient_id
        self.__name=name
        self.__disease=disease
        self.__gender=gender
        self.__age = age
        self.__name=name
        self.__disease=disease
        self.__gender=gender

        
        
       
    '''patient setter and getter variables'''
    
    def get_PatientID(self):    
       return self.__patient_id
    def set_PatientID(self,patient_id):   
       self.__patient_id=patient_id
    def get_name(self):   
       return self.__name
    def set_name(self,name):
       self.__name=name
    def get_disease(self):
       return self.__disease
    def set_disease(self,disease):  
       self.__disease=disease
    def get_age(self):
       return self.__age
    def set_(self,age):
       self.__age=age
    def get_gender(self):
       return self.__gender
    def set_gender(self,gender):
       self.__gender=gender




    def __str__(self):
        """
        Returns a formatted string representation of the patient's details.
        """
        return (
            f"{self.__patient_id:<5} {self.__name:<20} {self.__disease:<15} "
            f"{self.__gender:<10} {self.__age:<5}"
        )


userinput=int(input('''Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu
>>> 1'''))

while userinput<5:
   if userinput==1:
       patientMenu = open('patients.txt', 'r')
       for sentence in patientMenu:
        sentence = sentence.replace("_", " ")   #Sentence is replaced without underscores 
        print(sentence)
        patientMenu.close()
      
   


