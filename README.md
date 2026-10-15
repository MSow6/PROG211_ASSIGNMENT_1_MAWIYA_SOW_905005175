# Government License Management System for Sierra Leone 🇸🇱

## 1. Project Overview

The Government License Management System is a Python-based, terminal application developed as an Object-Oriented Programming (OOP) project.

The system demonstrates how a digital platform could help manage government license applications in Sierra Leone. It allows citizens to register accounts, submit license applications, track application progress, respond to correction requests, and receive updates about their applications.

It also provides different roles for government officials to review applications, request corrections, approve or reject applications, and mark approved licenses as ready for collection.

This project is an educational prototype. It is not an official Government of Sierra Leone system, and its workflows do not represent verified government licensing procedures.

## 2. Project Objectives

The main objectives of this project are to:

- Apply Object-Oriented Programming concepts in Python.
- Demonstrate the use of classes, objects, attributes, and methods.
- Use dictionaries and lists to manage information.
- Demonstrate how different user roles can interact with a system.
- Provide a simple way to submit and track license applications.
- Demonstrate application status management and status history.
- Explore Digital Public Goods (DPG) principles, including accessibility, privacy, modularity, and open-source development.

## 3. Key Features

### Citizen Features

Citizens can:

- Register an account.
- Log in to their accounts.
- Receive automatically generated citizen IDs.
- Submit license applications.
- Select a license category.
- Enter information required for the selected license type.
- View their submitted applications.
- Track application statuses.
- View application status history.
- Respond to requests for additional information.
- Correct application details, subject to the correction limit.

### Application Officer Features

Application Officers can:

- Access the Application Officer menu.
- Locate and review applications.
- Mark applications as under review.
- Request corrections from citizens.
- Provide messages explaining the required corrections.

### Approving Officer Features

Approving Officers can:

- Access the Approving Officer menu.
- Review applications awaiting a decision.
- Approve applications.
- Reject applications.
- Provide reasons for decisions.
- Mark approved licenses as ready for collection.

### System Administrator Features

System Administrators can:

- Access administrative functions.
- Review applicant and application information.
- Perform supported application management operations.
- View a summary of system records.

### Application Management

The system supports:

- Automatic generation of applicant and application IDs.
- Duplicate ID checks.
- Application status tracking.
- Application status history.
- License-specific application forms.
- Input validation.
- A maximum of two correction attempts per application.
- Restrictions on certain actions based on application status and user role.

## 4. Supported License Categories

The prototype includes four license categories:

1. Business License
2. Professional License
3. Driving License
4. Construction License

Each category has its own set of application fields.

The information collected depends on the selected license category.

## 5. Technologies Used

- **Programming Language:** Python 3
- **Interface:** Command-Line Interface (CLI)
- **Programming Paradigm:** Object-Oriented Programming
- **Data Structures:** Dictionaries and lists
- **Data Management:** Python objects and in-memory storage
- **Development Environment:** Visual Studio Code

The project uses Python's standard library and does not require third-party Python packages.

## 6. Project Structure

The project is organized into separate Python files to improve readability and maintainability.

