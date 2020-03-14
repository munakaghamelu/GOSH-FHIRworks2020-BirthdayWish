from flask import Flask
from flask_restful import Api, Resource
from fhir_parser.fhir import FHIR

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def __init__(self):
        super(Data, self).__init__()

    def get(self):
        fhir_parser = FHIR(endpoint="http://localhost:5000/api/", verify_ssl=False)
        patients = fhir_parser.get_all_patients()

        januaryPatients = ""
        febrauryPatients = ""
        marchPatients = ""
        aprilPatients = ""
        mayPatients = ""
        junePatients = ""
        julyPatients = ""
        augustPatients = ""
        septemberPatients = ""
        octoberPatients = ""
        novemberPatients = ""
        decemberPatients = ""

        for patient in patients:
            identifier = patient.full_name()
            if (patient.birth_date.month == 1): januaryPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 2): febrauryPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 3): marchPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 4): aprilPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 5): mayPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 6): junePatients += patient.full_name() + ","
            elif (patient.birth_date.month == 7): julyPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 8): augustPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 9): septemberPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 10): octoberPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 11): novemberPatients += patient.full_name() + ","
            elif (patient.birth_date.month == 12): decemberPatients += patient.full_name() + ","

        sortedByBirthday = {"january": januaryPatients, "february": febrauryPatients, "march": marchPatients, "april": aprilPatients, "may": marchPatients, "june": junePatients, "july": julyPatients, "august": augustPatients, "september": septemberPatients, "november": novemberPatients, "december": decemberPatients}

        return sortedByBirthday

api.add_resource(Data, "/p/birthdayWish_Api/", endpoint="birthdayWish")

if __name__ == "__main__":
    app.run(debug=True, port=5002)