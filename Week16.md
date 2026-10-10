BICT 3202 — OBJECT-ORIENTED ANALYSIS AND DESIGN

WEEK 16: COMPREHENSIVE REVISION, INTEGRATED CASE STUDY AND EXAMINATION PREPARATION

Programme: BSc in Information Communication and Technology
Year of Study: Three
Course Code: BICT 3202
Week: 16 of 16
Module: Object-Oriented Analysis and Design
Lecture Hours: 2
Tutorial Hours: 1
Practical Hours: 1
Independent Learning: 10 hours
Credits: 10


---

1. INTRODUCTION TO WEEK 16

Welcome to the final teaching week of Object-Oriented Analysis and Design.

This week is deliberately different from the previous weeks.

We are not introducing another major isolated topic.

Instead, Week 16 answers the most important question:

> Can the student take everything learned throughout the module and solve a new object-oriented analysis and design problem independently?



That is the purpose of this week.

The official UML specification itself separates UML concepts into structural modelling, behavioural modelling and supplementary concepts such as use cases and deployment. This supports the approach we have followed throughout the module: students should understand how the different UML views work together rather than memorising diagrams independently. 


---

2. WEEK 16 LEARNING OUTCOMES

By the end of Week 16, students should be able to:

1. Explain the fundamental principles of object-oriented analysis and design.


2. Explain the strengths and limitations of object-oriented development.


3. Distinguish analysis from design.


4. Explain the purpose of UML.


5. Identify UML building blocks and major diagram types.


6. Identify actors and use cases from a problem statement.


7. Construct and interpret use-case diagrams.


8. Identify objects and classes.


9. Construct class diagrams.


10. Explain association, aggregation, composition, generalisation and inheritance.


11. Explain polymorphism.


12. Construct dynamic/state models.


13. Construct activity diagrams.


14. Construct sequence diagrams.


15. Construct communication/collaboration diagrams.


16. Explain the Unified Software Development Process.


17. Explain iterations, phases, workflows and artefacts.


18. Explain reuse, generalisation and inheritance within software development.


19. Combine object, dynamic and behavioural models into an object-oriented design.


20. Evaluate the consistency of a complete UML model.


21. Apply OOAD to an unfamiliar real-world problem.


22. Use UML/CASE tools to represent a solution.


23. Answer theoretical and practical examination questions effectively.




---

3. THE ENTIRE MODULE IN ONE PICTURE

Students should be able to reproduce this conceptual journey from memory:

OBJECT-ORIENTED ANALYSIS
                          │
                          ↓
                  Understand the Problem
                          │
                          ↓
                    Business Needs
                          │
                          ↓
                     Requirements
                          │
                          ↓
                       Use Cases
                          │
                          ↓
                 Identify Objects/Classes
                          │
                          ↓
                  OBJECT MODEL
                          │
                          ↓
             ┌────────────┼────────────┐
             ↓            ↓            ↓
        Object Model  Dynamic Model  Behaviour Model
             │            │            │
             │            │            │
          Classes       States      Interactions
        Relationships   Events       Activities
             │            │            │
             └────────────┼────────────┘
                          ↓
                    ANALYSIS MODEL
                          │
                          ↓
                  OBJECT-ORIENTED
                       DESIGN
                          │
                          ↓
              Architecture / Components
                          │
                          ↓
                    Implementation

The student must understand that these are connected stages/views, not unrelated examination topics.


---

PART A — WHAT IS OOAD?

4. Object-Oriented Analysis

Object-oriented analysis asks:

> What does the system need to do, and what objects/classes exist in the problem domain?



Suppose we are developing a library system.

The analyst may identify:

Student
Book
Librarian
Loan
Library

The analyst then investigates:

What does a student do?

What is a book?

How is a book borrowed?

What happens when a book is returned?

Who is allowed to borrow?

What relationships exist between students and loans?


This is analysis.


---

5. Object-Oriented Design

Design asks:

> How should the software be structured so that those requirements can actually be implemented?



For example, analysis might identify:

Student
Book
Loan

Design may introduce:

LoanService
BookRepository
StudentRepository
NotificationService
LoanController

Therefore:

> Analysis focuses primarily on understanding the problem; design focuses on constructing a software solution to that problem.




---

6. Simple Difference Between Analysis and Design

Analysis	Design

Understands the problem	Defines the solution
What does the system need?	How will the system do it?
Identifies domain concepts	Refines them into software structures
Focuses on requirements	Focuses on implementation structure
"What?"	"How?"


Simple example

Client says:

> "Students should be able to borrow books."



Analysis:

Student
Book
Loan
Borrow Book

Design:

LoanController
LoanService
Loan
BookRepository
NotificationService

That distinction is extremely important in examinations.


---

PART B — OBJECT-ORIENTED PRINCIPLES REVISION

7. Object

An object represents a particular entity with:

identity;

state;

behaviour.


Example:

Object:
Student #ST1001

State:
Name = John
Programme = ICT
Year = 3

Behaviour:
registerCourse()
dropCourse()
viewResults()


---

8. Class

A class is a blueprint or definition from which objects can be created.

Example:

Student
-------------------------
studentId
name
programme
-------------------------
registerCourse()
dropCourse()