```text
Government_License_Management_System/
│
├── main.py
├── Applicant.py
├── Applicant_Registry.py
├── License.py
├── License_Application.py
├── Application_Registry.py
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Runs the application and manages menus, login, user interactions, and application workflows. |
| `Applicant.py` | Defines the Applicant class and handles applicant information and validation. |
| `Applicant_Registry.py` | Registers applicants, searches for applicants, displays records, and counts applicants. |
| `License.py` | Defines the License class and validates license information, dates, and statuses. |
| `License_Application.py` | Defines license applications, manages application details, validates statuses, and records status history. |
| `Application_Registry.py` | Registers applications, checks applicant registration, searches for applications, and displays records. |
| `README.md` | Documents the project and explains how to install and run it. |

## 7. Installation and Setup

### Requirements

To run the project, you need:

- Python 3 installed on your computer.
- A terminal or command-line application.
- The project source files.

Visual Studio Code is recommended but is not compulsory.

### Step 1: Download the Project

Clone the repository using:

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with the actual URL of your GitHub repository.

Alternatively, download the project as a ZIP file from GitHub and extract it.

### Step 2: Open the Project Folder

Open the project folder in Visual Studio Code or navigate to it using your terminal.

### Step 3: Run the Application

Run the following command:

```bash
python3 main.py
```

On systems where Python is configured differently, you may be able to use:

```bash
python main.py
```

The application should start in your terminal.

## 8. Demonstration Accounts

The prototype includes predefined government official accounts for demonstration purposes.

| Username | Password | Role |
|---|---|---|
| `officer01` | `review123` | Application Officer |
| `approver01` | `approve123` | Approving Officer |
| `admin01` | `admin123` | System Administrator |

**Security Notice:** These credentials are for demonstration purposes only. The prototype stores passwords in plain text, and its authentication implementation is not suitable for a production government system.

Do not use real or sensitive personal information when testing the application.

## 9. How to Use the System

### Citizen Workflow

1. Start the application.
2. Select the citizen registration option.
3. Enter the required registration details.
4. Log in using the newly created account.
5. Select the option to submit a license application.
6. Choose a license category.
7. Enter the required application information.
8. Submit the application.
9. Use the tracking feature to check the application's status.
10. If corrections are requested, read the official's message and update the relevant information.

### Application Officer Workflow

1. Log in using the Application Officer demonstration account.
2. Access the Application Officer menu.
3. Locate an application.
4. Review the submitted information.
5. Mark the application as under review or request corrections, depending on the available options.

### Approving Officer Workflow

1. Log in using the Approving Officer demonstration account.
2. Access the Approving Officer menu.
3. Locate an application awaiting a decision.
4. Review the application.
5. Approve or reject it.
6. Provide a reason for the decision when required.
7. If approved, mark the license as ready for collection when the system permits it.

### System Administrator Workflow

1. Log in using the System Administrator demonstration account.
2. Access the administrative menu.
3. Review applicant and application information.
4. Use the supported management operations.
5. View the system summary.

Available actions depend on the user's role and the application's current status.

## 10. Object-Oriented Programming Concepts

This project demonstrates several fundamental Object-Oriented Programming concepts.

### Classes and Objects

Classes define the structure and behaviour of objects.

The project includes these classes:

- `Applicant`
- `ApplicantRegistry`
- `License`
- `LicenseApplication`
- `ApplicationRegistry`

Objects created from these classes represent applicants, licenses, applications, and registries.

### Attributes

Attributes store information associated with an object.

Examples include:

- `applicant_id`
- `full_name`
- `phone`
- `address`
- `application_id`
- `license_type`
- `submission_date`
- `status`

### Instance Methods

Instance methods operate on individual objects.

Examples include:

- `display_info()`
- `update_phone()`
- `update_address()`
- `update_status()`
- `add_applicant()`
- `add_application()`

These methods allow the system to display information, update records, and manage registrations.

### Class Methods

The `License` and `LicenseApplication` classes demonstrate the use of class methods through the `@classmethod` decorator.

For example:

```python
@classmethod
def get_valid_statuses(cls):
    return cls.VALID_STATUSES.copy()
