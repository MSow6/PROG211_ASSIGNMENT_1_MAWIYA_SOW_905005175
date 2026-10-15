from datetime import datetime, date


class License:
    VALID_STATUSES = [
        "Pending",
        "Active",
        "Expired",
        "Suspended",
        "Revoked"
    ]

    def __init__(
        self,
        license_number,
        license_type,
        issue_date,
        expiry_date,
        status="Pending"
    ):
        self.license_number = self._validate_text(
            license_number, "License number"
        )

        self.license_type = self._validate_text(
            license_type, "License type"
        )

        self.issue_date = self._validate_date(
            issue_date, "Issue date"
        )

        self.expiry_date = self._validate_date(
            expiry_date, "Expiry date"
        )

        self._validate_date_order(
            self.issue_date, self.expiry_date
        )

        self.status = self._validate_status(status)

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be text.")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} cannot be empty.")

        return value

    @staticmethod
    def _validate_date(value, field_name):
        if isinstance(value, datetime):
            raise TypeError(
                f"{field_name} must be a date, not a datetime."
            )

        if isinstance(value, date):
            return value

        if not isinstance(value, str):
            raise TypeError(
                f"{field_name} must be a date in YYYY-MM-DD format."
            )

        try:
            return date.fromisoformat(value)
        except ValueError:
            raise ValueError(
                f"{field_name} must use YYYY-MM-DD format "
                "and represent a valid date."
            ) from None

    @staticmethod
    def _validate_date_order(issue_date, expiry_date):
        if expiry_date <= issue_date:
            raise ValueError(
                "Expiry date must be later than issue date."
            )

    @classmethod
    def get_valid_statuses(cls):
        return cls.VALID_STATUSES.copy()

    @classmethod
    def is_valid_status(cls, status):
        return (
            isinstance(status, str)
            and status.strip().casefold()
            in [item.casefold() for item in cls.VALID_STATUSES]
        )

    @classmethod
    def _validate_status(cls, status):
        status = cls._validate_text(status, "License status")

        for valid_status in cls.VALID_STATUSES:
            if status.casefold() == valid_status.casefold():
                return valid_status

        raise ValueError(
            f"Invalid license status. Choose from: "
            f"{', '.join(cls.VALID_STATUSES)}."
        )

    def display_info(self):
        print("\n===== LICENSE DETAILS =====")
        print(f"License Number: {self.license_number}")
        print(f"License Type: {self.license_type}")
        print(f"Issue Date: {self.issue_date}")
        print(f"Expiry Date: {self.expiry_date}")
        print(f"Status: {self.status}")
        print("===========================")