An actual object might be:

studentId = ST1001
name = John Banda
programme = ICT

So:

> Class = blueprint; object = instance of that blueprint.




---

9. Encapsulation

Encapsulation means keeping an object's data and the operations that control that data together while controlling inappropriate direct access.

Example:

BankAccount
---------------------
- balance
---------------------
+ deposit()
+ withdraw()
+ getBalance()

A customer should not simply do:

balance = -500000

Instead, the object controls how balance changes.


---

10. Abstraction

Abstraction means focusing on important characteristics while hiding unnecessary implementation details.

Example:

When using an ATM, you see:

Withdraw Money
Deposit Money
Check Balance

You do not need to know:

how the database query works
how encryption works
how the bank server communicates

That hidden complexity is abstracted from the user.


---

11. Inheritance

Inheritance allows a specialised class to inherit characteristics from a more general class.

Example:

Person
                △
                |
        ┌───────┴────────┐
        ↓                ↓
     Student          Lecturer

If Person has:

name
email
login()

the subclasses can inherit those characteristics.


---

12. Polymorphism

Polymorphism means that the same operation/interface can produce different behaviour depending on the object involved.

For example:

Employee
   |
   +── calculateSalary()

A:

PermanentEmployee

and:

ContractEmployee

could implement calculateSalary() differently.

Conceptually:

employee.calculateSalary()

can behave differently depending on the actual employee object.


---

PART C — UML REVISION

13. What Is UML?

UML = Unified Modeling Language.

UML is a standard modelling language used to represent and communicate software/system models.

The Object Management Group (OMG) currently lists UML 2.5.1 as a formal UML specification, adopted in December 2017. 

Students should remember:

> UML is a modelling language, not a programming language.




---

14. Why Do We Need UML?

Imagine explaining a complicated banking system using only this paragraph:

> "The customer logs in, selects an account, chooses a transaction, the system checks the balance, validates the transaction, updates the account, records the transaction and sends a notification."



That is difficult to visualise.

Instead, UML can represent:

Customer
   ↓
Login
   ↓
Select Account
   ↓
Make Transaction
   ↓
Validate
   ↓
Update Account
   ↓
Notify Customer

A diagram can make relationships and behaviour easier to communicate.


---

15. UML Diagram Families

For examination purposes, students should understand the major categories.

Structural diagrams

Show what the system is made of.

Examples:

class diagram;

component diagram;

deployment diagram;

package diagram.


Behavioural diagrams

Show what the system does.

Examples:

use-case diagram;

activity diagram;

state-machine diagram.


Interaction diagrams

Focus specifically on communication between participants.

Examples:

sequence diagram;

communication/collaboration diagram.


The formal UML specification similarly organises structural modelling primarily in Clauses 7–12, behavioural modelling in Clauses 13–17, and supplementary concepts such as use cases and deployments in later clauses. 


---

PART D — USE-CASE REVISION

16. What Is a Use Case?

A use case represents a goal that an actor wants to accomplish using the system.

Example:

Actor:
Student

Use case:
Register Course

The use case describes the student's interaction with the system to accomplish that goal.


---

17. Actor vs Use Case

This is a common examination question.

Actor

External role interacting with the system.

Example:

Student

Use case

Goal/function provided by the system.

Example:

Register Course

Therefore:

Student  ─────────  Register Course
 Actor               Use Case


---

18. Common Use-Case Relationships

Association

Shows communication between actor and use case.

<<include>>

Used when one use case always incorporates another required behaviour.

Example:

Register Course
      |
      | <<include>>
      ↓
Check Eligibility

<<extend>>

Used when additional behaviour occurs conditionally.

Example:

Make Payment
      ↑
      |
 <<extend>>
      |
Apply Discount

Students must not use include and extend randomly.


---

PART E — CLASS DIAGRAM REVISION

19. Class Diagram

A class diagram describes the static structure of the system.

Example:

Student
------------------------
- studentId : String
- name : String
- email : String
------------------------
+ registerCourse()
+ dropCourse()


---

20. Attribute

An attribute describes data belonging to a class.

Example:

Student
----------------
studentId
name
email
dateOfBirth


---

21. Operation

An operation describes behaviour/responsibility associated with a class.

Example:

Student
----------------
+ registerCourse()
+ dropCourse()


---

22. Visibility

Students should know the common UML visibility symbols:

+ public
- private
# protected
~ package

Example:

Student
-----------------------
- studentId : String
- name : String
+ getName() : String


---

PART F — RELATIONSHIPS REVISION

23. Association

A general relationship between classes.

Example:

Student ───────── Course

Meaning:

> A student is associated with a course.




---

24. Multiplicity

Multiplicity tells us how many objects can participate.

Example:

Student 1 ─────── 0..* Registration

Meaning:

> One student can have zero or many registration records.



Common multiplicities:

1       exactly one
0..1    zero or one
*       many
0..*    zero or many
1..*    one or many


---

25. Aggregation

Aggregation represents a whole-part relationship where the parts can conceptually exist independently.

Example:

Department ◇──── Lecturer

A lecturer may exist even if the particular department relationship changes.


---

26. Composition

Composition is a stronger whole-part relationship.

Example:

House ◆──── Room

