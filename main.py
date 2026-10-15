from Applicant import Applicant
from Applicant_Registry import ApplicantRegistry
from License_Application import LicenseApplication
from Application_Registry import ApplicationRegistry


# ==========================================
# SYSTEM SETUP
# ==========================================

applicant_registry = ApplicantRegistry()
application_registry = ApplicationRegistry(applicant_registry)

citizens = {}

citizen_counter = 1
applicant_counter = 1
application_counter = 1


# ==========================================
# LICENSE SERVICES AND THEIR FORM FIELDS
# ==========================================

LICENSE_FORMS = {
    "1": {
        "name": "Business License",
        "fields": [
            "Business Name",
            "Business Type",
            "Business Address",
            "Applicant's Role",
            "Business Contact Number"
        ]
    },
    "2": {
        "name": "Professional License",
        "fields": [
            "Profession",
            "Professional Qualification",
            "Qualification Institution",
            "Certificate Number",
            "Years of Experience"
        ]
    },
    "3": {
        "name": "Driving License",
        "fields": [
            "Date of Birth (YYYY-MM-DD)",
            "Driving License Category",
            "Already Holds a Driving License (yes/no)",
            "Previous License Number (or N/A)"
        ]
    },
    "4": {
        "name": "Construction License",
        "fields": [
            "Company or Contractor Name",
            "Type of Construction Work",
            "Project Address",
            "Project Description",
            "Registration Details (or N/A)"
        ]
    }
}

# ==========================================
# DEMONSTRATION OFFICIAL ACCOUNTS
# ==========================================
OFFICIAL_ACCOUNTS = {
    "officer01": {
        "password": "review123",
        "role": "Application Officer"
    },
    "approver01": {
        "password": "approve123",
        "role": "Approving Officer"
    },
    "admin01": {
        "password": "admin123",
        "role": "System Administrator"
    }
}

# ==========================================
# GENERAL HELPERS
# ==========================================

def generate_id(prefix, number):
    return f"{prefix}{number:06d}"


def get_application(application_id):
    return application_registry.find_application(
        application_id.strip()
    )


def show_services():
    print("\n========== AVAILABLE LICENSES ==========")

    for number, form in LICENSE_FORMS.items():
        print(f"{number}. {form['name']}")

    print("========================================")


def display_application_history(application):
    print("\n========== APPLICATION HISTORY ==========")

    for entry in application.history:
        print(f"Date: {entry['date']}")
        print(f"Status: {entry['status']}")
        print(f"Message: {entry['message']}")
        print("----------------------------------------")

    print("========================================")


def display_citizen_application(application):
    application.display_info()

    print("\nMESSAGE FOR CITIZEN:")
    print(
        application.STATUS_MESSAGES.get(
            application.status,
            "Please contact the relevant department."
        )
    )

    if application.status == "More Information Required":
        print(
            f"Correction attempts remaining: "
            f"{application.correction_limit - application.correction_attempts}"
        )

    if application.decision_reason:
        print(f"Official's Message: {application.decision_reason}")


def display_all_applications():
    if not application_registry.applications:
        print("No applications have been submitted.")
        return

    application_registry.display_all_applications()


# ==========================================
# APPLICATION FORM
# ==========================================

def collect_license_details(license_type, existing_details=None):
    """Collect or update information for the selected license."""

    form = None

    for service in LICENSE_FORMS.values():
        if service["name"] == license_type:
            form = service
            break

    if form is None:
        raise ValueError("This license type has no configured form.")

    if existing_details is None:
        details = {}
    else:
        details = existing_details.copy()

    print(f"\n========== {license_type.upper()} FORM ==========")
    print("Enter the requested information below.")
    print("Enter N/A only when a field genuinely does not apply.")

    for field in form["fields"]:
        previous_value = details.get(field, "")

        if previous_value:
            print(f"\nCurrent {field}: {previous_value}")
            print("Press Enter to keep the current value.")
            value = input(f"New {field}: ").strip()

            if value:
                details[field] = value

        else:
            value = input(f"{field}: ").strip()

            if not value:
                print(f"{field} cannot be empty.")
                return None

            details[field] = value

    if license_type == "Driving License":
        dob = details.get("Date of Birth (YYYY-MM-DD)", "")

        try:
            from datetime import date

            birth_date = date.fromisoformat(dob)

            if birth_date > date.today():
                print("Date of birth cannot be in the future.")
                return None

        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
            return None

        holds_license = details.get(
            "Already Holds a Driving License (yes/no)", ""
        ).casefold()

        if holds_license not in ("yes", "no"):
            print("Please answer yes or no for existing license.")
            return None

    print("\n========== REVIEW YOUR INFORMATION ==========")

    for field, value in details.items():
        print(f"{field}: {value}")

    print("=============================================")

    return details


