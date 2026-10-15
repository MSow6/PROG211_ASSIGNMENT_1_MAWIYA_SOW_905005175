class Applicant:
    
    def __init__(self, applicant_id, full_name, phone, address):
        self.applicant_id = self._validate_text(
            applicant_id, "Applicant ID"
        )
        self.full_name = self._validate_text(
            full_name, "Full name"
        )
        self.phone = self._validate_phone(phone)
        self.address = self._validate_text(
            address, "Address"
        )

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be text.")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} cannot be empty.")

        return value

    @staticmethod
    def _validate_phone(phone):
        phone = Applicant._validate_text(phone, "Phone number")

        if not phone.isdigit():
            raise ValueError(
                "Phone number must contain digits only."
            )

        if not 7 <= len(phone) <= 15:
            raise ValueError(
                "Phone number must contain between 7 and 15 digits."
            )

        return phone

    def display_info(self):
        print("\n===== APPLICANT DETAILS =====")
        print(f"Applicant ID: {self.applicant_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Phone Number: {self.phone}")
        print(f"Address: {self.address}")
        print("=============================")

    def update_phone(self, new_phone):
        validated_phone = self._validate_phone(new_phone)
        self.phone = validated_phone
        print("Phone number updated successfully.")

    def update_address(self, new_address):
        validated_address = self._validate_text(
            new_address, "Address"
        )
        self.address = validated_address
        print("Address updated successfully.")