The room is treated as strongly belonging to that particular house in the model.

Students should remember:

> Aggregation = weaker whole-part relationship.



> Composition = stronger ownership/lifecycle relationship.




---

27. Generalisation

Generalisation represents an "is-a" relationship.

Example:

Vehicle
                △
                |
        ┌───────┴───────┐
        ↓               ↓
       Car           Motorcycle

A car is a vehicle.


---

28. Inheritance

Inheritance is the implementation-oriented concept where a subclass receives characteristics from a superclass.

For example:

Vehicle
   ↑
   |
 Car

Car inherits suitable characteristics from Vehicle.

Important examination distinction

Generalisation is the UML modelling relationship.

Inheritance is the object-oriented programming mechanism commonly used to implement such a relationship.


---

PART G — DYNAMIC MODELLING REVISION

29. What Is Dynamic Modelling?

Dynamic modelling describes how the system changes or behaves over time.

Think:

> "What happens?"



rather than:

> "What exists?"




---

30. Event

An event is something that causes a change in behaviour or state.

Example:

Course Registration Opens

can cause:

Closed → Open


---

31. State

A state describes the condition of an object at a particular point.

Example:

Course
------
Open
Closed
Full


---

32. Transition

A transition describes movement from one state to another.

Example:

Available
    |
    | Student registers for final seat
    ↓
Full


---

33. State Diagram Example

┌──────────┐
             │ Created  │
             └────┬─────┘
                  │
                  │ Open registration
                  ↓
             ┌──────────┐
             │ Available│
             └────┬─────┘
                  │
                  │ Last seat taken
                  ↓
             ┌──────────┐
             │   Full   │
             └────┬─────┘
                  │
                  │ Registration closes
                  ↓
             ┌──────────┐
             │  Closed  │
             └──────────┘


---

PART H — BEHAVIOURAL MODELLING REVISION

34. Activity Diagram

An activity diagram models a workflow.

Example:

Start
  ↓
Login
  ↓
Select Course
  ↓
Check Eligibility
  ↓
Eligible?
 ┌──┴──┐
No    Yes
↓      ↓
Reject Check Capacity
          ↓
       Available?
        ┌──┴──┐
       No    Yes
       ↓      ↓
     Reject Register
              ↓
             End


---

35. Sequence Diagram

A sequence diagram focuses on:

> Who communicates with whom, and in what order?



Example:

Student
   |
   | registerCourse()
   ↓
RegistrationController
   |
   | checkEligibility()
   ↓
RegistrationService
   |
   | checkPrerequisite()
   ↓
StudentRecord
   |
   | eligible
   ↓
RegistrationService
   |
   | createRegistration()
   ↓
Registration


---

36. Sequence Diagram vs Activity Diagram

This distinction frequently appears in examinations.

Sequence Diagram	Activity Diagram

Focuses on interactions	Focuses on workflow
Shows participants	Shows activities/actions
Shows message ordering	Shows process flow
Often uses lifelines	Uses activities, decisions and flows


Easy memory trick

> Sequence = Who talks to whom?



> Activity = What happens next?




---

37. Communication/Collaboration Diagram

A communication diagram also models interactions but emphasises:

participating objects;

relationships between them;

messages exchanged.


Example:

Student
   |
1: register()
   ↓
RegistrationController
   |
2: validate()
   ↓
RegistrationService
   |
3: save()
   ↓
Registration

The message numbering helps communicate the interaction order.


---

PART I — FULL MODEL INTEGRATION

38. The Most Important Week 16 Concept

Students should understand this chain:

Requirement
    ↓
Use Case
    ↓
Class/Object
    ↓
Interaction
    ↓
Behaviour
    ↓
Design

Let's use one example.

Requirement

> Students must be able to register for courses.



↓

Use Case

Register Course

↓

Classes

Student
Course
Registration
RegistrationService

↓

Sequence

Student
   ↓
RegistrationService
   ↓
Course
   ↓
Registration

↓

State

Course:
Available → Full

↓

Activity

Select Course
      ↓
Check Eligibility
      ↓
Check Capacity
      ↓
Register

↓

Design

Presentation
      ↓
Application
      ↓
Domain
      ↓
Persistence

That is integrated OOAD.


---

PART J — UML MODEL CONSISTENCY

39. What Does Consistency Mean?

Suppose the class diagram says:

Course
+ checkCapacity()

but the sequence diagram says:

Course.checkAvailableSeats()

We should ask:

> Are these actually the same operation?



If not, the model may be inconsistent.


---

40. Consistency Rules

Students should perform the following checks.

Check 1 — Use Cases ↔ Requirements

Does every important requirement have an appropriate use case?

Check 2 — Use Cases ↔ Classes

Are there classes that can support the use cases?

Check 3 — Sequence ↔ Class

Do messages correspond to valid operations?

Check 4 — Activity ↔ Sequence

Do the workflow and interactions tell compatible stories?

Check 5 — State ↔ Behaviour

Are state transitions caused by meaningful events/operations?

Check 6 — Design ↔ Requirements

Does the final design actually solve the original problem?


---

PART K — UNIFIED SOFTWARE DEVELOPMENT PROCESS REVISION

41. What Is USDP/UP?

