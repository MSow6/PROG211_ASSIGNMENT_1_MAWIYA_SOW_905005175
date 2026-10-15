from License_Application import LicenseApplication

class ApplicationRegistry:

    def __init__(self, applicant_registry):
        self.applicant_registry = applicant_registry
        self.applications = {}

    def add_application(self, application):
        if not isinstance(application, LicenseApplication):
            raise TypeError(
                "Only LicenseApplication objects can be registered."
            )

        applicant_id = application.applicant.applicant_id

        registered_applicant = (
            self.applicant_registry.find_applicant(applicant_id)
        )

        if registered_applicant is None:
            raise ValueError(
                f"Applicant {applicant_id} is not registered."
            )   

        application_id = application.application_id

        if application_id in self.applications:
            raise ValueError(
                f"Application ID {application_id} already exists."
            )

        self.applications[application_id] = application

        print(
            f"Application {application_id} "
            "registered successfully."
        )

    def find_application(self, application_id):
        if not isinstance(application_id, str):
            raise TypeError("Application ID must be text.")

        application_id = application_id.strip()

        if not application_id:
            raise ValueError("Application ID cannot be empty.")

        return self.applications.get(application_id)

    def display_all_applications(self):
        if not self.applications:
            print("No applications have been registered.")
            return

        for application in self.applications.values():
            application.display_info()

    def count_applications(self):
        return len(self.applications)