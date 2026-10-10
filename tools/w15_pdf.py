"""
Week 15 PDF content — COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 15,
    "title": "Complete OOAD Case Study, Model Integration and CASE Tool Implementation",
    "filename": "Week15_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Week 15 Theme"))
    s += [P("Week 15 is the <b>integration and application week</b>. Students now take the concepts "
            "developed from Weeks 1–14 and apply them to a complete system. The emphasis is not simply "
            "on drawing UML diagrams, but on demonstrating that the diagrams <b>tell a consistent story "
            "and can guide implementation</b>."),
          P("The central question is: <i>“If I am given a real software problem today, can I use "
            "everything I have learned to analyse it, model it, design it and communicate the design to "
            "another developer?”</i> By now, use-case, class, sequence, activity, state and component "
            "diagrams should no longer feel like separate examination topics — they are different views "
            "of one software system.")]
    s += FIG("w15_progression.png", "Figure 1 — Week 14 -> Week 15")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Analyse a complete software problem using object-oriented techniques.",
        "Identify stakeholders and system actors; extract functional and non-functional requirements.",
        "Identify appropriate use cases and construct a use-case model.",
        "Identify candidate classes and develop a conceptual/domain class model.",
        "Refine the analysis model into a design model; identify class responsibilities.",
        "Define attributes, operations, associations, inheritance and composition.",
        "Develop interaction, activity and state-machine models for important behaviours.",
        "Develop a component-level view; check consistency between UML models.",
        "Document a complete OOAD solution and use a CASE/UML tool to organise models.",
        "Explain how the final design could be implemented.",
    ])

    # PART A — looking back -------------------------------------------------------
    s.append(H1("PART A — WHAT HAVE WE BEEN LEARNING?"))
    s.append(H1("3.  Looking Back at the Entire Module"))
    s += [P("The OOAD process can be simplified as a journey: Business Problem -> Requirements -> Use "
            "Cases -> Object Identification -> Class Model -> Dynamic Model -> Behavioural Model -> Analysis "
            "Documentation -> Design -> Architecture/Components -> Integrated Design -> Implementation. "
            "The single most important word is <b>INTEGRATION</b>.")]
    s += FIG("w15_process.png", "Figure 2 — The OOAD journey")

    s.append(H1("4.  Why Integration Matters"))
    s += [P("If the use-case diagram shows <font name='Mono'>Student -> Register Course</font> but the "
            "class diagram has no <font name='Mono'>Registration</font> class, the models are incomplete. "
            "If the class diagram says <font name='Mono'>Course.checkCapacity()</font> but the sequence "
            "diagram calls <font name='Mono'>verifySeats()</font>, there is a consistency problem. If the "
            "activity diagram says “Check payment” but no payment-related class, operation or component "
            "exists anywhere, something is missing. Therefore: <b>a good OOAD model must be internally "
            "consistent.</b>")]
    s += FIG("w15_consistency.png", "Figure 3 — Why integration matters")

    # PART B — case study intro -------------------------------------------------------
    s.append(H1("PART B — THE COMPLETE CASE STUDY"))
    s.append(H1("5.  Case Study: University Online Course Registration System"))
    s += [P("The university wants students to register for courses online instead of filling out paper "
            "forms. Today it suffers from long queues, lost forms, duplicate registrations, students "
            "registering without prerequisites, courses exceeding capacity, delayed confirmation and "
            "poor reporting."),
          P("<b>Business goal:</b> students should search for courses, check eligibility, register and "
            "receive confirmation electronically; administrators should create/modify courses, set "
            "capacity, view registrations, close registration and generate reports.")]
    s += FIG("w15_business_problem.png", "Figure 4 — The business problem and goal")

    # PART C — requirements -------------------------------------------------------
    s.append(H1("PART C — REQUIREMENTS"))
    s.append(H1("6.  Functional and Non-Functional Requirements"))
    s += [P("A <b>functional requirement</b> describes something the system must do. For this system: "
            "<font name='Mono'>FR1</font> student login, <font name='Mono'>FR2</font> view courses, "
            "<font name='Mono'>FR3</font> search courses, <font name='Mono'>FR4</font> check "
            "eligibility, <font name='Mono'>FR5</font> register, <font name='Mono'>FR6</font> prevent "
            "duplicate registration, <font name='Mono'>FR7</font> check capacity, <font name='Mono'>FR8"
            "</font> drop course, <font name='Mono'>FR9</font> confirmation, <font name='Mono'>FR10"
            "</font> administration."),
          P("A <b>non-functional requirement</b> describes how well the system operates: security "
            "(authorised access only), performance (acceptable response time), availability (up during "
            "registration periods), usability (no extensive training) and maintainability (future "
            "changes without a rewrite).")]
    s += FIG("w15_requirements.png", "Figure 5 — Functional vs non-functional requirements")

    # PART D — actors -------------------------------------------------------
    s.append(H1("PART D — IDENTIFYING ACTORS"))
    s.append(H1("7.  What Is an Actor?"))
    s += [P("An <b>actor</b> is an external role that interacts with the system — not necessarily a "
            "human. Actors can be a student, administrator, lecturer, payment service, email service or "
            "another software system. For our system we identify: <b>Student, Administrator, Lecturer, "
            "Notification Service</b> and (potentially) <b>Payment Gateway</b>.")]
    s += FIG("w15_actors.png", "Figure 6 — Actors in the system")

    # PART E — use-case model -------------------------------------------------------
    s.append(H1("PART E — USE-CASE MODEL"))
    s.append(H1("8.  Student and Administrator Use Cases"))
    s += [P("A <b>student</b> might: Login, View Courses, Search Courses, Register Course, Drop Course, "
            "View Registration, Download Registration Confirmation. An <b>administrator</b> might: "
            "Login, Create Course, Update Course, Delete Course, Set Course Capacity, View "
            "Registrations, Close Registration, Generate Report.")]
    s += FIG("w15_use_case_diagram.png", "Figure 7 — Simplified use-case diagram")

    # PART F — use-case specification -------------------------------------------------------
    s.append(H1("PART F — FULL USE-CASE SPECIFICATION"))
    s.append(H1("9.  Use Case: Register for Course"))
    s += [P("<b>Name:</b> Register for Course · <b>Primary Actor:</b> Student · <b>Goal:</b> register "
            "for an available course · <b>Preconditions:</b> authenticated, registration period open, "
            "account active."),
          P("<b>Main success scenario:</b> (1) the student selects an open course; (2) the system checks "
            "prerequisites and rejects an active duplicate; (3) <font name='Mono'>Course.reserveSeat()</font> "
            "atomically claims a seat; (4) the system creates and saves the Registration in the same "
            "transaction; (5) after the transaction commits, the system sends confirmation and displays the result."),
          P("<b>Alternative flows:</b> if the prerequisite fails, a duplicate exists or no seat can be "
            "reserved, the system rejects the request without creating or saving a new Registration. "
            "If persistence fails after a seat claim, the transaction rolls the claim back. These alternatives "
            "are shown in the sequence/activity models.")]
    s += FIG("w15_use_case_spec.png", "Figure 8 — Use-case specification")

    # PART G — identifying objects -------------------------------------------------------
    s.append(H1("PART G — IDENTIFYING OBJECTS"))
    s.append(H1("10.  Candidate Classes"))
    s += [P("From the requirements we identify <b>domain classes</b> — Student, Course, Registration, "
            "Programme, a PrerequisiteRule where policy is complex, Administrator and Lecturer — and "
            "<b>technical/application classes</b> — RegistrationController, RegistrationService, "
            "StudentRepository, CourseRepository, RegistrationRepository, NotificationService and "
            "AuthenticationService. Domain classes represent the problem domain; technical classes "
            "support implementation. <b>Do not confuse these.</b>")]
    s += FIG("w15_candidate_classes.png", "Figure 9 — Domain vs technical classes")

    # PART H — class model -------------------------------------------------------
    s.append(H1("PART H — CLASS MODEL"))
    s.append(H1("11.  The Design Classes"))
    s += [P("Refined design classes include: <font name='Mono'>Student</font> (studentId, name, email, "
            "programme, completedCourses; isEligibleFor(course), dropCourse()), <font name='Mono'>Course</font> "
            "(courseCode, courseName, credits, capacity, enrolledCount, status; prerequisite self-association, "
            "hasCapacity(), "
            "reserveSeat(), releaseSeat()), <font name='Mono'>Registration</font> (registrationId, "
            "registrationDate, status; create(student, course), confirm(), cancel()), "
            "<font name='Mono'>RegistrationService</font> "
            "(registerStudent(), dropStudent(), checkEligibility(), checkDuplicate()) and "
            "<font name='Mono'>RegistrationRepository</font> (save(), existsActiveFor(), findByStudent(), "
            "findByCourse()). A complex prerequisite policy can have its own <font name='Mono'>PrerequisiteRule</font> "
            "class. Notice the movement from “register a course” to a detailed design: "
            "<b>Controller -> Service -> Domain objects -> Repository.</b> The model should state that "
            "each Registration connects exactly one Student and one Course. A database uniqueness constraint or "
            "equivalent transaction must prevent concurrent duplicate active registrations.")]
    s += FIG("w15_class_model.png", "Figure 10 — The class model")

    # PART I — associations -------------------------------------------------------
    s.append(H1("PART I — ASSOCIATIONS"))
    s.append(H1("12.  Student, Course and Registration"))
    s += [P("A student can have many registrations: <font name='Mono'>Student 1 — 0..* Registration"
            "</font> — one student may have zero or many registration records. A course can have many "
            "registrations: <font name='Mono'>Course 1 — 0..* Registration</font>. The Student-to-Course "
            "completed-course association supports prerequisite checks; Course can also have a recursive "
            "prerequisite association with explicit target/prerequisite roles. Use a <font name='Mono'>PrerequisiteRule</font> "
            "class if policy has compound conditions. Combined, these relationships are more meaningful "
            "than simply drawing lines between classes — <b>students must understand the multiplicity.</b>")]
    s += FIG("w15_associations.png", "Figure 11 — Associations and multiplicity")

    # PART J — inheritance -------------------------------------------------------
    s.append(H1("PART J — INHERITANCE"))
    s.append(H1("13.  Should We Use Inheritance?"))
    s += [P("Student, Administrator and Lecturer all share a user ID, name, email and authentication "
            "behaviour, but have different responsibilities — so a general <font name='Mono'>User"
            "</font> abstraction with <font name='Mono'>Student</font>, <font name='Mono'>Administrator"
            "</font> and <font name='Mono'>Lecturer</font> as specialisations may be reasonable. "
            "However, <b>do not use inheritance simply because UML allows it</b> — it must be genuinely "
            "appropriate.")]
    s += FIG("w15_inheritance.png", "Figure 12 — Inheritance: a shared User abstraction")

    # PART K — sequence diagram -------------------------------------------------------
    s.append(H1("PART K — SEQUENCE DIAGRAM"))
    s.append(H1("14.  Register Course Interaction"))
    s += [P("Student sends <font name='Mono'>requestRegistration(courseCode)</font> to "
            "<font name='Mono'>RegistrationController</font>, which calls "
            "<font name='Mono'>RegistrationService.registerStudent()</font>. The service checks "
            "eligibility, asks <font name='Mono'>RegistrationRepository.existsActiveFor()</font> to "
            "reject duplicates, then calls <font name='Mono'>Course.reserveSeat()</font>. Only when "
            "the guarded checks succeed does it create and save <font name='Mono'>Registration</font> "
            "and send confirmation through <font name='Mono'>NotificationService</font> only after the "
            "registration transaction commits. An <font name='Mono'>alt</font> fragment shows the rejection "
            "path. <b>reserveSeat() must be "
            "atomic:</b> a separate capacity check followed by a later update can overbook the final "
            "seat under concurrent requests. Enforce duplicate prevention atomically too: an existence query alone "
            "can race, so use a unique active-registration constraint or equivalent transaction. Coordinate "
            "seat reservation and save in one transaction; if persistence fails, roll the seat back. The "
            "class diagram shows <i>what exists</i>; the sequence "
            "diagram shows <i>how those classes cooperate</i>.")]
    s += FIG("w15_sequence.png", "Figure 13 — Sequence diagram: Register Course")

    # PART L — state machine -------------------------------------------------------
    s.append(H1("PART L — STATE MACHINE"))
    s.append(H1("15.  Course Lifecycle"))
    s += [P("A course moves through <font name='Mono'>Created -> Available -> Full -> Closed</font>. "
            "Transitions: <b>Created -> Available</b> when an authorised administrator opens registration; "
            "<b>Available -> Full</b> when an atomic <font name='Mono'>reserveSeat()</font> succeeds for "
            "the final seat; <b>Full -> Available</b> when a seat is released; and <b>Available/Full -> "
            "Closed</b> when the registration period ends. Keep the guard and capacity invariant in view: "
            "<font name='Mono'>enrolledCount <= capacity</font>."),
          P("We can put <font name='Mono'>status : CourseStatus</font> in the class, but that does not "
            "explain <i>what causes the status to change</i>. The state machine supplies that dynamic "
            "information and should agree with the sequence diagram.")]
    s += FIG("w15_state_machine.png", "Figure 14 — Course lifecycle state machine")

    # PART M — activity diagram -------------------------------------------------------
    s.append(H1("PART M — ACTIVITY DIAGRAM"))
    s.append(H1("16.  Registration Workflow"))
    s += [P("The workflow: Start -> authenticate -> select open course -> check prerequisites -> "
            "<i>[eligible?]</i> No -> reject / Yes -> check for duplicate -> <i>[already registered?]</i> "
            "Yes -> reject / No -> atomically reserve a seat -> <i>[seat reserved?]</i> No -> report full / "
            "Yes -> create and save Registration in the seat transaction -> commit -> send confirmation -> End. "
            "The activity diagram describes "
            "workflow decisions; the sequence diagram assigns those actions to objects. A failed guard "
            "must not create or save a new Registration.")]
    s += FIG("w15_activity.png", "Figure 15 — Registration workflow activity diagram")

    # PART N — component design -------------------------------------------------------
    s.append(H1("PART N — COMPONENT DESIGN"))
    s.append(H1("17.  From Classes to Components"))
    s += [P("At design level we group related functionality into components — Student Management, "
            "Course Registration, Authentication and Notification — and organise the system into "
            "layers: <b>Presentation</b> (web/mobile interface), <b>Application</b> "
            "(controllers/services), <b>Domain</b> (Student/Course/Registration) and <b>Persistence</b> "
            "(repositories/database). This connects directly with the architectural concepts covered "
            "earlier in the module.")]
    s += FIG("w15_components.png", "Figure 16 — Components and layered architecture")

    # PART O — traceability -------------------------------------------------------
    s.append(H1("PART O — MODEL TRACEABILITY"))
    s.append(H1("18.  Requirement -> Implementation"))
    s += [P("Trace FR5 (register an eligible student) from the <font name='Mono'>Register Course</font> "
            "use case to <font name='Mono'>RegistrationService.registerStudent()</font>, the "
            "<font name='Mono'>Registration</font> class and its save operation. Trace FR6 (prevent "
            "duplicates) to <font name='Mono'>existsActiveFor()</font> and its guarded rejection path; "
            "trace FR7 (capacity) to atomic <font name='Mono'>Course.reserveSeat()</font> and the "
            "Available/Full state transition. NFRs such as role-based access should map to the "
            "authentication boundary and test evidence. This is stronger than a one-way diagram list: "
            "each requirement has a model/design element and a way to validate it.")]
    s += FIG("w15_traceability.png", "Figure 17 — Model traceability")

    # PART P — consistency check -------------------------------------------------------
    s.append(H1("PART P — CONSISTENCY CHECK"))
    s.append(H1("19.  Performing a Model Audit"))
    s += BUL([
        "<b>Use Case <-> Class Model:</b> does every major use case have supporting classes?",
        "<b>Class Model <-> Sequence Diagram:</b> does every important message correspond to an operation?",
        "<b>Sequence <-> State Model:</b> do messages cause appropriate state transitions?",
        "<b>Activity <-> Sequence:</b> does the workflow correspond to the interaction?",
        "<b>Class <-> Component:</b> are classes sensibly allocated to components?",
        "<b>Requirements <-> Design:</b> can each important requirement be traced into the design?",
    ])
    s += [P("<b>Example defect:</b> if the activity diagram says “Check Payment” but the class diagram "
            "contains no payment-related class, ask “how is payment being checked?” — the solution may "
            "require introducing <font name='Mono'>PaymentService</font>, <font name='Mono'>Payment"
            "</font> and <font name='Mono'>PaymentGateway</font>. This is model validation.")]

    # PART Q — documentation -------------------------------------------------------
    s.append(H1("PART Q — FULL ANALYSIS DOCUMENTATION"))
    s.append(H1("20.  What Should a Complete OOAD Document Contain?"))
    s += BUL([
        "Introduction (background, problem statement, purpose).",
        "Requirements (functional and non-functional).",
        "Actors and use cases (with the use-case diagram).",
        "Domain/class model (important classes).",
        "Interaction models (sequence/collaboration diagrams).",
        "Dynamic model (state diagrams) and activity model (workflows).",
        "Design (refined classes and responsibilities) and architecture (layers/components).",
        "Model validation (consistency) and conclusion.",
    ])

    # PART R — CASE tools -------------------------------------------------------
    s.append(H1("PART R — CASE TOOLS"))
    s.append(H1("21.  What Is a CASE Tool?"))
    s += [P("<b>CASE</b> means Computer-Aided Software Engineering. A CASE tool provides software "
            "support for requirements analysis, modelling, UML diagram creation, documentation, project "
            "management and code-related development activities. For this course the important part is "
            "<b>using a tool to create and manage UML models</b>."),
          P("Imagine drawing 15 UML diagrams manually and then discovering “the class name is wrong in "
            "six diagrams” — you would have to correct everything by hand. A modelling tool makes model "
            "management much easier through diagram editing, model repositories, documentation, "
            "consistency support, project organisation and sometimes code engineering."),
          P("<b>Examples:</b> Enterprise Architect, Visual Paradigm, StarUML, Modelio, and "
            "diagrams.net/draw.io. The exact tool matters less than understanding the modelling "
            "principles; the course outline specifically mentions a <b>CASE Tool: Select Enterprise "
            "Demonstration</b>.")]

    # PART S/T — practical & thinking -------------------------------------------------------
    s.append(H1("PART S &amp; T — CASE TOOL PRACTICAL AND THE RIGHT MINDSET"))
    s.append(H1("22.  Practical Demonstration and How to Think"))
    s += [P("In the practical session, the lecturer demonstrates creating: (1) the project "
            "“University Course Registration”; (2) packages for Requirements, Analysis and Design; "
            "(3) the use-case diagram; (4) the class diagram; (5) the sequence diagram for Register "
            "Course; (6) the activity diagram for the Registration Process; (7) the state diagram for "
            "the Course Lifecycle; and (8) the component diagram for the System Architecture."),
          P("<b>The tool does not do the thinking.</b> Knowing Enterprise Architect is like knowing "
            "Microsoft Word — knowing Word does not mean knowing what to write, and knowing a CASE tool "
            "does not mean understanding object-oriented analysis and design. The student must first "
            "understand <font name='Mono'>Problem -> Model -> Design</font>, then use the tool to "
            "represent that model.")]

    # PART U — common mistakes -------------------------------------------------------
    s.append(H1("PART U — COMMON CASE-TOOL MISTAKES"))
    s.append(H1("23.  Four Classic Mistakes"))
    s += BUL([
        "<b>Drawing diagrams without requirements</b> — opening the tool and immediately drawing classes; the correct order is requirements -> understand system -> actors -> use cases -> classes -> diagrams.",
        "<b>Creating too many classes</b> — StudentManager, StudentProcessor, StudentHandler, StudentHelper…; always ask: what responsibility does this class have?",
        "<b>Copying diagrams from the internet</b> — UML notation is standard, but the model must represent your system.",
        "<b>Inconsistent naming</b> — class “Registration” but sequence “Enrollment” and database “CourseSignup”; establish a consistent vocabulary.",
    ])

    # PART V — integrated model -------------------------------------------------------
    s.append(H1("PART V — COMPLETE INTEGRATED MODEL"))
    s.append(H1("24.  The Big Picture"))
    s += [P("Student and Administrator act on Use Cases, which feed the Analysis Model; the analysis "
            "branches into the Class Model (classes), Dynamic Model (states) and Behavioural Model "
            "(interactions); these converge into the Design Model, then Architecture, then Components, "
            "then Implementation. <b>This is the complete OOAD journey.</b>")]
    s += FIG("w15_integrated.png", "Figure 18 — The complete OOAD journey")

    # PART W — tutorial -------------------------------------------------------
    s.append(H1("PART W — TUTORIAL SESSION (1 HOUR)"))
    s.append(H1("25.  Tutorial: Online Library Management System"))
    s += [P("A college wants an Online Library Management System. <b>Students</b> can search, borrow, "
            "return and view borrowed books. <b>Librarians</b> can add books, remove books, register "
            "members and view overdue books."),
          P("<b>Tasks:</b> (1) identify actors, use cases and candidate classes; (2) create the use-case "
            "diagram; (3) create the class diagram; (4) select “Borrow Book” and create a sequence "
            "diagram; (5) create an activity diagram for borrowing; (6) create a state diagram for Book "
            "Copy (Available -> Borrowed -> Returned -> Available); (7) explain how the five diagrams "
            "relate.")]

    # PART X — practical -------------------------------------------------------
    s.append(H1("PART X — PRACTICAL SESSION (1 HOUR)"))
    s.append(H1("26.  Practical Deliverables and Quality Requirements"))
    s += [P("Using a UML/CASE tool, implement the University Registration case study with six diagrams: "
            "use-case, class, sequence, activity, state-machine and component."),
          P("<b>Quality requirements:</b> naming consistency (Registration should not randomly become "
            "Enrollment); every relationship must have a reason; multiplicity (1, 0..1, 0..*, 1..*) used "
            "where appropriate; sequence messages must correspond to class operations; state transitions "
            "triggered by meaningful events; every major requirement represented somewhere in the model.")]

    # PART Y — independent learning -------------------------------------------------------
    s.append(H1("PART Y — INDEPENDENT LEARNING (10 HOURS)"))
    s.append(H1("27.  Major Week 15 Assignment — Ten Deliverables"))
    s += [P("Select one real-world information system (banking, hospital management, e-commerce, "
            "library, hotel reservation, university registration, mobile money or airline reservation) "
            "and produce:"),
          P("(1) a problem definition (background, problem statement, objectives, scope); (2) at least "
            "10 functional and 5 non-functional requirements; (3) actors and major use cases with "
            "relationships; (4) a complete use-case diagram; (5) a class model of at least 10 meaningful "
            "classes with attributes, operations, visibility and relationships; (6) at least two sequence "
            "diagrams for important use cases; (7) at least one activity diagram; (8) a state diagram "
            "for a state-dependent object (Order, Ticket, Account, Book, Course, Application or "
            "Payment); (9) a component diagram (Authentication, Student Management, Course Management, "
            "Registration, Notification, Reporting, Database); and (10) an integration analysis answering "
            "how the use-case model relates to the class model, how the sequence relates to operations, "
            "how the state relates to behaviour, how the activity relates to the workflow, how the "
            "component relates to the classes, and how the complete model supports the requirements.")]

    # PART Z — assessment rubric -------------------------------------------------------
    s.append(H1("PART Z — ASSESSMENT RUBRIC (100 MARKS)"))
    s.append(DTABLE(
        ["Area", "Marks"],
        [["Problem definition", "5"],
         ["Requirements", "10"],
         ["Use-case model", "10"],
         ["Class model", "15"],
         ["Sequence diagrams", "15"],
         ["Activity diagram", "10"],
         ["State model", "10"],
         ["Component/design model", "10"],
         ["Model consistency/integration", "10"],
         ["Documentation/presentation", "5"],
         ["Total", "100"]],
        widths=[0.7 * DOC_W, 0.3 * DOC_W]))

    # PART AB — distinctions -------------------------------------------------------
    s.append(H1("28.  Important Distinctions Students Must Know"))
    s.append(DTABLE(
        ["Concept", "What it answers"],
        [["Requirements", "What does the stakeholder need?"],
         ["Use case", "What goal does an actor accomplish?"],
         ["Class diagram", "What structural elements exist?"],
         ["Sequence diagram", "How do objects communicate over time?"],
         ["Activity diagram", "How does a workflow proceed?"],
         ["State diagram", "How does one object change state?"],
         ["Component diagram", "How is functionality organised into components?"],
         ["Design model", "How should the system be structured for implementation?"],
         ["CASE tool", "What software can help create/manage the models?"]],
        widths=[0.38 * DOC_W, 0.62 * DOC_W]))
    s += [P("At Year 3 level, “a class diagram shows the system and a sequence diagram shows "
            "interaction” is too vague. The expected answer: <i>“A class diagram models the "
            "structural/static aspects of the system by representing classes, attributes, operations and "
            "relationships, whereas a sequence diagram models a particular interaction scenario by "
            "showing the ordered exchange of messages between participating objects.”</i>")]

    # exam --------------------------------------------------------------
    s.append(H1("29.  Examination-Style Questions"))
    s += [P("<b>Question 1 (20 marks).</b> Explain the purpose of CASE tools in object-oriented analysis "
            "and design, discussing at least five ways in which CASE tools support software development."),
          P("<b>Question 2 (25 marks).</b> Using an Online Library Management System, explain how "
            "requirements are transformed into use cases, classes, interactions and a final "
            "object-oriented design."),
          P("<b>Question 3 (25 marks).</b> Explain why UML diagrams should not be developed "
            "independently, demonstrating how use-case, class, sequence, activity and state-machine "
            "diagrams describe different aspects of the same system."),
          P("<b>Question 4 (30 marks).</b> A university wants an online course registration system. "
            "Develop an OOAD solution including (a) actors, (b) use cases, (c) candidate classes, "
            "(d) class relationships, (e) major operations, (f) the registration interaction sequence, "
            "(g) course states, (h) the registration workflow, (i) components, and (j) an explanation of "
            "how the models remain consistent.")]

    # summary --------------------------------------------------------------
    s.append(H1("30.  Week 15 Summary"))
    s.append(CALLOUT("THE MOST IMPORTANT LESSON",
        ["OOAD is not about drawing many UML diagrams. It is about building a coherent model of a "
         "software system where requirements, use cases, objects, classes, interactions, behaviour and "
         "design decisions all support one another. A student who can take a new problem from "
         "<b>Requirement -> Use Case -> Class -> Interaction -> Behaviour -> Design -> Components -> Integrated "
         "UML Documentation</b> has genuinely understood Object-Oriented Analysis and Design — and that "
         "is exactly what Week 15 is designed to test."]))

    # references --------------------------------------------------------------
    s.append(H1("31.  References and Further Reading"))
    s.append(H2("Primary standards"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — formal UML specification (adopted December 2017), organising UML into structural, behavioural and supplementary concepts.",
        "OMG. <i>Introduction to OMG Specifications.</i> Overview of UML diagram categories.",
    ])
    s.append(H2("Process frameworks"))
    s += BUL([
        "IBM. <i>Rational Unified Process (RUP)</i> — four phases (Inception, Elaboration, Construction, Transition) with iterations as planned intervals.",
        "IBM. <i>RUP Best Practices</i> — Inception establishes the business case and scope; Elaboration analyses the domain, establishes the architectural foundation and addresses high-risk areas.",
    ])
    s.append(H2("Prescribed and recommended texts"))
    s += BUL([
        "Mach, E. (2019). <i>Object Oriented Analysis &amp; Design Cookbook: Introduction to Practical System Modeling.</i>",
        "Reddy, V., &amp; Korra, S. (2018). <i>Object-Oriented Analysis and Design Using UML.</i>",
        "The Art of Service. (2021). <i>Object Oriented Analysis and Design: A Complete Guide.</i>",
        "Wixom, B., &amp; Dennis, A. (2018). <i>Systems Analysis and Design.</i>",
        "Blokdyk, G. (2021). <i>Object-Oriented Analysis and Design Standard Requirements.</i>",
        "Wixom, B., &amp; Dennis, A. (2020). <i>Systems Analysis and Design: An Object-Oriented Approach with UML.</i>",
    ])

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