The Unified Software Development Process (USDP), commonly associated with the Unified Process, is an iterative and incremental software development approach.

A key concept is that development is divided into phases and iterations rather than assuming the entire system is perfectly specified and built in one uninterrupted sequence.

IBM's documentation describes the Rational Unified Process as having four major phases:

1. Inception


2. Elaboration


3. Construction


4. Transition



It also describes iterations as planned intervals within phases. 


---

42. Inception

Main question:

> Should we build this system?



Activities include:

understanding the business problem;

identifying scope;

identifying major stakeholders;

establishing feasibility;

developing an initial business case.



---

43. Elaboration

Main question:

> Do we understand the problem and architecture well enough to build the system?



Activities include:

detailed requirements analysis;

architecture;

risk analysis;

important use cases;

initial design.



---

44. Construction

Main question:

> Can we build the system?



Activities include:

implementation;

integration;

testing;

refinement.



---

45. Transition

Main question:

> Can users actually use the system?



Activities include:

deployment;

user acceptance;

training;

fixing deployment issues;

moving toward operational use.



---

46. Easy Way to Remember UP Phases

INCEPTION
"Should we build it?"

        ↓

ELABORATION
"How will we build it?"

        ↓

CONSTRUCTION
"Let's build it."

        ↓

TRANSITION
"Let's deliver it."


---

PART L — ITERATIVE DEVELOPMENT

47. What Is an Iteration?

An iteration is a development cycle during which a team produces and evaluates part of the system.

Instead of:

Plan everything
     ↓
Build everything
     ↓
Test everything

an iterative approach may look like:

Iteration 1
Requirements + basic design
       ↓
Feedback

Iteration 2
More functionality
       ↓
Feedback

Iteration 3
More functionality
       ↓
Feedback

Iteration 4
Refinement + testing

IBM's current documentation explicitly describes iterations as planned, measured intervals within project phases and notes that iterations can help teams deliver incremental value to stakeholders. 


---

PART M — REUSE REVISION

48. What Is Software Reuse?

Software reuse means using an existing:

component;

class;

library;

framework;

service;

design;

architecture;


rather than unnecessarily developing everything from scratch.


---

49. Example

Instead of developing your own authentication mechanism from zero, an application might use an established authentication library/service.

Instead of building every UI component from scratch, developers might use a UI framework.

The goal is:

Reuse
 ↓
Less duplication
 ↓
Less development effort
 ↓
Potentially improved consistency
 ↓
Easier maintenance

However:

> Reuse should be based on suitability, security, maintainability, compatibility and licensing—not simply because something already exists.




---

PART N — CASE STUDY FOR FINAL REVISION

50. Scenario: Mobile Money System

A telecommunications company wants to develop a mobile money system.

Users should be able to:

create accounts;

deposit money;

withdraw money;

send money;

receive money;

check balance;

view transaction history.


Agents should be able to:

deposit money for customers;

withdraw money for customers;

view their transactions.


Administrators should be able to:

manage users;

manage agents;

monitor transactions;

generate reports.



---

51. Step 1 — Identify Actors

Possible actors:

Customer
Agent
Administrator
Banking System
Notification Service


---

52. Step 2 — Identify Use Cases

Customer:

Register
Login
Deposit Money
Withdraw Money
Send Money
Receive Money
Check Balance
View Transaction History

Agent:

Login
Deposit for Customer
Withdraw for Customer
View Transactions

Administrator:

Manage Users
Manage Agents
Monitor Transactions
Generate Reports


---

53. Step 3 — Candidate Classes

User
Customer
Agent
Administrator
Wallet
Transaction
Deposit
Withdrawal
Transfer
Notification

Potential services:

AuthenticationService
TransactionService
NotificationService


---

54. Step 4 — Identify Relationships

For example:

User
 △
 |
 ├──────── Customer
 ├──────── Agent
 └──────── Administrator

And:

Customer 1 ───── 1 Wallet

Wallet 1 ───── 0..* Transaction


---

55. Step 5 — Sequence Diagram

For Send Money:

Customer
    |
    | sendMoney()
    ↓
TransferService
    |
    | validateSender()
    ↓
SenderWallet
    |
    | checkBalance()
    ↓
TransferService
    |
    | creditReceiver()
    ↓
ReceiverWallet
    |
    | createTransaction()
    ↓
Transaction
    |
    | sendNotification()
    ↓
NotificationService


---

56. Step 6 — State Model

A transaction might have:

Created
   ↓
Pending
   ↓
Completed

or:

Pending
  ↓
Failed

depending on the result.


---

57. Step 7 — Activity Model

Start
 ↓
Login
 ↓
Enter Recipient
 ↓
Enter Amount
 ↓
Validate Recipient
 ↓
Check Balance
 ↓
Enough Balance?
 ┌──────┴──────┐
 No           Yes
 ↓             ↓
Reject       Transfer
               ↓
          Record Transaction
               ↓
          Send Notification
               ↓
              End


---

58. Step 8 — Design

A possible layered architecture:

┌─────────────────────────────┐
│ Presentation Layer          │
│ Mobile App / Web App        │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ Application Layer           │
│ Controllers / Services      │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ Domain Layer                │
│ Wallet / Transaction / User │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│ Persistence Layer           │
│ Database / Repositories     │
└─────────────────────────────┘


