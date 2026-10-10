BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 15: COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION

Programme: BSc in Information Communication and Technology
Year: Three
Course Code: BICT 3202
Week: 15 of 16
Module: Object-Oriented Analysis and Design
Lecture Hours: 2
Tutorial Hours: 1
Practical Hours: 1
Independent Learning: 10 hours
Credits: 10

> Position in the course: Week 15 is the integration and application week. Students now take the concepts developed from Weeks 1–14 and apply them to a complete system. The emphasis is not simply on drawing UML diagrams, but on demonstrating that the diagrams tell a consistent story and can guide implementation.



The UML standard groups structural modelling and behavioural modelling into related but distinct parts of UML, which is important for this week's emphasis on integrating multiple views of the same system. 


---

1. WEEK 15 THEME

Complete Object-Oriented Analysis and Design: From Requirements to an Integrated Design

The central question for this week is:

> "If I am given a real software problem today, can I use everything I have learned to analyse it, model it, design it and communicate the design to another developer?"



By Week 15, students should no longer see:

use-case diagrams,

class diagrams,

sequence diagrams,

activity diagrams,

state diagrams,

component diagrams,


as separate examination topics.

Instead, they should understand them as different views of one software system.


---

2. LEARNING OUTCOMES

By the end of Week 15, students should be able to:

1. Analyse a complete software problem using object-oriented techniques.


2. Identify stakeholders and system actors.


3. Extract functional and non-functional requirements.


4. Identify appropriate use cases.


5. Construct a use-case model.


6. Identify candidate classes and objects.


7. Develop a conceptual/domain class model.


8. Refine the analysis model into a design model.


9. Identify class responsibilities.


10. Define attributes and operations.


11. Model associations, inheritance and composition where appropriate.


12. Develop interaction models for important use cases.


13. Develop sequence diagrams.


14. Develop activity diagrams.


15. Develop state-machine diagrams for state-dependent objects.


16. Develop a component-level view of the system.


17. Check consistency between UML models.


18. Document a complete OOAD solution.


19. Use a CASE/UML modelling tool to create and organise models.


20. Explain how the final design could be implemented.




---

PART A — WHAT HAVE WE BEEN LEARNING?

3. Looking Back at the Entire Module

Before starting the case study, students should see the entire journey.

The OOAD process can be simplified as:

Business Problem
       ↓
Requirements
       ↓
Use Cases
       ↓
Object Identification
       ↓
Class Model
       ↓
Dynamic Model
       ↓
Behavioural Model
       ↓
Analysis Documentation
       ↓
Design
       ↓
Architecture / Components
       ↓
Integrated Design
       ↓
Implementation

The important word here is:

> INTEGRATION




---

4. Why Integration Matters

Imagine that a team creates these models:

Use-case diagram

Student → Register Course

But the class diagram has no:

Registration

class.

Then the models are incomplete.

Or imagine:

Class diagram

Course
---------
checkCapacity()

But the sequence diagram calls:

verifySeats()

There is a consistency problem.

Or:

Activity diagram

says:

Check payment

but there is no payment-related class, operation or component anywhere else.

Again:

> Something is missing.



Therefore:

> A good OOAD model must be internally consistent.




---

PART B — THE COMPLETE CASE STUDY

5. Case Study: University Online Course Registration System

For this week's major case study, we will use a system familiar to students:

> University Online Course Registration System



The university wants students to register for courses online instead of filling out paper forms.


---

6. Business Problem

The university currently has problems such as:

long registration queues;

lost registration forms;

duplicate registrations;

students registering for courses without prerequisites;

courses exceeding capacity;

delays in confirming registration;

difficulty producing registration reports.


The university therefore wants an online system.


---

7. Business Goal

The goal is to develop a system that allows:

> Students to search for courses, check eligibility, register for courses and receive confirmation electronically.



Academic administrators should also be able to:

create courses;

modify courses;

set course capacity;

view registrations;

close registration;

generate reports.



---

PART C — REQUIREMENTS

8. Functional Requirements

A functional requirement describes something the system must do.

For example:

> "The system shall allow students to log in."



That describes functionality.

For our system:

FR1 — Student Login

The system shall allow students to authenticate.

FR2 — View Courses

The system shall allow students to view available courses.

FR3 — Search Courses

Students shall be able to search for courses.

FR4 — Check Eligibility

The system shall check whether the student satisfies prerequisites.

FR5 — Register

Students shall be able to register for eligible courses.

FR6 — Prevent Duplicate Registration

The system shall prevent a student from registering for the same course twice.

FR7 — Check Capacity

The system shall prevent registration when a course has reached its maximum capacity.

FR8 — Drop Course

Students shall be able to drop a course within the permitted period.

FR9 — Confirmation

The system shall provide registration confirmation.