# ==========================================
# CITIZEN REGISTRATION
# ==========================================

def citizen_registration():
    global citizen_counter, applicant_counter

    print("\n========== CITIZEN REGISTRATION ==========")

    try:
        full_name = input("Full Name: ").strip()
        email = input("Email Address: ").strip().casefold()
        phone = input("Phone Number: ").strip()
        address = input("Address: ").strip()

        if (
            not email
            or "@" not in email
            or "." not in email.split("@")[-1]
        ):
            print("Please enter a valid email address.")
            return

        if email in citizens:
            print("An account with this email already exists.")
            return

        password = input("Create Password (minimum 6 characters): ")
        confirm_password = input("Confirm Password: ")

        if len(password) < 6:
            print("Password must contain at least 6 characters.")
            return

        if password != confirm_password:
            print("Passwords do not match.")
            return

        citizen_id = generate_id("CIT", citizen_counter)
        applicant_id = generate_id("APP", applicant_counter)

        applicant = Applicant(
            applicant_id,
            full_name,
            phone,
            address
        )

        applicant_registry.add_applicant(applicant)

        citizens[email] = {
            "citizen_id": citizen_id,
            "email": email,
            "password": password,
            "applicant": applicant
        }

        citizen_counter += 1
        applicant_counter += 1

        print("\nRegistration successful!")
        print(f"Citizen ID: {citizen_id}")
        print(f"Applicant ID: {applicant_id}")
        print("You can now log in.")

    except (ValueError, TypeError) as error:
        print(f"Registration failed: {error}")


# ==========================================
# CITIZEN LOGIN
# ==========================================

def citizen_login():
    print("\n========== CITIZEN LOGIN ==========")

    email = input("Email Address: ").strip().casefold()
    password = input("Password: ")

    citizen = citizens.get(email)

    if citizen is None or citizen["password"] != password:
        print("Invalid email or password.")
        return

    print(f"\nWelcome, {citizen['applicant'].full_name}!")
    citizen_dashboard(citizen)


# ==========================================
# SUBMIT A NEW APPLICATION
# ==========================================

def submit_application(citizen):
    global application_counter

    show_services()

    choice = input("Choose a license number: ").strip()

    if choice not in LICENSE_FORMS:
        print("Invalid service selection.")
        return

    license_type = LICENSE_FORMS[choice]["name"]

    details = collect_license_details(license_type)

    if details is None:
        print("Application was not submitted.")
        return

    confirm = input("\nSubmit this application? (yes/no): ").strip().casefold()

    if confirm != "yes":
        print("Application cancelled.")
        return

    application_id = generate_id("LA", application_counter)

    try:
        application = LicenseApplication(
            application_id,
            citizen["applicant"],
            license_type
        )

        application.application_details = details

        application_registry.add_application(application)
        application_counter += 1

        print("\nApplication submitted successfully!")
        print(f"Application ID: {application_id}")
        print("Status: Submitted")
        print(application.STATUS_MESSAGES["Submitted"])

    except (ValueError, TypeError) as error:
        print(f"Application failed: {error}")


# ==========================================
# VIEW CITIZEN APPLICATIONS
# ==========================================

def view_my_applications(citizen):
    applicant_id = citizen["applicant"].applicant_id
    found = False

    print("\n========== MY APPLICATIONS ==========")

    for application in application_registry.applications.values():
        if application.applicant.applicant_id == applicant_id:
            display_citizen_application(application)
            found = True

    if not found:
        print("You have not submitted any applications.")


# ==========================================
# TRACK APPLICATION AND HISTORY
# ==========================================