---

PART O — PRACTICAL REVISION

59. Practical Exercise

Students should use a UML/CASE tool to model the mobile money system.

The practical must contain:

Diagram 1

Use-case diagram.

Diagram 2

Class diagram.

Diagram 3

Sequence diagram for:

> Send Money



Diagram 4

Activity diagram for:

> Send Money



Diagram 5

State-machine diagram for:

> Transaction



Diagram 6

Component diagram.


---

60. Practical Challenge

After completing the diagrams, students should deliberately introduce the following error:

The sequence diagram calls:

validateTransaction()

but the class diagram contains:

checkTransaction()

Students must identify the inconsistency and correct it.

This teaches an important professional skill:

> UML modelling is not complete when the diagram looks beautiful; it is complete when the model is logically consistent.




---

PART P — EXAMINATION REVISION

61. Common Theory Questions

Students should prepare for questions such as:

Question 1

Define object-oriented analysis and design.

Question 2

Explain five characteristics of object-oriented systems.

Question 3

Distinguish an object from a class.

Question 4

Explain encapsulation, abstraction, inheritance and polymorphism.

Question 5

What is UML?

Question 6

Explain the difference between structural and behavioural modelling.

Question 7

Explain association, aggregation and composition.

Question 8

Differentiate generalisation from inheritance.

Question 9

Explain the purpose of a use-case diagram.

Question 10

Differentiate sequence and activity diagrams.


---

62. Common Practical Questions

Students may be given a scenario and asked to:

identify actors;

identify use cases;

draw a use-case diagram;

identify classes;

draw a class diagram;

add multiplicities;

identify inheritance;

create a sequence diagram;

create an activity diagram;

create a state diagram;

create a component diagram;

explain relationships between diagrams.



---

PART Q — HOW TO APPROACH AN EXAM SCENARIO

63. Never Start Drawing Immediately

Suppose the examination gives you:

> "A hospital wants a system through which patients can book appointments with doctors."



Do not immediately draw random classes.

Use this process:

STEP 1
Read the problem twice
       ↓
STEP 2
Underline nouns
       ↓
STEP 3
Identify possible objects/classes
       ↓
STEP 4
Identify actors
       ↓
STEP 5
Identify actions/goals
       ↓
STEP 6
Convert major goals into use cases
       ↓
STEP 7
Build use-case diagram
       ↓
STEP 8
Develop class model
       ↓
STEP 9
Choose important scenario
       ↓
STEP 10
Develop sequence diagram
       ↓
STEP 11
Develop activity/state models
       ↓
STEP 12
Check consistency


---

64. Example of the Noun Technique

Problem statement:

> "A patient books an appointment with a doctor. The receptionist manages patient records and doctors have access to their appointment schedules."



Potential nouns:

Patient
Appointment
Doctor
Receptionist
Patient Record
Schedule

Potential verbs:

book
manage
access

Potential use cases:

Book Appointment
Manage Patient Record
View Appointment Schedule

This is not a mechanical rule that every noun must become a class, but it is a useful candidate-identification technique.


---

PART R — COMMON STUDENT MISTAKES

65. Mistake 1 — Confusing Class and Object

Wrong:

> "Student is an object."



Better:

> Student can be a class, while student123 can be an object/instance of that class.




---

66. Mistake 2 — Every Noun Becomes a Class

A scenario might contain:

> "The student quickly registers for a course."



The word "student" may be a candidate class.

But:

> "quickly"



is not a class.

The analyst must use judgement.


---

67. Mistake 3 — Every Verb Becomes a Method

A verb can suggest behaviour, but it does not automatically mean that the corresponding method belongs to a particular class.

Ask:

> Which object has the responsibility to perform this operation?




---

68. Mistake 4 — Confusing Include and Extend

Remember:

Include

Required/reused behaviour.

Register Course
      |
      ↓
<<include>>
Check Eligibility

Extend

Optional/conditional additional behaviour.

Make Payment
      ↑
      |
<<extend>>
Apply Discount


---

69. Mistake 5 — Confusing Aggregation and Composition

Students should not decide based purely on:

> "The diamond looks nice."



Ask:

> What is the ownership/lifecycle relationship between the whole and the part?




---

70. Mistake 6 — Drawing Sequence Diagrams Without Class Diagrams

A sequence diagram should not be treated as an isolated drawing.

If the sequence says:

Course.checkCapacity()

the design/class model should provide a logical place for that responsibility.


---

71. Mistake 7 — Beautiful UML, Wrong Logic

A diagram can be:

neat;

colourful;

perfectly aligned;


and still be wrong.

Examiners award marks for:

> correct modelling, not artistic decoration.




---

PART S — MASTER REVISION TABLE

72. All Major Concepts

Topic	Main Question