FR10 — Administration

Administrators shall be able to manage courses.


---

9. Non-Functional Requirements

These describe how well the system should operate.

Examples:

Security

Only authorised users should access protected functionality.

Performance

The system should respond to normal requests within an acceptable time.

Availability

The system should be available during registration periods.

Usability

Students should be able to complete registration without extensive training.

Maintainability

The system should be designed so that future changes can be made without rewriting the entire application.


---

PART D — IDENTIFYING ACTORS

10. What Is an Actor?

An actor is an external role that interacts with the system.

It does not necessarily mean a human being.

An actor can be:

a student;

administrator;

lecturer;

payment service;

email service;

another software system.



---

11. Actors in Our System

We identify:

Student
Administrator
Lecturer
Notification Service

Potentially:

Payment Gateway

if students pay registration fees online.


---

PART E — USE CASE MODEL

12. Student Use Cases

A student might:

Login
View Courses
Search Courses
Register Course
Drop Course
View Registration
Download Registration Confirmation


---

13. Administrator Use Cases

An administrator might:

Login
Create Course
Update Course
Delete Course
Set Course Capacity
View Registrations
Close Registration
Generate Report


---

14. Simplified Use-Case Diagram

Conceptually:

UNIVERSITY SYSTEM
                 ┌─────────────────────────────┐
                 │                             │
Student ─────────┤ Login                       │
                 │ View Courses                 │
Student ─────────┤ Search Courses              │
                 │ Register Course              │
Student ─────────┤ Drop Course                  │
                 │ View Registration             │
                 │                             │
Administrator ───┤ Create Course                │
                 │ Update Course                │
Administrator ───┤ View Registrations           │
                 │ Generate Report              │
                 └─────────────────────────────┘

The exact graphical notation should be produced using a UML tool in the practical session.

The OMG UML specification formally defines UML's modelling constructs, while the UML 2.5.1 specification remains the formal UML reference maintained by OMG. 


---

PART F — FULL USE CASE SPECIFICATION

15. Use Case: Register for Course

Students should not stop at the diagram.

A complete OOAD analysis should document important use cases.

Use Case Name

Register for Course

Primary Actor

Student

Goal

Register for an available course.

Preconditions

Student is authenticated.

Registration period is open.

Student account is active.


Main Success Scenario

1. The student selects "Register Course".

2. The system displays available courses, and the student selects one.

3. The system verifies that the course is open and that the student satisfies its prerequisites.

4. The system checks for an existing active registration.

5. The system atomically reserves a seat. A separate capacity check followed by a later update is not sufficient because simultaneous requests could overbook the final seat.

6. The system creates and saves the Registration in the same transaction as the seat reservation.

7. After the transaction commits, the system sends confirmation and displays the result.




---

16. Alternative Flow — Course Full

Suppose the final seat is claimed by another request before this student's seat reservation is committed.

Student selects course
       ↓
System requests atomic Course.reserveSeat()
       ↓
No seat can be reserved
       ↓
System rejects the request without creating or saving a Registration
       ↓
System displays: "Course is currently full."


---

17. Another Alternative Flow

Suppose the student has not completed the prerequisite.

Student selects course
       ↓
System checks prerequisite
       ↓
Prerequisite NOT satisfied
       ↓
Registration rejected

This becomes important later when we construct the sequence diagram.


---

PART G — IDENTIFYING OBJECTS

18. Candidate Classes

From the requirements, we can identify these domain classes:

Student
Course
Registration
Programme
PrerequisiteRule (if rules are compound)
Administrator
Lecturer

Potential technical/application classes include:

RegistrationController
RegistrationService
StudentRepository
CourseRepository
RegistrationRepository
NotificationService
AuthenticationService

For the worked design, `RegistrationController.requestRegistration(courseCode)` receives the system request, `RegistrationService.registerStudent(studentId, courseCode)` coordinates it, and `NotificationService.sendConfirmation(registration)` sends a message only after the registration transaction commits.

A candidate is not automatically a class: retain a class only when it has a clear domain meaning or software responsibility.


---

19. Domain Classes vs Technical Classes

This distinction is important.

Domain class

Represents something from the problem domain.

Example:

Student
Course
Registration

Technical/application class

Supports implementation.

Example:

RegistrationController
RegistrationRepository
NotificationService

Students should not confuse these. If a sequence diagram uses a design object such as RegistrationService, that object should have a clear responsibility and a corresponding design-class/interface representation.


---

PART H — CLASS MODEL

20. Student

Student
--------------------------------
- studentId : String
- name : String
- email : String
- programme : Programme
- completedCourses : Course[*]
--------------------------------
+ isEligibleFor(course : Course) : Boolean
+ dropCourse(course : Course) : Result
+ viewRegistration() : Registration[*]

