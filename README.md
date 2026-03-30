# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
```mermaid
flowchart LR
    Student((Student))
    Admin((Admin))
    
    Login((Login))
    ViewCatalog((View Course Catalog))
    RegDrop((Register/Drop Courses))
    ViewSchedule((View Schedule))
    ViewBilling((View Billing Summary))
    ManageProfile((Edit Profile))

    ManageStudents((Manage Students))
    ManageCourses((Manage Courses))
    ViewRoster((View Class Roster))
    
    Student --> Login
    Student --> ViewCatalog
    Student --> RegDrop
    Student --> ViewSchedule
    Student --> ViewBilling
    Student --> ManageProfile
    
    Admin --> Login
    Admin --> ViewCatalog
    Admin --> ManageStudents
    Admin --> ManageCourses
    Admin --> ViewRoster
    Admin --> ViewSchedule
    Admin --> ViewBilling
```

### Flowchart of the main workflow
```mermaid
flowchart TD
    Start([Start Application]) --> LoadData[Load Data or Seed Defaults]
    LoadData --> LoginMenu{Login Menu}
    
    LoginMenu -->|Option 1| StudentLogin[Student Login]
    LoginMenu -->|Option 2| AdminLogin[Admin Login]
    LoginMenu -->|Option 3| SaveExit[Save Data and Exit]
    
    StudentLogin --> StudentMenu{Student Menu}
    StudentMenu -->|Pick Action| StudentAction[View Catalog, Register, Drop, Schedule, Billing, Profile]
    StudentAction --> StudentMenu
    StudentMenu -->|Logout| SaveData1[Save Data] --> LoginMenu
    
    AdminLogin --> AdminMenu{Admin Menu}
    AdminMenu -->|Pick Action| AdminAction[Manage Courses, Manage Students, View Rosters, Billing]
    AdminAction --> AdminMenu
    AdminMenu -->|Logout| SaveData2[Save Data] --> LoginMenu
    
    SaveExit --> Stop([End Application])
```

### Prompts
1. "Execute this code. i want to know what program does"
2. "Try to execute it, read the code, and understand what the program does. Create a use case diagram that shows the program's functionality. Put the use case diagram in the README.md. Create a flowchart (using Mermaid) to show the user's flow through the main menu. Put the flowchart in the README.md. Based on what you understand about the program, select one use case and create an equivalent Python version of the program. Put the Python program in a new folder called python. You can use AI to help you on this, but you must put the prompts you used in the README.md under the section # Prompts. Commit the code and push to the repository. Put the URL of your forked repository in the provided box below."