Business Needs	Why does the organisation need the system?
Requirements	What does the system need to provide?
Object Orientation	How can the system be viewed as interacting objects?
Object	What individual entity exists?
Class	What defines similar objects?
Encapsulation	How are data and behaviour controlled together?
Abstraction	What details can be hidden?
Inheritance	What can a specialised class inherit?
Polymorphism	How can the same operation behave differently?
UML	How do we communicate the model visually?
Use Case	What goal does an actor accomplish?
Class Diagram	What structure exists?
Association	How are classes related?
Aggregation	What weak whole-part relationship exists?
Composition	What strong whole-part relationship exists?
Generalisation	What is the superclass/subclass relationship?
Dynamic Model	How does the system/object change over time?
State	What condition is an object currently in?
Event	What triggers behaviour/change?
Activity Diagram	What is the workflow?
Sequence Diagram	Who communicates with whom, and when?
Communication Diagram	Which objects communicate and what messages pass between them?
USDP	How can development be organised iteratively?
Reuse	What can be used instead of reinventing it?
Design	How should the solution be structured?
Component	How can functionality be packaged?
CASE Tool	How can modelling be supported by software?
Integration	Do all models tell the same story?



---

PART T — 16-WEEK JOURNEY

73. What Students Have Covered

The module follows the teaching files and course-outline sequence below. Some broad syllabus areas extend across more than one week; the sequence is cumulative rather than a claim that each topic belongs to only one class.

| Week | Teaching focus | What it contributes to the OOAD journey |
|---|---|---|
| 1 | Business needs, software needs and object technology for business | Understand the problem, stakeholders, requirements and why object technology may help. |
| 2 | Principles of object modelling | Identify useful objects, their characteristics and relationships; manage complexity through models. |
| 3 | Modelling language — UML overview | Understand UML, its purpose and major diagram families. |
| 4 | UML building blocks, rules, mechanisms and architecture | Apply UML things, relationships, well-formedness, common mechanisms and metamodel levels. |
| 5 | Object-oriented analysis — object modelling I | Model classes/objects, notation, links, associations and generalisation/specialisation. |
| 6 | Object-oriented analysis — object modelling II | Apply aggregation, inheritance, polymorphism and grouping. |
| 7 | Dynamic modelling | Model events, states, operations, transitions, concurrency and structural/dynamic relationships. |
| 8 | Behavioural modelling | Model use cases, actors, interactions, sequences, communication, activities and analysis documentation. |
| 9 | Unified Software Development Process (USDP/UP) | Organise work through phases, iterations, workflows, artefacts, risk and reuse. |
| 10 | Object-oriented design | Move from analysis toward a solution; integrate object, dynamic and behavioural models. |
| 11 | Refining the object-oriented design | Refine classes, attributes, operations, responsibilities, interfaces, dependencies and design quality. |
| 12 | Integrated object-oriented modelling and design | Check consistency, traceability, validation, packages and integration across models. |
| 13 | Multilayer systems, reusable components and architectural design | Organise layers/components and evaluate reuse, adaptability, cohesion and coupling. |
| 14 | Integrating object, dynamic and behavioural models into design | Transform a coherent analysis into a consistent, implementable design. |
| 15 | Complete OOAD case study and CASE-tool implementation | Apply the complete process to a case and maintain an integrated model. |
| 16 | Comprehensive revision, integrated case study and examination preparation | Consolidate the course and demonstrate independent analysis and design. |

That is the actual 16-week sequence represented by the course materials.


---

PART U — WEEK 16 TUTORIAL

74. Tutorial Exercise

Scenario

A university wants an Online Examination Management System.

Students can:

log in;

view examinations;

start an examination;

answer questions;

submit an examination;

view results.


Lecturers can:

create examinations;

add questions;

publish examinations;

mark examinations;

release results.


Administrators can:

manage students;

manage lecturers;

manage examination schedules.



---

Student Tasks

Task 1

Identify all major actors.

Task 2

Identify at least 10 use cases.

Task 3

Identify at least 10 candidate classes.

Task 4

Create a use-case diagram.

Task 5

Create a class diagram.

Task 6

Choose:

> Start Examination



and create a sequence diagram.

Task 7

Create an activity diagram for:

> Taking an Examination



Task 8

Create a state diagram for:

> Examination



Possible states:

Created
   ↓
Scheduled
   ↓
Open
   ↓
In Progress
   ↓
Submitted
   ↓
Marked
   ↓
Released

Task 9

Identify components.

Task 10

Explain how all diagrams relate.


---

PART V — WEEK 16 PRACTICAL ASSESSMENT

75. Practical Mini-Project

Students should work individually or in small groups.

Choose one:

Hospital Management System

Banking System

Mobile Money System

University Registration System

Library System

Hotel Management System

E-commerce System

Transport Booking System



---

Required Output

Students must submit:

1. Problem Statement
2. Business Objectives
3. Functional Requirements
4. Non-functional Requirements
5. Actors
6. Use Cases
7. Use-case Diagram
8. Class Diagram
9. Sequence Diagram
10. Activity Diagram
11. State Diagram
12. Component Diagram
13. Architecture
14. Model Consistency Analysis
15. Conclusion


---

PART W — EXAMINATION REVISION QUESTION BANK

This is a revision question bank, not a single timed examination: it has no fixed duration, mark allocation or selection rule. Use it for short, untimed recall and discussion. For a full, timed practice sitting, use the generated papers in `output/exams/candidates/` (sources in `exams/`) and the separate examiner's guide (lecturers only).

SECTION A — SHORT ANSWERS