```

This method returns the valid statuses defined by the class.

Class methods help organize behaviour associated with a class rather than with one specific object.

### Static Methods

The project also uses static methods for validation tasks.

Examples include validating text, phone numbers, and dates.

Static methods allow validation logic to be organized inside the relevant class without requiring an existing object.

### Encapsulation and Validation

The classes validate important inputs before accepting them.

For example, the Applicant class checks that required text fields are not empty and that phone numbers contain an acceptable number of digits.

The License class checks that dates are valid and that the expiry date is later than the issue date.

These checks help prevent invalid information from entering the system through supported operations.

## 11. Python Data Structures

### Dictionaries

Dictionaries store applicants, applications, application details, and other related information.

For example, the applicant registry uses a dictionary to associate applicant IDs with Applicant objects.

```python
self.applicants = {}
```

The application registry stores applications using application IDs.

```python
self.applications = {}
```

This makes it possible to search for records using their identifiers.

### Lists

Lists store collections of valid statuses and other related values.

For example:

```python
VALID_STATUSES = [
    "Pending",
    "Active",
    "Expired",
    "Suspended",
    "Revoked"
]
```

### Objects and Dictionaries Together

The registries store objects created from the Applicant and LicenseApplication classes.

This demonstrates how Python objects and data structures can work together to organize information.

## 12. Application Status Management

The prototype supports several application statuses, including:

- Submitted
- Under Review
- More Information Required
- Approved
- Ready for Collection
- Rejected

When an application's status changes, the system records the status, message, and date in its history.

This allows citizens to review the recorded progress of their applications.

The prototype also restricts certain operations according to the application's current status. For example, a license can only be marked ready for collection after the application has been approved.

## 13. Digital Public Goods (DPG) Principles

This project explores principles relevant to developing accessible, reusable, and responsible public-interest software.

### 13.1 Open Source

The project is intended to be published on GitHub so that its source code can be inspected, studied, and improved.

However, public visibility alone does not establish an open-source license. A suitable license must be added before the project can formally claim to be open source.

### 13.2 Accessibility and Inclusion

The terminal interface uses text-based menus and messages to guide users through the available operations.

This provides a straightforward way to demonstrate the system's functionality.

However, a terminal application may not be accessible to every citizen. A future version could provide a graphical or web interface, support assistive technologies, and offer relevant local-language options.

### 13.3 Privacy and Data Protection

The prototype uses temporary in-memory data and is intended for educational demonstrations.

It should only be tested with fictional information.

A production system would require stronger privacy protections, secure authentication, appropriate authorization, secure storage, and measures to prevent unauthorized access.

### 13.4 Modularity and Reusability

The system separates its main classes into different files.

For example, applicant management is separated from application management.

This modular structure makes the code easier to understand, maintain, test, and extend.

Future developers could build additional features without placing the entire system in one large Python file.

## 14. Current Limitations

This project is an educational prototype and has several limitations:

- All records are stored in memory.
- Data is lost when the application exits.
- There is no database integration.
- The interface is terminal-based.
- Demonstration passwords are stored in plain text.
- The system is not connected to official government services.
- License requirements and procedures have not been verified against official Sierra Leone government regulations.
- The system has not been assessed for production security, accessibility, or legal compliance.

These limitations should be addressed before considering real-world deployment.

## 15. Future Improvements

Possible future improvements include:

- Integrating a database such as PostgreSQL.
- Implementing secure password hashing.
- Developing a graphical or web-based interface.
- Improving authentication and authorization.
- Introducing automated tests.
- Improving error handling and input validation.
- Adding secure document uploads.
- Supporting accessible design and local languages.
- Introducing secure notifications for application updates.
- Implementing audit logging and appropriate data protection controls.
- Reviewing the workflow against official licensing requirements.
- Deploying the system through an appropriately secured hosting environment.

## 16. Sample Workflow

A typical demonstration may follow this sequence:

1. Register a citizen account.
2. Log in as the citizen.
3. Submit a Business License application.
4. Log in as an Application Officer.
5. Review the application.
6. Request additional information if necessary.
7. Log in as the citizen and submit corrections.
8. Review the updated application.
9. Log in as an Approving Officer.
10. Approve or reject the application.
11. If approved, mark the license as ready for collection.

The exact menu wording and output depend on the version of the source code being executed.

## 17. Screenshots

Screenshots can be added to demonstrate the application's functionality.

Recommended screenshots include:

1. Main menu.
2. Citizen registration.
3. Citizen login.
4. License application submission.
5. Application tracking.
6. Application status history.
7. Application Officer menu.
8. Approving Officer menu.
9. System Administrator menu.

After adding actual screenshots to the repository, they can be displayed here using Markdown.

For example:

```markdown
![Main Menu](screenshots/main-menu.png)
```

The screenshot file must exist at the specified path for the image to display correctly.

## 18. Academic Context

This project was developed as an individual Object-Oriented Programming assignment.

It demonstrates the application of Python classes, objects, attributes, methods, data structures, validation, and modular programming to a public-service scenario.

The project also explores how software design can incorporate Digital Public Goods principles.

## 19. Author and Repository

**Project Title:** Government License Management System for Sierra Leone

**Programming Language:** Python

**Project Type:** Educational Object-Oriented Programming Prototype

**Author:** Add your name here.

**GitHub Repository:** Add your repository URL here after publishing the project.

## 20. Disclaimer

This is an educational prototype and is not an official Government of Sierra Leone service.

It must not be used to process real government license applications or sensitive personal information.

The project demonstrates programming concepts and possible public-service workflows. It does not replace official government licensing procedures, legal requirements, or secure production systems.