def track_application(citizen):
    application_id = input("Enter Application ID: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    if (
        application.applicant.applicant_id
        != citizen["applicant"].applicant_id
    ):
        print("Access denied. This application does not belong to you.")
        return

    display_citizen_application(application)
    display_application_history(application)


# ==========================================
# CORRECT AN EXISTING APPLICATION
# ==========================================

def correct_application(citizen):
    application_id = input("Enter Application ID to correct: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    if (
        application.applicant.applicant_id
        != citizen["applicant"].applicant_id
    ):
        print("Access denied.")
        return

    if application.status != "More Information Required":
        print("This application is not awaiting corrections.")
        return

    remaining = (
        application.correction_limit
        - application.correction_attempts
    )

    if remaining <= 0:
        print("You have used both correction attempts.")
        print("Please contact the relevant government department.")
        return

    print("\n========== CORRECTION REQUEST ==========")
    print(f"Official's Message: {application.correction_request}")
    print(f"Correction attempts remaining: {remaining}")

    updated_details = collect_license_details(
        application.license_type,
        application.application_details
    )

    if updated_details is None:
        print("No correction was submitted.")
        return

    confirm = input(
        "\nSubmit these corrections? (yes/no): "
    ).strip().casefold()

    if confirm != "yes":
        print("Correction cancelled. No attempt was used.")
        return

    # Count only when the citizen confirms resubmission.
    application.correction_attempts += 1
    application.application_details = updated_details
    application.correction_request = ""

    application.update_status(
        "Submitted",
        "Your corrected application has been resubmitted "
        "and is awaiting review."
    )

    print("\nCorrections submitted successfully!")
    print(f"Application ID remains: {application.application_id}")
    print(
        f"Attempts used: {application.correction_attempts}/"
        f"{application.correction_limit}"
    )


# ==========================================
# CITIZEN PROFILE
# ==========================================

def view_my_profile(citizen):
    print("\n========== MY PROFILE ==========")
    print(f"Citizen ID: {citizen['citizen_id']}")
    print(f"Email: {citizen['email']}")
    citizen["applicant"].display_info()


# ==========================================
# CITIZEN DASHBOARD
# ==========================================