Use these prompts for short-answer recall. For the comparison, essay and case-study sections below, match the depth of your response to the task.

1.

Define object-oriented analysis.

2.

Define object-oriented design.

3.

Distinguish an object from a class.

4.

What is encapsulation?

5.

What is abstraction?

6.

What is polymorphism?

7.

What is inheritance?

8.

What is UML?

9.

What is an actor?

10.

What is a use case?

11.

What is multiplicity?

12.

What is an association?

13.

What is aggregation?

14.

What is composition?

15.

What is generalisation?

16.

What is a state?

17.

What is an event?

18.

What is an activity diagram?

19.

What is a sequence diagram?

20.

What is a CASE tool?


---

SECTION B — DIFFERENTIATE

Question 21

Differentiate:

a. Class vs Object

b. Analysis vs Design

c. Association vs Aggregation

d. Aggregation vs Composition

e. Generalisation vs Inheritance

f. Sequence Diagram vs Activity Diagram

g. Include vs Extend

h. Structural vs Behavioural Modelling


---

SECTION C — LONG ANSWER

Question 22

Explain the four major principles of object-oriented programming:

encapsulation;

abstraction;

inheritance;

polymorphism.


Use a practical example for each.


---

Question 23

Explain the role of UML in object-oriented analysis and design.

Your answer should discuss:

communication;

visualisation;

documentation;

requirements analysis;

system structure;

system behaviour;

design.



---

Question 24

Explain the Unified Software Development Process.

Discuss:

Inception;

Elaboration;

Construction;

Transition;

iterations;

workflows;

artefacts.


When discussing the Unified Process, use the prescribed course texts and explain how phases, iterations, workflows and artefacts support incremental, risk-aware development.


---

SECTION D — CASE STUDY

Question 25

A university wants to develop an online student registration system.

Students can:

log in;

view courses;

check prerequisites;

register for courses;

drop courses;

view their registration.


Administrators can:

create courses;

modify courses;

close registration;

view reports.


Required:

a. Identify the actors.
b. Identify the use cases.
c. Draw a use-case diagram.
d. Identify candidate classes.
e. Draw a class diagram.
f. Identify relationships and multiplicities.
g. Create a sequence diagram for "Register Course".
h. Create an activity diagram for registration.
i. Create a state diagram for Course.
j. Explain how the models are related.


---

Full-length timed practice papers

Two parallel papers are included with this module:

- Paper A — Community Clinic Appointment System: `exams/End-Semester-Exam-Paper-A.md`
- Paper B — Campus Equipment Lending System: `exams/End-Semester-Exam-Paper-B.md`
- Examiner's marking guide (lecturers only): `exams/Examiner-Marking-Guide.md`

Printable PDF and editable Word copies are in `output/exams/candidates/`; the guide is in `output/exams/examiner/`. These are publicly available practice materials, not secure live exam papers.

Each candidate paper uses the same proposed 100-mark structure: Question 1 is compulsory (40 marks), followed by any three of four Section B questions (20 marks each). The candidate-facing total is 100 marks; the examination contributes 60% of the overall module grade under the course outline. The papers are parallel practice forms rather than two exams students must sit.

The course outline does not state a sitting duration. The three-hour duration printed on these drafts is a proposal and must be confirmed against Faculty rules before formal use. Use the marking guide only for moderation and marking; do not distribute it with candidate copies.


---

PART X — EXAM ANSWERING STRATEGY

76. For Definition Questions

Do not write only:

> "Encapsulation is hiding data."



Instead:

> Encapsulation is an object-oriented principle in which data and the operations that manipulate that data are grouped within a class, while access to the internal state is controlled through an appropriate interface.



Then give an example.


---

77. For "Explain" Questions

Use:

Definition
     ↓
Explanation
     ↓
Example
     ↓
Importance

For example:

> Define polymorphism.



Then:

1. Define it.


2. Explain it in simple language.


3. Give a programming/system example.


4. Explain why it is useful.




---

78. For "Compare" Questions

Use a table.

For example:

Feature	Class	Object

Meaning	Blueprint/definition	Instance
Memory	Defines structure	Represents actual instance
Example	Student	Student ST001
Quantity	One class can describe many objects	Many objects can belong to one class


This is much stronger than writing:

> "Class is different from object."




---

79. For UML Questions

Always:

1. identify the requirement;


2. identify actors;


3. identify use cases;


4. identify classes;


5. establish relationships;


6. add behaviour;


7. check consistency.



Do not randomly draw diagrams.


Exam-time and diagram-quality checklist

For the proposed three-hour practice papers, use the mark allocation to plan your time rather than spending too long on one diagram. A possible plan is about 65 minutes for the compulsory 40-mark case, about 32 minutes for each of three 20-mark questions, and the remaining time to read instructions and check answers. Adjust this plan if the approved examination duration differs.

Before handing in a UML answer, check:

- Have I answered the exact task and labelled the system boundary or modelled subject?
- Are actors external roles and use cases actor goals?
- Are class names, attributes, operations, relationships and multiplicities meaningful?
- Do sequence messages have a plausible receiving object and matching design operation?
- Are state changes triggered by events, with guards where a rule is conditional?
- Do the activity, sequence and state models tell compatible stories?
- Have I stated assumptions and business constraints clearly?