Eligibility can depend on completed prerequisites and other explicit university rules. Do not place unrelated persistence or notification work inside Student.


---

21. Course

Course
--------------------------------
- courseCode : String
- courseName : String
- credits : Integer
- capacity : Integer
- enrolledCount : Integer
- status : CourseStatus
--------------------------------
+ isOpen() : Boolean
+ hasCapacity() : Boolean
+ reserveSeat() : Boolean
+ releaseSeat() : void
+ openRegistration() : void
+ closeRegistration() : void

`hasCapacity()` can support a query or display, but the actual booking must use an atomic `reserveSeat()` operation. A separate check followed later by an update can allow two concurrent requests to take the same final seat.


---

22. Registration

Registration
--------------------------------
- registrationId : String
- registrationDate : Date
- status : RegistrationStatus
--------------------------------
+ create(student, course) : Registration
+ confirm() : void
+ cancel() : void

Each Registration refers to exactly one Student and one Course. Keep cancelled registrations as history if the institution requires an audit trail; do not silently delete them.


---

23. RegistrationService

RegistrationService
--------------------------------
+ registerStudent(studentId, courseCode) : Result
+ dropStudent(studentId, courseCode) : Result
+ checkEligibility(student, course) : Boolean
+ checkDuplicate(student, course) : Boolean

The service coordinates the use case. It validates the request, asks the domain objects/repositories for the needed facts, and returns a clear success or rejection result.


---

24. RegistrationRepository

RegistrationRepository
--------------------------------
+ save(registration) : void
+ existsActiveFor(student, course) : Boolean
+ findByStudent(student) : Registration[*]
+ findByCourse(course) : Registration[*]

A preliminary `existsActiveFor()` query is useful for a clear response, but it is not sufficient to prevent simultaneous duplicate requests. Enforce the active `(student, course)` uniqueness rule in the same transaction (for example, with a database unique constraint) and return a clear rejection if it is violated.

Notice what has happened.

We have moved from:

"Register a course"

to a more detailed design:

Controller
     ↓
Service
     ↓
Domain objects
     ↓
Repository

The class model must also show how Student, Course and Registration relate; a sequence diagram must not introduce unexplained operations or objects.


---

PART I — ASSOCIATIONS

25. Student and Registration

A student can have many registrations, while each registration is for exactly one student:

Student 1 ───────── 0..* Registration

Read the multiplicity at each end carefully: one Student may have zero or many Registration records; every Registration links back to one Student.


---

26. Course and Registration

A course can have many registrations, while each registration is for exactly one course:

Course 1 ───────── 0..* Registration

Therefore, Registration resolves the many-to-many relationship between Student and Course:

Student 1 ─── 0..* Registration 0..* ─── 1 Course

A student can register for many courses, and a course can have many students over time. Each individual Registration connects one student with one course. If cancelled registrations are retained, state whether the multiplicities count historical records or only active registrations.


Prerequisites and completed-course history

A student's academic history can be represented by a `completedCourses : Course[*]` association. A course can require zero or more prerequisite courses, and any course may be a prerequisite for many other courses:

```text
Student 0..* --completedCourses--> 0..* Course
Course 0..* --prerequisiteOf--> 0..* Course
```

`Student.isEligibleFor(course)` compares the student's completed-course history with the course's prerequisite rule. If the institution supports complex conditions (such as “Course A and either Course B or Course C”), model those rules explicitly with a `PrerequisiteRule` class rather than hiding the policy in an unexplained Boolean check.


---

PART J — INHERITANCE

27. Should We Use Inheritance?

Suppose the system has:

User
 |
 ├── Student
 ├── Administrator
 └── Lecturer

We might model:

User
----------------
userId
name
email
login()
logout()
        △
        |
 ┌──────┼────────┐
 ↓      ↓        ↓
Student Admin  Lecturer

But students must ask:

> Is inheritance genuinely appropriate?



Do not use inheritance simply because UML allows it.


---

28. Why Inheritance Might Be Useful Here

All three may share:

user ID;

name;

email;

authentication behaviour.


But they have different responsibilities.

Therefore a general User abstraction may be reasonable.


---

PART K — SEQUENCE DIAGRAM

29. Register Course Interaction

Now we ask:

> What happens when the student actually registers?



A sequence diagram should show a complete scenario, including its decision points. This design-level trace is consistent with the classes and operations introduced above:

```text
Student -> RegistrationController: requestRegistration(courseCode)
RegistrationController -> RegistrationService: registerStudent(studentId, courseCode)
RegistrationService -> Student: isEligibleFor(course)
Student --> RegistrationService: eligible / not eligible
RegistrationService -> RegistrationRepository: existsActiveFor(student, course)
RegistrationRepository --> RegistrationService: true / false
RegistrationService -> Course: reserveSeat()
Course --> RegistrationService: seatReserved / full

alt [eligible AND not already registered AND seatReserved]
    RegistrationService -> Registration: create(student, course)
    RegistrationService -> RegistrationRepository: save(registration)
    RegistrationService -> NotificationService: sendConfirmation(registration)
    RegistrationService --> RegistrationController: success
else [prerequisite failed OR duplicate OR course full]
    RegistrationService --> RegistrationController: rejected(reason)
end
RegistrationController --> Student: display result
```

In a detailed UML sequence diagram, use an `alt` combined fragment (or clearly labelled guarded branches) for the success and rejection paths. The class model should contain a reasonable home for each participating design object and message. Send confirmation only after the registration transaction commits.

**Concurrency and integrity rule:** do not rely on `hasCapacity()` followed later by an unrelated increment. `Course.reserveSeat()` must check and claim a seat atomically, or the service must use an equivalent transaction/locking strategy. Also enforce the active-registration uniqueness rule atomically—for example, with a unique `(studentId, courseCode)` constraint or an equivalent transactional operation—because a preliminary duplicate query alone can race. Coordinate seat reservation and persistence in one transaction; if saving fails, release/roll back the claimed seat so the count and registration records cannot diverge. If the last seat has already been claimed, the second request receives `full` and must not create a Registration.


---

30. Why Is This Diagram Important?

Because it tells the developer:

> Which object talks to which other object, in what order, and what happens on success or failure?



The class diagram told us:

> What classes and relationships exist.



The sequence diagram tells us:

> How those classes cooperate in one scenario.



The messages in the sequence must correspond to plausible operations on the lifelines' classes. The state model must allow the resulting state changes; for example, reserving the last seat can move Course from Available to Full.


---

Cross-check with the Activity Workflow

A compatible registration activity is:

```text
Start -> authenticate -> select course -> verify course is open
     -> check prerequisites -> check duplicate registration
     -> reserve seat atomically
     -> create and save Registration
     -> commit seat + Registration transaction
     -> send confirmation -> End
```

At each decision, a failed guard returns a clear rejection and does not create or save a new Registration. The activity diagram focuses on the workflow; the sequence diagram identifies which objects carry it out. These are complementary views, not two independent versions of the same drawing.


---

PART L — STATE MACHINE

31. Course Lifecycle

A course can have different states:

```text
[*] -> Created -> Available -> Full
                          ^       |
                          |       |
                          +-------+
                     [seat released]

Available -> Closed
Full -> Closed
```

The closing transitions occur when the registration period ends. A course may also be closed by an authorised administrator if the business rules allow it.


---

32. State Transitions and Guards

Created -> Available

Event: `openRegistration` from an authorised administrator.

Available -> Full

Event: `reserveSeat` with guard `[enrolledCount == capacity]` after the final seat is successfully claimed.

Full -> Available

Event: `releaseSeat` when a confirmed registration is dropped and a seat becomes available.

Available -> Closed; Full -> Closed

Event: `registrationPeriodEnds`.

The state and the count must agree: `enrolledCount` cannot exceed `capacity`, and a successful atomic reservation is the only operation that may consume a seat. This links the class, state and sequence models.


---

33. Why Not Just Put "Status" in the Class Diagram?

We can have:

status : CourseStatus

in the class.

But that does not explain:

> What causes the status to change?



The state machine supplies event/guard-driven behaviour. The class diagram shows that the state is stored; the sequence/activity models show how a request causes a state transition. This demonstrates why multiple models are useful.


---

PART M — ACTIVITY DIAGRAM

34. Registration Workflow

```text
Initial
  -> Authenticate student
  -> View and select an open course
  -> Check prerequisites
  -> [eligible?]
       No  -> show rejection -> Final
       Yes -> check for an existing active registration
              -> [duplicate?]
                   Yes -> show rejection -> Final
                   No  -> reserve seat atomically
                          -> [seat reserved?]
                               No  -> show course-full message -> Final
                               Yes -> create and save Registration
                                      -> commit seat + Registration transaction
                                      -> send confirmation
                                      -> Final
```

The activity diagram describes the workflow and its alternative paths. The reservation action must be atomic so two concurrent requests cannot both pass a stale capacity check. Confirmation is sent only after the registration transaction commits.


---

PART N — COMPONENT DESIGN

35. From Classes to Components

At design level, we can group related functionality.

For example:

┌─────────────────────────────┐
│ Student Management          │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Course Registration         │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Authentication              │
│ Component                   │
└─────────────────────────────┘

┌─────────────────────────────┐
│ Notification                │
│ Component                   │
└─────────────────────────────┘

UML includes component modelling among its formal modelling constructs. 


---

36. Possible Layered Architecture

The system could be organised as:

┌──────────────────────────┐
│ Presentation Layer       │
│ Web / Mobile Interface   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Application Layer        │
│ Controllers / Services   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Domain Layer             │
│ Student / Course /       │
│ Registration             │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Persistence Layer        │
│ Repositories / Database  │
└──────────────────────────┘

This connects directly with the design and architectural concepts covered previously.


---

PART O — MODEL TRACEABILITY

37. Requirement → Use Case

Requirement:

> Student must register for courses.



↓

Use case:

Register Course


---

38. Use Case → Sequence

Register Course
       ↓
Student
       ↓
RegistrationController
       ↓
RegistrationService
       ↓
Student + RegistrationRepository + Course
       ↓
Registration + NotificationService


---

39. Sequence → Classes

The design-level sequence is supported by these classes/interfaces:

RegistrationController
RegistrationService
Student
RegistrationRepository
Course
Registration
NotificationService

Every design object on the sequence lifelines should have a clear responsibility and a corresponding class or interface in the design model.


---

40. Sequence → Operations

Messages become candidate operations on those lifelines:

requestRegistration(courseCode)
registerStudent(studentId, courseCode)
isEligibleFor(course)
existsActiveFor(student, course)
reserveSeat()
create(student, course)
save(registration)
sendConfirmation(registration)


---

41. Operations → Implementation

Eventually developers can implement these operations in a programming language such as:

Java
C#
Python
C++
Kotlin
TypeScript

The exact language does not change the OOAD principle.


Traceability Matrix — Worked Example

| Requirement | Use case | Design/model evidence | Consistency question |
|---|---|---|---|
| FR4: check prerequisites | Register Course | Student.isEligibleFor(course); guarded success path in the sequence | Does a failed prerequisite stop registration? |
| FR5: register an eligible student | Register Course | RegistrationService.registerStudent(); Registration class; saved Registration | Does the use case lead to a persistent registration? |
| FR6: prevent duplicates | Register Course | RegistrationRepository.existsActiveFor(student, course) plus atomic uniqueness constraint | Is an existing or concurrent duplicate rejected? |
| FR7: enforce capacity | Register Course / Drop Course | Course.reserveSeat() and releaseSeat(); Course state Available/Full | Can concurrent requests exceed capacity? |
| FR9: confirm the result | Register Course | NotificationService.sendConfirmation() after transaction commit | Is confirmation sent only for a successful registration? |
| NFR: protect account access | Login / protected actions | AuthenticationService and role checks at the application boundary | Are privileged actions limited to authorised roles? |

This matrix is a small traceability record, not a requirement to repeat every requirement in every diagram. Trace each requirement to the model element or design decision that satisfies it, and show where it is tested or validated.


---

PART P — CONSISTENCY CHECK

42. Students Should Perform a Model Audit

Give students this checklist.

Use Case ↔ Class Model

Does every major use case have supporting classes?

Class Model ↔ Sequence Diagram

Does every important message correspond to an operation?

Sequence ↔ State Model

Do messages cause appropriate state transitions?

Activity ↔ Sequence

Does the workflow correspond to the interaction?

Class ↔ Component

Are classes sensibly allocated to components?

Requirements ↔ Design

Can we trace each important requirement into the design?


---

43. Example of a Defect

Suppose the activity diagram says:

Check Payment

But:

Class diagram

contains no payment-related class.

Ask:

> How is payment being checked?



Possible solution:

PaymentService
Payment
PaymentGateway

may need to be introduced.

This is model validation.


---

PART Q — FULL ANALYSIS DOCUMENTATION

44. What Should a Complete OOAD Document Contain?

A professional analysis/design document could contain:

Section 1 — Introduction

background;

problem statement;

purpose.


Section 2 — Requirements

functional requirements;

non-functional requirements.


Section 3 — Actors

Identify external roles.

Section 4 — Use Cases

Describe system functionality.

Section 5 — Use-Case Diagram

Visual representation.

Section 6 — Domain/Class Model

Identify important classes.

Section 7 — Interaction Models

Sequence/collaboration diagrams.

Section 8 — Dynamic Model

State diagrams.

Section 9 — Activity Model

Workflows.

Section 10 — Design

Refined classes and responsibilities.

Section 11 — Architecture

Layers/components.

Section 12 — Model Validation

Check consistency.

Section 13 — Conclusion

Summarise the proposed solution.


---

PART R — CASE TOOLS

45. What Is a CASE Tool?

CASE means:

> Computer-Aided Software Engineering.



A CASE tool provides software support for activities such as:

requirements analysis;

modelling;

UML diagram creation;

documentation;

project management;

code-related development activities.


For this course, the important part is:

> Using a tool to create and manage UML models.




---

46. Why Use a CASE Tool?

Imagine drawing 15 UML diagrams manually.

You discover:

> "The class name is wrong in six diagrams."



You have to correct everything manually.

A modelling tool can make model management much easier.

CASE tools can also provide:

diagram editing;

model repositories;

documentation;

consistency support;

project organisation;

sometimes code engineering capabilities.



---

47. Examples of UML/CASE Tools

Examples students may encounter include:

Enterprise Architect;

Visual Paradigm;

StarUML;

Modelio;

diagrams.net/draw.io.


The exact tool is less important than understanding the modelling principles.

For example, the course outline specifically mentions:

> CASE Tool: Select Enterprise Demonstration



Therefore, the practical session should demonstrate a CASE/UML modelling environment rather than teaching students to draw UML only on paper.


---

PART S — CASE TOOL PRACTICAL

48. Practical Demonstration

The lecturer should demonstrate the creation of:

1. Project

University Course Registration

2. Package

Requirements
Analysis
Design

3. Use-case diagram

Add:

Student
Administrator

and use cases.

4. Class diagram

Add:

Student
Course
Registration

etc.

5. Sequence diagram

Model:

> Register Course



6. Activity diagram

Model:

> Registration Process



7. State diagram

Model:

> Course Lifecycle



8. Component diagram

Model:

> System Architecture




---

PART T — HOW STUDENTS SHOULD THINK WHEN USING A CASE TOOL

49. The Tool Does Not Do the Thinking

This is extremely important.

Students should not think:

> "If I learn Enterprise Architect, I know OOAD."



No.

The tool is like Microsoft Word for documentation.

Knowing Word does not mean knowing what to write.

Similarly:

> Knowing a CASE tool does not mean understanding object-oriented analysis and design.



The student must first understand:

Problem
 ↓
Model
 ↓
Design

Then use the CASE tool to represent that model.


---

PART U — COMMON CASE TOOL MISTAKES

50. Mistake 1: Drawing Diagrams Without Requirements

Students sometimes open the tool and immediately start drawing classes.

Correct process:

Requirements
     ↓
Understand system
     ↓
Identify actors
     ↓
Identify use cases
     ↓
Identify objects/classes
     ↓
Create diagrams


---

51. Mistake 2: Creating Too Many Classes

A student might produce:

StudentManager
StudentProcessor
StudentHandler
StudentHelper
StudentUtility
StudentController
StudentService
StudentSystem

without clear justification.

The question should always be:

> What responsibility does this class have?




---

52. Mistake 3: Copying Diagrams From the Internet

A diagram may look professional but still be wrong for the given system.

Students should understand:

> UML notation is standard, but the model must represent your system.




---

53. Mistake 4: Inconsistent Naming

For example:

Class: Registration

but:

Sequence: Enrollment

and:

Database: CourseSignup

Different names can cause confusion.

Establish a consistent vocabulary.


---

PART V — COMPLETE INTEGRATED MODEL

54. The Big Picture

Our system can now be represented as:

UNIVERSITY REGISTRATION SYSTEM
                                      │
                  ┌───────────────────┴──────────────────┐
                  │                                      │
                Student                              Administrator
                  │                                      │
                  ↓                                      ↓
             Use Cases                               Use Cases
                  │                                      │
                  └──────────────────┬───────────────────┘
                                     ↓
                               Analysis Model
                                     │
                     ┌───────────────┼───────────────┐
                     ↓               ↓               ↓
                 Class Model    Dynamic Model   Behaviour Model
                     │               │               │
                     ↓               ↓               ↓
                  Classes          States        Interactions
                     │               │               │
                     └───────────────┼───────────────┘
                                     ↓
                              Design Model
                                     ↓
                              Architecture
                                     ↓
                              Components
                                     ↓
                              Implementation

This is the complete OOAD journey.


---

PART W — TUTORIAL SESSION

55. Tutorial Activity — 1 Hour

Scenario

A college wants an Online Library Management System.

Students should be able to:

search books;

borrow books;

return books;

view borrowed books.


Librarians should be able to:

add books;

remove books;

register members;

view overdue books.



---

Task 1

Identify:

actors;

use cases;

candidate classes.


Task 2

Create a use-case diagram.

Task 3

Create a class diagram.

Task 4

Select:

> Borrow Book



and create a sequence diagram.

Task 5

Create an activity diagram for borrowing.

Task 6

Create a state diagram for:

> Book Copy



Possible states:

Available
    ↓
Borrowed
    ↓
Returned
    ↓
Available

Task 7

Explain how the five diagrams relate.


---

PART X — PRACTICAL SESSION

56. Practical — 1 Hour

Students should use a UML/CASE tool to implement the University Registration case study.

Minimum deliverables

Diagram 1: Use-case diagram

Diagram 2: Class diagram

Diagram 3: Sequence diagram

Diagram 4: Activity diagram