def citizen_dashboard(citizen):
    while True:
        print("\n========== CITIZEN PORTAL ==========")
        print("1. View Available Services")
        print("2. Apply for a License")
        print("3. View My Applications")
        print("4. Track Application and History")
        print("5. Correct an Application")
        print("6. View My Profile")
        print("0. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_services()

        elif choice == "2":
            submit_application(citizen)

        elif choice == "3":
            view_my_applications(citizen)

        elif choice == "4":
            track_application(citizen)

        elif choice == "5":
            correct_application(citizen)

        elif choice == "6":
            view_my_profile(citizen)

        elif choice == "0":
            print("Logged out successfully.")
            break

        else:
            print("Invalid option.")


# ==========================================
# OFFICIAL LOGIN
# ==========================================

def official_login():
    print("\n========== GOVERNMENT OFFICIAL LOGIN ==========")

    username = input("Username: ").strip()
    password = input("Password: ")

    official = OFFICIAL_ACCOUNTS.get(username)

    if official is None or official["password"] != password:
        print("Invalid username or password.")
        return

    role = official["role"]

    print(f"\nWelcome, {role}!")
    official_dashboard(role)


# ==========================================
# REQUEST CORRECTIONS
# ==========================================

def request_corrections(role):
    if role not in ("Application Officer", "System Administrator"):
        print("Access denied.")
        return

    application_id = input("Application ID: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    if application.status in (
        "Approved", "Ready for Collection", "Rejected"
    ):
        print("This application cannot be sent for corrections.")
        return

    remaining = (
        application.correction_limit
        - application.correction_attempts
    )

    if remaining <= 0:
        print("The citizen has used both correction attempts.")
        print("You may need to handle this case outside the correction workflow.")
        return

    reason = input("Explain what needs to be corrected: ").strip()

    if not reason:
        print("A correction request message is required.")
        return

    application.correction_request = reason

    application.update_status(
        "More Information Required",
        f"Additional information is required: {reason}"
    )

    print("Correction request sent to the citizen.")


# ==========================================
# REVIEW APPLICATION
# ==========================================

def review_application(role):
    if role not in ("Application Officer", "System Administrator"):
        print("Access denied.")
        return

    application_id = input("Application ID to review: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    application.display_info()

    if application.status in (
        "Approved", "Ready for Collection", "Rejected"
    ):
        print("This application already has a final decision.")
        return

    print("\n1. Mark Under Review")
    print("2. Request Corrections")
    print("0. Cancel")

    choice = input("Choose an action: ").strip()

    if choice == "1":
        application.update_status("Under Review")

    elif choice == "2":
        request_corrections(role)

    elif choice == "0":
        return

    else:
        print("Invalid option.")


# ==========================================
# APPROVE OR REJECT APPLICATION
# ==========================================

def decide_application(role, decision):
    if role != "Approving Officer":
        print("Access denied.")
        return

    application_id = input("Application ID: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    application.display_info()

    if application.status not in ("Submitted", "Under Review"):
        print(
            "This application must be submitted or under review "
            "before a final decision."
        )
        return

    if decision == "Rejected":
        reason = input("Reason for rejection: ").strip()

        if not reason:
            print("A rejection reason is required.")
            return

        application.decision_reason = reason

        application.update_status(
            "Rejected",
            f"Your application has been rejected. Reason: {reason}"
        )

    elif decision == "Approved":
        application.decision_reason = ""

        application.update_status(
            "Approved",
            application.STATUS_MESSAGES["Approved"]
        )

    print("Decision recorded successfully.")


# ==========================================
# MARK LICENSE READY FOR COLLECTION
# ==========================================

def mark_ready_for_collection(role):
    if role not in ("Approving Officer", "System Administrator"):
        print("Access denied.")
        return

    application_id = input("Application ID: ").strip()
    application = get_application(application_id)

    if application is None:
        print("Application not found.")
        return

    if application.status != "Approved":
        print(
            "Only approved applications can be marked ready "
            "for collection."
        )
        return

    application.update_status(
        "Ready for Collection",
        application.STATUS_MESSAGES["Ready for Collection"]
    )

    print("The citizen can now see that their license is ready.")


# ==========================================
# ADMIN SUMMARY
# ==========================================

def system_summary(role):
    if role != "System Administrator":
        print("Access denied.")
        return

    print("\n========== SYSTEM SUMMARY ==========")
    print("Registered Citizens:", len(citizens))
    print("Registered Applicants:", applicant_registry.count_applicants())
    print(
        "Total Applications:",
        application_registry.count_applications()
    )


# ==========================================
# OFFICIAL DASHBOARD
# ==========================================

def official_dashboard(role):
    while True:
        print(f"\n========== OFFICIAL PORTAL: {role} ==========")
        print("1. View All Applications")
        print("2. Review Application / Request Corrections")

        if role == "Approving Officer":
            print("3. Approve Application")
            print("4. Reject Application")
            print("5. Mark License Ready for Collection")

        if role == "System Administrator":
            print("3. View All Applicants")
            print("4. View System Summary")
            print("5. Mark License Ready for Collection")

        print("0. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Logged out successfully.")
            break

        elif choice == "1":
            display_all_applications()

        elif choice == "2":
            review_application(role)

        elif role == "Approving Officer" and choice == "3":
            decide_application(role, "Approved")

        elif role == "Approving Officer" and choice == "4":
            decide_application(role, "Rejected")

        elif role == "Approving Officer" and choice == "5":
            mark_ready_for_collection(role)

        elif role == "System Administrator" and choice == "3":
            applicant_registry.display_all_applicants()

        elif role == "System Administrator" and choice == "4":
            system_summary(role)

        elif role == "System Administrator" and choice == "5":
            mark_ready_for_collection(role)

        else:
            print("Invalid option for your role.")


# ==========================================
# MAIN MENU
# ==========================================

def main():
    while True:
        print("\n============================================")
        print(" GOVERNMENT LICENSE MANAGEMENT SYSTEM")
        print("              SIERRA LEONE")
        print("============================================")
        print("1. Citizen Registration")
        print("2. Citizen Login")
        print("3. Government Official Login")
        print("0. Exit")
        print("============================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            citizen_registration()

        elif choice == "2":
            citizen_login()

        elif choice == "3":
            official_login()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()