The two practice papers are linked in `exams/End-Semester-Exam-Paper-A.md` and `exams/End-Semester-Exam-Paper-B.md`. They are equivalent practice forms, not a requirement to sit both.


---

PART Y — FINAL WEEK 16 TAKEAWAY

The entire module can ultimately be reduced to one question:

> How can we systematically understand a software problem and represent a solution using objects, classes, UML models and an appropriate development process?



The answer is:

BUSINESS PROBLEM
                        ↓
                   REQUIREMENTS
                        ↓
                      ACTORS
                        ↓
                    USE CASES
                        ↓
                  OBJECTS / CLASSES
                        ↓
                   CLASS MODEL
                        ↓
              DYNAMIC / STATE MODEL
                        ↓
              BEHAVIOURAL / INTERACTION
                        ↓
                    ANALYSIS
                        ↓
                     DESIGN
                        ↓
              ARCHITECTURE / COMPONENTS
                        ↓
                 MODEL INTEGRATION
                        ↓
                   IMPLEMENTATION

The student should therefore leave BICT 3202 understanding that:

> Object-Oriented Analysis and Design is not simply about drawing UML diagrams.



It is about thinking systematically about a software problem, identifying the things that matter, understanding how those things interact and behave, and then transforming that understanding into a coherent design that developers can implement.


---

80. FINAL REVISION CHECKLIST

Before sitting for the examination, every student should be able to answer YES to the following:

Business and Requirements

[ ] Can I distinguish a business problem, business need, requirement and solution?

[ ] Can I identify stakeholders and write functional and measurable non-functional requirements?

[ ] Can I trace a requirement to a use case and model element?

Object Orientation

[ ] Can I define an object?

[ ] Can I define a class?

[ ] Can I explain encapsulation?

[ ] Can I explain abstraction?

[ ] Can I explain inheritance?

[ ] Can I explain polymorphism?


UML

[ ] Can I explain UML?

[ ] Can I distinguish structural and behavioural diagrams?

[ ] Can I identify the purpose of each major diagram?


Use Cases

[ ] Can I identify actors?

[ ] Can I identify use cases?

[ ] Can I use include correctly?

[ ] Can I use extend correctly?


Class Modelling

[ ] Can I identify classes?

[ ] Can I identify attributes?

[ ] Can I identify operations?

[ ] Can I identify associations?

[ ] Can I assign multiplicities?

[ ] Can I explain aggregation?

[ ] Can I explain composition?

[ ] Can I model generalisation?


Dynamic Modelling

[ ] Can I identify events?

[ ] Can I identify states?

[ ] Can I model transitions?

[ ] Can I explain concurrency?


Behavioural Modelling

[ ] Can I create an activity diagram?

[ ] Can I create a sequence diagram?

[ ] Can I create a communication diagram?

[ ] Can I explain the difference between them?


USDP

[ ] Can I explain Inception?

[ ] Can I explain Elaboration?

[ ] Can I explain Construction?

[ ] Can I explain Transition?

[ ] Can I explain iterations?

[ ] Can I explain workflows?

[ ] Can I explain artefacts?


Design

[ ] Can I distinguish analysis from design?

[ ] Can I combine object, dynamic and behavioural models?

[ ] Can I identify components?

[ ] Can I explain layered architecture?

[ ] Can I explain software reuse?


Practical

[ ] Can I use a UML/CASE tool?

[ ] Can I model a new system from scratch?

[ ] Can I check consistency between diagrams?


Examination

[ ] Can I explain concepts in my own words?

[ ] Can I give examples?

[ ] Can I draw UML diagrams?

[ ] Can I analyse an unfamiliar case study?

[ ] Can I justify my modelling decisions?



---

81. FINAL REFERENCE BASE

For technical UML notation and semantics, use the Object Management Group's UML 2.5.1 specification as the standard reference.

[OMG — UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/)

For the Unified Process, consult the prescribed course texts and lecturer-approved references, paying attention to phases, iterations, workflows and artefacts.

The prescribed and recommended textbooks from the university course outline should remain the primary course-reading materials; the OMG specification can be used to verify technical UML details.


---

82. CONCLUSION OF THE 16-WEEK MODULE

Week 1 established business/software needs and object technology; Week 2 developed object-modelling principles; Weeks 3–4 introduced and formalised UML; Weeks 5–6 developed structural object modelling; Week 7 modelled dynamic behaviour; Week 8 modelled use cases and interactions; and Week 9 covered the Unified Software Development Process.

Weeks 10–12 moved into object-oriented design, refinement and integrated modelling. Weeks 13–14 developed multilayer architecture, reusable components and model integration. Week 15 applied these ideas in a complete OOAD case study and CASE-tool exercise.

And now:

WEEK 16 — THE STUDENT BECOMES THE ANALYST/DESIGNER

Instead of being told:

> "Here is a class diagram. Explain it."



the student should now be capable of being told:

> "Here is a real-world problem. Analyse it and design the system."



And independently produce:

Requirements → Actors → Use Cases → Classes → Relationships → Interactions → Behaviour → Architecture → Components → Integrated UML Model.

That is the intended culmination of BICT 3202 Object-Oriented Analysis and Design.
