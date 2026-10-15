from datetime import date, datetime


class LicenseApplication:
    VALID_STATUSES = [
        "Submitted",
        "Under Review",
        "More Information Required",
        "Approved",
        "Ready for Collection",
        "Rejected"
    ]

    STATUS_MESSAGES = {
        "Submitted": (
            "Your application has been submitted successfully "
            "and is awaiting review."
        ),
        "Under Review": (
            "Your application is being reviewed by the "
            "relevant department."
        ),
        "More Information Required": (
            "Additional information is required. Please read "
            "the official's message and correct your application."
        ),
        "Approved": (
            "Your application has been approved, and we are "
            "now processing your license. We will notify you "
            "when it is ready for collection."
        ),
        "Ready for Collection": (
            "Your license is ready! You can now come and "
            "collect your license."
        ),
        "Rejected": (
            "Your application has been rejected. Please check "
            "the reason provided by the reviewing official."
        )
    }

    def __init__(
        self,
        application_id,
        applicant,
        license_type,
        submission_date=None,
        status="Submitted"
    ):
        self.application_id = self._validate_text(
            application_id, "Application ID"
        )

        self.applicant = self._validate_applicant(applicant)

        self.license_type = self._validate_text(
            license_type, "License type"
        )

        if submission_date is None:
            submission_date = date.today()

        self.submission_date = self._validate_date(submission_date)
        self.status = self._validate_status(status)

        # Information supplied on the license form.
        self.application_details = {}

        # Correction tracking.
        self.correction_attempts = 0
        self.correction_limit = 2
        self.correction_request = ""

        # Reason for a final decision, when applicable.
        self.decision_reason = ""

        # History of changes during this application's lifetime.
        self.history = [
            {
                "status": self.status,
                "message": self.STATUS_MESSAGES[self.status],
                "date": str(date.today())
            }
        ]

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be text.")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} cannot be empty.")

        return value

    @staticmethod
    def _validate_applicant(applicant):
        from Applicant import Applicant

        if not isinstance(applicant, Applicant):
            raise TypeError(
                "Applicant must be an Applicant object."
            )

        return applicant

    @staticmethod
    def _validate_date(value):
        if isinstance(value, datetime):
            raise TypeError(
                "Submission date must be a date, not a datetime."
            )

        if isinstance(value, date):
            result = value

        elif isinstance(value, str):
            try:
                result = date.fromisoformat(value)
            except ValueError:
                raise ValueError(
                    "Submission date must use YYYY-MM-DD format."
                ) from None

        else:
            raise TypeError(
                "Submission date must be a date or YYYY-MM-DD string."
            )

        if result > date.today():
            raise ValueError("Submission date cannot be in the future.")

        return result

    @classmethod
    def get_valid_statuses(cls):
        return cls.VALID_STATUSES.copy()

    @classmethod
    def _validate_status(cls, status):
        status = cls._validate_text(status, "Application status")

        for valid_status in cls.VALID_STATUSES:
            if status.casefold() == valid_status.casefold():
                return valid_status

        raise ValueError(
            "Invalid application status. Choose from: "
            + ", ".join(cls.VALID_STATUSES)
        )

    def update_status(self, new_status, message=None):
        """Update status and record the change in application history."""

        validated_status = self._validate_status(new_status)
        old_status = self.status

        self.status = validated_status

        if message is None:
            message = self.STATUS_MESSAGES[validated_status]

        self.history.append({
            "status": validated_status,
            "message": message,
            "date": str(date.today())
        })

        print(
            f"Application status changed from "
            f"{old_status} to {validated_status}."
        )

    def display_info(self):
        print("\n========== LICENSE APPLICATION ==========")
        print(f"Application ID: {self.application_id}")
        print(f"Applicant ID: {self.applicant.applicant_id}")
        print(f"Applicant Name: {self.applicant.full_name}")
        print(f"License Type: {self.license_type}")
        print(f"Submission Date: {self.submission_date}")
        print(f"Status: {self.status}")
        print(
            f"Correction Attempts: "
            f"{self.correction_attempts}/{self.correction_limit}"
        )

        if self.correction_request:
            print(
                f"Official's Correction Request: "
                f"{self.correction_request}"
            )

        if self.decision_reason:
            print(f"Decision Reason: {self.decision_reason}")

        if self.application_details:
            print("\nSubmitted Information:")

            for field, value in self.application_details.items():
                print(f"{field}: {value}")

        print("=========================================")