Diagram 5: State-machine diagram

Diagram 6: Component diagram


---

57. Practical Quality Requirements

Students should ensure:

Naming consistency

Registration should not randomly become Enrollment.

Relationships

Every relationship must have a reason.

Multiplicity

Use:

1
0..1
0..*
1..*

where appropriate.

Operations

Sequence messages should correspond to class operations.

Behaviour

State transitions should be triggered by meaningful events.

Requirements

Every major requirement should be represented somewhere in the model.


---

PART Y — INDEPENDENT LEARNING — 10 HOURS

58. Major Week 15 Assignment

Students must select one real-world information system.

Examples:

1. Banking system


2. Hospital management system


3. E-commerce system


4. Library management system


5. Hotel reservation system


6. University registration system


7. Mobile money system


8. Airline reservation system




---

59. Deliverable 1 — Problem Definition

Write:

background;

problem statement;

objectives;

scope.



---

60. Deliverable 2 — Requirements

Provide:

at least 10 functional requirements;

at least 5 non-functional requirements.



---

61. Deliverable 3 — Use Cases

Identify:

actors;

major use cases;

use-case relationships where appropriate.



---

62. Deliverable 4 — Use-Case Diagram

Produce a complete diagram.


---

63. Deliverable 5 — Class Model

At least:

> 10 meaningful classes



Each should have appropriate:

attributes;

operations;

visibility;

relationships.



---

64. Deliverable 6 — Sequence Diagrams

Create at least:

> Two sequence diagrams



for important use cases.


---

65. Deliverable 7 — Activity Diagram

Create at least:

> One activity diagram



for a major workflow.


---

66. Deliverable 8 — State Diagram

Choose an object whose behaviour changes over time.

Examples:

Order
Ticket
Account
Book
Course
Application
Payment


---

67. Deliverable 9 — Component Diagram

Group the system into major components.

For example:

Authentication
Student Management
Course Management
Registration
Notification
Reporting
Database


---

68. Deliverable 10 — Integration Analysis

This is the most important part.

Students must write a section answering:

Question 1

How does the use-case model relate to the class model?

Question 2

How does the sequence diagram relate to class operations?

Question 3

How does the state diagram relate to object behaviour?

Question 4

How does the activity diagram relate to the system workflow?

Question 5

How does the component diagram relate to the classes?

Question 6

How does the complete model support the requirements?


---

PART Z — ASSESSMENT RUBRIC

Area	Marks

Problem definition	5
Requirements	10
Use-case model	10
Class model	15
Sequence diagrams	15
Activity diagram	10
State model	10
Component/design model	10
Model consistency/integration	10
Documentation/presentation	5
Total	100



---

PART AA — EXAMINATION QUESTIONS

Question 1 — 20 Marks

> Explain the purpose of CASE tools in object-oriented analysis and design. Discuss at least five ways in which CASE tools can support software development.




---

Question 2 — 25 Marks

> Using an Online Library Management System as an example, explain how requirements can be transformed into use cases, classes, interactions and a final object-oriented design.




---

Question 3 — 25 Marks

> Explain why UML diagrams should not be developed independently. Using a practical example, demonstrate how a use-case diagram, class diagram, sequence diagram, activity diagram and state-machine diagram can describe different aspects of the same system.




---

Question 4 — 30 Marks

> A university wants an online course registration system. Students can search for courses and register if they have satisfied prerequisites and the course has available capacity. Administrators can manage courses and view registrations.

Develop an object-oriented analysis and design for the system. Your answer should include:

a. Actors
b. Use cases
c. Candidate classes
d. Class relationships
e. Major operations
f. Sequence of registration interactions
g. Course states
h. Registration workflow
i. Components
j. Explanation of how the models remain consistent.




---

PART AB — IMPORTANT DISTINCTIONS STUDENTS MUST KNOW

Concept	What it answers

Requirements	What does the stakeholder need?
Use case	What goal does an actor accomplish?
Class diagram	What structural elements exist?
Object model	What objects/classes and relationships exist?
Sequence diagram	How do objects communicate over time?
Activity diagram	How does a workflow proceed?
State diagram	How does one object change state?
Component diagram	How is functionality organised into components?
Design model	How should the system be structured for implementation?
CASE tool	What software can help us create/manage the models?


This distinction is particularly important because students often lose marks by simply writing:

> "A class diagram shows the system and a sequence diagram shows interaction."



That is too vague.

They should be able to say:

> A class diagram models the structural/static aspects of the system by representing classes, their attributes, operations and relationships, whereas a sequence diagram models a particular interaction scenario by showing the ordered exchange of messages between participating objects.



That is the level expected at Year 3.


---

PART AC — THE "16-YEAR-OLD" EXPLANATION

If I had to explain the whole Week 15 to a 16-year-old:

