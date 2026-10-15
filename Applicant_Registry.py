from Applicant import Applicant


class ApplicantRegistry:

    def __init__(self):
        self.applicants = {}

    def add_applicant(self, applicant):
        if not isinstance(applicant, Applicant):
            raise TypeError(
                "Only Applicant objects can be registered."
            )

        applicant_id = applicant.applicant_id

        if applicant_id in self.applicants:
            raise ValueError(
                f"Applicant ID {applicant_id} already exists."
            )

        self.applicants[applicant_id] = applicant

        print(
            f"Applicant {applicant.full_name} "
            "registered successfully."
        )

    def find_applicant(self, applicant_id):
        if not isinstance(applicant_id, str):
            raise TypeError("Applicant ID must be text.")

        applicant_id = applicant_id.strip()

        if not applicant_id:
            raise ValueError("Applicant ID cannot be empty.")

        return self.applicants.get(applicant_id)

    def display_all_applicants(self):
        if not self.applicants:
            print("No applicants have been registered.")
            return

        for applicant in self.applicants.values():
            applicant.display_info()

    def count_applicants(self):
        return len(self.applicants)