Imagine you want to build a school management app.

First you ask:

> "What does the school need?"



That's requirements.

Then:

> "Who will use the app and what will they do?"



That's use cases.

Then:

> "What things do we need inside the app?"



That's classes/objects.

Then:

> "How will these things talk to each other?"



That's sequence/interaction modelling.

Then:

> "What happens step by step?"



That's activity modelling.

Then:

> "What happens when an object changes condition?"



That's state modelling.

Then:

> "How do we organise all these pieces into software components?"



That's design/architecture.

Finally:

> "Let's put all of this into a professional UML/CASE tool and make sure everything agrees."



That's Week 15.

So the student should remember:

WHAT?
 ↓
Requirements

WHO?
 ↓
Actors / Use Cases

WHAT THINGS?
 ↓
Classes / Objects

HOW DO THEY TALK?
 ↓
Sequence / Interaction

WHAT HAPPENS STEP-BY-STEP?
 ↓
Activity

HOW DOES SOMETHING CHANGE?
 ↓
State

HOW DO WE ORGANISE THE SOFTWARE?
 ↓
Design / Components

DOES EVERYTHING AGREE?
 ↓
Model Integration

CAN ANOTHER DEVELOPER UNDERSTAND IT?
 ↓
Complete OOAD Documentation


---

PART AD — CONNECTION TO WEEK 14

Week 14 taught:

> How to combine the Object, Dynamic and Behavioural Models into an object-oriented design.



Week 15 now asks:

> Can you actually do it on a complete system?



Therefore:

WEEK 14
Understanding + Integration
        ↓
WEEK 15
Complete Application
        ↓
Requirements
        ↓
Use Cases
        ↓
Classes
        ↓
Interactions
        ↓
Activities
        ↓
States
        ↓
Components
        ↓
Design
        ↓
CASE Tool
        ↓
Complete OOAD Documentation

This progression is intentional. We are not introducing another disconnected topic in Week 15.


---

PART AE — CONNECTION TO WEEK 16

Week 15 is effectively the final major application/project week.

Week 16 should therefore not introduce another large new theoretical topic.

Instead, it should consolidate the entire module through:

comprehensive revision;

examination-oriented questions;

UML notation revision;

common student mistakes;

integrated case-study examination;

practical modelling exercise;

review of the entire 16-week learning journey.


That preserves the original agreement we made at the beginning: 16 weeks, with the final weeks used to consolidate everything rather than rushing the syllabus beyond what was provided.


---

REFERENCES AND CURRENT AUTHORITATIVE SOURCES

1. Object Management Group — UML Specification

The Object Management Group (OMG) maintains the formal UML specification. UML 2.5.1 is listed by OMG as a formal specification, with its adoption dating to December 2017. 

[OMG — Unified Modeling Language Specification](https://www.omg.org/spec/UML/?utm_source=chatgpt.com)

2. UML 2.5.1 Specification

The UML 2.5.1 specification organises UML concepts into structural modelling clauses, behavioural modelling clauses and supplementary concepts including use cases and deployments. This supports the approach used in this week's integrated case study. 

[OMG UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/PDF?utm_source=chatgpt.com)

3. IBM — Unified Process / RUP

IBM documentation describes the Rational Unified Process as having four major phases—Inception, Elaboration, Construction and Transition—and describes iterations as planned intervals within phases. This reinforces the process concepts covered earlier in the module. 

4. IBM Rational Unified Process Best Practices

IBM's RUP material describes Inception as establishing the business case and project scope, while Elaboration focuses on analysing the problem domain, establishing the architectural foundation and addressing high-risk areas. 


---

PRESCRIBED TEXTS FROM THE COURSE OUTLINE

Mach, E. (2019). Object Oriented Analysis & Design Cookbook: Introduction to Practical System Modeling.

Reddy, V. & Korra, S. (2018). Object-Oriented Analysis and Design Using UML.

The Art of Service (2021). Object Oriented Analysis and Design: A Complete Guide.


RECOMMENDED TEXTS

Wixom, B. & Dennis, A. (2018). Systems Analysis and Design.

Blokdyk, G. (2021). Object-Oriented Analysis and Design Standard Requirements.

Wixom, B. & Dennis, A. (2020). Systems Analysis and Design: An Object-Oriented Approach with UML.



---

WEEK 15 — FINAL TAKEAWAY

The single most important lesson is:

> OOAD is not about drawing many UML diagrams. It is about building a coherent model of a software system where requirements, use cases, objects, classes, interactions, behaviour and design decisions all support one another.



A student who can take a completely new problem, move from:

Requirement → Use Case → Class → Interaction → Behaviour → Design → Components → Integrated UML Documentation

has genuinely understood Object-Oriented Analysis and Design.

And that is exactly what Week 15 is designed to test.
