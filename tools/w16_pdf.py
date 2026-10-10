"""
Week 16 PDF content — COMPREHENSIVE REVISION, INTEGRATED CASE STUDY AND EXAMINATION PREPARATION.
"""
from pdfengine import (H1, H2, P, BUL, FIG, CALLOUT, DTABLE, build, DOC_W,
                      C_MAROON, C_SOFT)

CFG = {
    "week": 16,
    "title": "Comprehensive Revision, Integrated Case Study and Examination Preparation",
    "filename": "Week16_Module_BICT3202_OOAD.pdf",
}


def story():
    s = []

    # 1. introduction --------------------------------------------------------
    s.append(H1("1.  Introduction to Week 16"))
    s += [P("Welcome to the final teaching week of Object-Oriented Analysis and Design. This week is "
            "deliberately different: we are not introducing another isolated topic. Week 16 answers the "
            "most important question: <i>can the student take everything learned throughout the module "
            "and solve a new object-oriented analysis and design problem independently?</i>")]
    s += FIG("w16_progression.png", "Figure 1 — Week 15 -> Week 16")

    # 2. learning outcomes -----------------------------------------------------
    s.append(H1("2.  Week 16 Learning Outcomes"))
    s += [P("By the end of this week, a student should be able to:")]
    s += BUL([
        "Explain the principles of OOAD and the strengths and limitations of object-oriented development.",
        "Distinguish analysis from design; explain the purpose of UML and its diagram families.",
        "Identify actors, use cases, objects and classes from a problem statement.",
        "Construct use-case, class, state, activity, sequence and communication diagrams.",
        "Explain association, aggregation, composition, generalisation, inheritance and polymorphism.",
        "Explain the Unified Software Development Process — phases, iterations, workflows, artefacts.",
        "Combine object, dynamic and behavioural models; evaluate model consistency.",
        "Apply OOAD to an unfamiliar problem and answer examination questions effectively.",
    ])

    # 3. module in one picture -------------------------------------------------------
    s.append(H1("3.  The Entire Module in One Picture"))
    s += [P("Students should be able to reproduce this conceptual journey from memory: understand the "
            "problem -> business needs -> requirements -> use cases -> identify objects/classes -> object "
            "model, dynamic model and behaviour model (classes, states, interactions) -> analysis model "
            "-> object-oriented design -> architecture/components -> implementation. <b>These are connected "
            "stages and views, not unrelated examination topics.</b>")]
    s += FIG("w16_module_picture.png", "Figure 2 — The entire module in one picture")

    # PART A — what is OOAD -------------------------------------------------------
    s.append(H1("PART A — WHAT IS OOAD?"))
    s.append(H1("4.  Object-Oriented Analysis and Design"))
    s += [P("<b>Object-oriented analysis</b> asks: <i>what does the system need to do, and what "
            "objects/classes exist in the problem domain?</i> For a library system the analyst may "
            "identify Student, Book, Librarian, Loan and Library, then investigate what a student does, "
            "what a book is, how a book is borrowed and returned, who may borrow, and the relationships "
            "between students and loans."),
          P("<b>Object-oriented design</b> asks: <i>how should the software be structured so those "
            "requirements can actually be implemented?</i> Where analysis identifies Student, Book and "
            "Loan, design may introduce LoanService, BookRepository, StudentRepository, "
            "NotificationService and LoanController. Therefore: <b>analysis focuses on understanding the "
            "problem; design focuses on constructing a software solution.</b>")]
    s += FIG("w16_analysis_design.png", "Figure 3 — Analysis vs design")
    s.append(DTABLE(
        ["Analysis", "Design"],
        [["Understands the problem", "Defines the solution"],
         ["What does the system need?", "How will the system do it?"],
         ["Identifies domain concepts", "Refines them into software structures"],
         ["Focuses on requirements", "Focuses on implementation structure"],
         ["“What?”", "“How?”"]],
        widths=[0.5 * DOC_W, 0.5 * DOC_W]))

    # PART B — OO principles -------------------------------------------------------
    s.append(H1("PART B — OBJECT-ORIENTED PRINCIPLES REVISION"))
    s.append(H1("5.  Object, Class, Encapsulation and Abstraction"))
    s += [P("An <b>object</b> represents a particular entity with <b>identity, state and behaviour</b> — "
            "Student #ST1001 with name = John, programme = ICT, year = 3 and behaviour registerCourse(), "
            "dropCourse(), viewResults(). A <b>class</b> is the blueprint from which objects are created; "
            "the object is an instance of that blueprint."),
          P("<b>Encapsulation</b> keeps an object's data and the operations that control that data "
            "together while controlling inappropriate direct access — a customer should not set "
            "<font name='Mono'>balance = -500000</font> directly; the BankAccount controls how balance "
            "changes through deposit(), withdraw() and getBalance(). <b>Abstraction</b> focuses on "
            "important characteristics while hiding unnecessary detail — an ATM shows Withdraw, Deposit "
            "and Check Balance without exposing database queries, encryption or server communication.")]
    s += FIG("w16_oo_principles.png", "Figure 4 — Core object-oriented concepts")

    s.append(H1("6.  Inheritance and Polymorphism"))
    s += [P("<b>Inheritance</b> lets a specialised class inherit characteristics from a more general "
            "class — Student and Lecturer inherit name, email and login() from Person. "
            "<b>Polymorphism</b> means the same operation/interface can behave differently depending on "
            "the object involved — PermanentEmployee and ContractEmployee each implement "
            "<font name='Mono'>calculateSalary()</font> differently, so "
            "<font name='Mono'>employee.calculateSalary()</font> behaves differently per object."),
          P("<b>Examination distinction:</b> generalisation is the UML modelling relationship; "
            "inheritance is the object-oriented programming mechanism commonly used to implement it.")]
    s += FIG("w16_inheritance_polymorphism.png", "Figure 5 — Inheritance and polymorphism")

    # PART C — UML revision -------------------------------------------------------
    s.append(H1("PART C — UML REVISION"))
    s.append(H1("7.  What Is UML, and Why Do We Need It?"))
    s += [P("<b>UML</b> is the Unified Modeling Language — a standard modelling language used to "
            "represent and communicate software/system models. The Object Management Group (OMG) lists "
            "UML 2.5.1 as a formal specification (adopted December 2017). Remember: <b>UML is a "
            "modelling language, not a programming language.</b> A complicated banking transaction "
            "described in a paragraph is hard to visualise; a diagram makes relationships and behaviour "
            "much easier to communicate.")]

    s.append(H1("8.  UML Diagram Families"))
    s += [P("<b>Structural diagrams</b> show what the system is made of — class, component, deployment "
            "and package diagrams. <b>Behavioural diagrams</b> show what the system does — use-case, "
            "activity and state-machine diagrams. <b>Interaction diagrams</b> focus on communication "
            "between participants — sequence and communication/collaboration diagrams.")]
    s += FIG("w16_uml_families.png", "Figure 6 — UML diagram families")

    # PART D — use-case revision -------------------------------------------------------
    s.append(H1("PART D — USE-CASE REVISION"))
    s.append(H1("9.  Actor, Use Case, Include and Extend"))
    s += [P("A <b>use case</b> represents a goal an actor wants to accomplish with the system. The "
            "<b>actor</b> is the external role (Student); the <b>use case</b> is the goal (Register "
            "Course). <font name='Mono'>&lt;&lt;include&gt;&gt;</font> is used when one use case always "
            "incorporates required behaviour (Register Course includes Check Eligibility); "
            "<font name='Mono'>&lt;&lt;extend&gt;&gt;</font> is used for optional, conditional behaviour "
            "(Make Payment extended by Apply Discount). <b>Do not use include and extend randomly.</b>")]
    s += FIG("w16_use_case_relations.png", "Figure 7 — Actors, use cases, include and extend")

    # PART E — class diagram revision -------------------------------------------------------
    s.append(H1("PART E — CLASS DIAGRAM REVISION"))
    s.append(H1("10.  Class, Attribute, Operation and Visibility"))
    s += [P("The <b>class diagram</b> describes the static structure. An <b>attribute</b> is data "
            "belonging to a class (studentId, name, email); an <b>operation</b> is behaviour or "
            "responsibility (registerCourse(), dropCourse()). Common <b>visibility</b> symbols: "
            "<font name='Mono'>+</font> public, <font name='Mono'>-</font> private, "
            "<font name='Mono'>#</font> protected, <font name='Mono'>~</font> package — e.g. "
            "<font name='Mono'>- studentId : String</font> and <font name='Mono'>+ getName() : String"
            "</font>.")]
    s += FIG("w16_class_notation.png", "Figure 8 — Class diagram notation")

    # PART F — relationships -------------------------------------------------------
    s.append(H1("PART F — RELATIONSHIPS REVISION"))
    s.append(H1("11.  Association, Multiplicity, Aggregation, Composition, Generalisation"))
    s += [P("<b>Association</b> is a general relationship between classes (Student — Course). "
            "<b>Multiplicity</b> says how many objects participate: <font name='Mono'>1</font> exactly "
            "one, <font name='Mono'>0..1</font> zero or one, <font name='Mono'>*</font> many, "
            "<font name='Mono'>0..*</font> zero or many, <font name='Mono'>1..*</font> one or many — "
            "e.g. <font name='Mono'>Student 1 ─ 0..* Registration</font>."),
          P("<b>Aggregation</b> is a weaker whole-part relationship where parts can exist independently "
            "(Department o— Lecturer); <b>composition</b> is stronger ownership/lifecycle (House *— "
            "Room). <b>Generalisation</b> is an “is-a” relationship (Car and Motorcycle are Vehicles). "
            "Choose the diamond from the ownership/lifecycle relationship, not because “the diamond "
            "looks nice.”")]
    s += FIG("w16_relationships.png", "Figure 9 — Class relationships")
    s += FIG("w16_multiplicity.png", "Figure 10 — Multiplicity")

    # PART G — dynamic modelling -------------------------------------------------------
    s.append(H1("PART G — DYNAMIC MODELLING REVISION"))
    s.append(H1("12.  Event, State, Transition and the State Diagram"))
    s += [P("Dynamic modelling describes how the system changes over time — <i>“what happens?”</i> "
            "rather than <i>“what exists?”</i>. An <b>event</b> causes a change (Course Registration "
            "Opens); a <b>state</b> is a condition at a point (Open, Closed, Full); a <b>transition</b> "
            "is movement between states (Available -> Full when the final seat is taken). The Course "
            "lifecycle: Created -> Available -> Full -> Closed.")]
    s += FIG("w16_state_diagram.png", "Figure 11 — State diagram: Course lifecycle")

    # PART H — behavioural modelling -------------------------------------------------------
    s.append(H1("PART H — BEHAVIOURAL MODELLING REVISION"))
    s.append(H1("13.  Activity, Sequence and Communication Diagrams"))
    s += [P("An <b>activity diagram</b> models a workflow (Start -> Login -> Select Course -> Check "
            "Eligibility -> Check Capacity -> Register -> End). A <b>sequence diagram</b> focuses on "
            "<i>who communicates with whom and in what order</i> (Student -> RegistrationController -> "
            "RegistrationService -> StudentRecord -> Registration). A <b>communication/collaboration "
            "diagram</b> also models interactions but emphasises objects, relationships and message "
            "numbering (1: register(), 2: validate(), 3: save()).")]
    s += FIG("w16_sequence_vs_activity.png", "Figure 12 — Sequence diagram vs activity diagram")
    s.append(DTABLE(
        ["Sequence Diagram", "Activity Diagram"],
        [["Focuses on interactions", "Focuses on workflow"],
         ["Shows participants/lifelines", "Shows activities/actions"],
         ["Shows message ordering", "Shows process flow"]],
        widths=[0.5 * DOC_W, 0.5 * DOC_W]))

    # PART I — full model integration -------------------------------------------------------
    s.append(H1("PART I — FULL MODEL INTEGRATION"))
    s.append(H1("14.  The Most Important Week 16 Concept"))
    s += [P("Follow one requirement through the chain: <b>Requirement</b> (“students must be able to "
            "register for courses”) -> <b>Use Case</b> (Register Course) -> <b>Classes</b> (Student, "
            "Course, Registration, RegistrationService) -> <b>Sequence</b> (Student -> "
            "RegistrationService -> Course -> Registration) -> <b>State</b> (Course: Available -> Full) -> "
            "<b>Activity</b> (Select Course -> Check Eligibility -> Check Capacity -> Register) -> "
            "<b>Design</b> (Presentation -> Application -> Domain -> Persistence). That is integrated "
            "OOAD.")]
    s += FIG("w16_integration_chain.png", "Figure 13 — Full model integration")

    # PART J — consistency -------------------------------------------------------
    s.append(H1("PART J — UML MODEL CONSISTENCY"))
    s.append(H1("15.  What Does Consistency Mean?"))
    s += [P("If the class diagram says <font name='Mono'>Course.checkCapacity()</font> but the sequence "
            "diagram says <font name='Mono'>Course.checkAvailableSeats()</font>, ask: <i>are these the "
            "same operation?</i> If not, the model may be inconsistent. Perform the six checks: "
            "(1) use cases <- requirements; (2) use cases <- classes; (3) sequence <- class; "
            "(4) activity <- sequence; (5) state <- behaviour; (6) design <- requirements.")]
    s += FIG("w16_consistency.png", "Figure 14 — Six model-consistency checks")

    # PART K — USDP -------------------------------------------------------
    s.append(H1("PART K — UNIFIED SOFTWARE DEVELOPMENT PROCESS REVISION"))
    s.append(H1("16.  USDP/UP and Its Four Phases"))
    s += [P("The Unified Software Development Process (USDP), associated with the Unified Process, is "
            "an <b>iterative and incremental</b> approach: development is divided into phases and "
            "iterations rather than one uninterrupted sequence. IBM's Rational Unified Process "
            "documentation describes four phases:"),
          P("<b>Inception</b> — “should we build this system?” (business problem, scope, stakeholders, "
            "feasibility, business case). <b>Elaboration</b> — “do we understand the problem and "
            "architecture?” (requirements, architecture, risk, key use cases, initial design). "
            "<b>Construction</b> — “can we build it?” (implementation, integration, testing, "
            "refinement). <b>Transition</b> — “can users use it?” (deployment, acceptance, training, "
            "fixes, operational use).")]
    s += FIG("w16_usdp.png", "Figure 15 — The four phases of the Unified Process")

    # PART L — iterative development -------------------------------------------------------
    s.append(H1("PART L — ITERATIVE DEVELOPMENT"))
    s.append(H1("17.  What Is an Iteration?"))
    s += [P("An <b>iteration</b> is a development cycle during which a team produces and evaluates part "
            "of the system. Instead of “plan everything -> build everything -> test everything”, an "
            "iterative approach cycles through: Iteration 1 (requirements + basic design) -> feedback -> "
            "Iteration 2 (more functionality) -> feedback -> Iteration 3 (more functionality) -> feedback "
            "-> Iteration 4 (refinement + testing). Iterations are planned, measured intervals within "
            "phases that deliver incremental value to stakeholders.")]
    s += FIG("w16_iterative.png", "Figure 16 — Iterative development")

    # PART M — reuse -------------------------------------------------------
    s.append(H1("PART M — REUSE REVISION"))
    s.append(H1("18.  What Is Software Reuse?"))
    s += [P("<b>Software reuse</b> means using an existing component, class, library, framework, "
            "service, design or architecture rather than developing everything from scratch — an "
            "authentication library instead of a bespoke mechanism, or a UI framework instead of "
            "building every control. The goal: reuse -> less duplication -> less effort -> potentially "
            "improved consistency -> easier maintenance. However, reuse should be based on suitability, "
            "security, maintainability, compatibility and licensing — not simply because something "
            "already exists.")]

    # PART N — case study -------------------------------------------------------
    s.append(H1("PART N — CASE STUDY FOR FINAL REVISION"))
    s.append(H1("19.  Scenario: Mobile Money System"))
    s += [P("A telecommunications company wants a mobile money system. <b>Users</b> create accounts, "
            "deposit, withdraw, send, receive, check balance and view history. <b>Agents</b> deposit "
            "and withdraw for customers and view their transactions. <b>Administrators</b> manage users "
            "and agents, monitor transactions and generate reports."),
          P("<b>Actors:</b> Customer, Agent, Administrator, Banking System, Notification Service. "
            "<b>Candidate classes:</b> User, Customer, Agent, Administrator, Wallet, Transaction, "
            "Deposit, Withdrawal, Transfer, Notification — plus services AuthenticationService, "
            "TransactionService, NotificationService. <b>Relationships:</b> User generalises Customer / "
            "Agent / Administrator; <font name='Mono'>Customer 1 ─ 1 Wallet</font>; "
            "<font name='Mono'>Wallet 1 ─ 0..* Transaction</font>. <b>Send Money:</b> sendMoney() -> "
            "validateSender() -> checkBalance() -> creditReceiver() -> createTransaction() -> "
            "sendNotification(). <b>Transaction states:</b> Created -> Pending -> Completed (or Failed).")]
    s += FIG("w16_mobile_money.png", "Figure 17 — Mobile money case study")

    # PART O — practical -------------------------------------------------------
    s.append(H1("PART O — PRACTICAL REVISION"))
    s.append(H1("20.  Practical Exercise and Challenge"))
    s += [P("Use a UML/CASE tool to model the mobile money system with six diagrams: use-case, class, "
            "sequence (Send Money), activity (Send Money), state-machine (Transaction) and component. "
            "Then deliberately introduce the error: the sequence diagram calls "
            "<font name='Mono'>validateTransaction()</font> but the class diagram contains "
            "<font name='Mono'>checkTransaction()</font> — and correct it. <b>UML modelling is complete "
            "when the model is logically consistent, not when the diagram looks beautiful.</b>")]

    # PART P — exam revision -------------------------------------------------------
    s.append(H1("PART P — EXAMINATION REVISION"))
    s.append(H1("21.  Common Theory and Practical Questions"))
    s += [P("<b>Theory:</b> define OOAD; explain five characteristics of OO systems; distinguish an "
            "object from a class; explain encapsulation, abstraction, inheritance and polymorphism; "
            "what is UML; structural vs behavioural modelling; association vs aggregation vs "
            "composition; generalisation vs inheritance; purpose of a use-case diagram; sequence vs "
            "activity diagrams."),
          P("<b>Practical:</b> given a scenario — identify actors and use cases, draw the use-case "
            "diagram, identify classes, draw the class diagram with multiplicities and inheritance, "
            "create sequence, activity, state and component diagrams, and explain how the diagrams "
            "relate.")]

    # PART Q — exam approach -------------------------------------------------------
    s.append(H1("PART Q — HOW TO APPROACH AN EXAM SCENARIO"))
    s.append(H1("22.  Never Start Drawing Immediately"))
    s += [P("Follow a disciplined process: (1) read the problem twice; (2) underline the nouns; "
            "(3) identify possible objects/classes; (4) identify actors; (5) identify actions/goals; "
            "(6) convert goals into use cases; (7) build the use-case diagram; (8) develop the class "
            "model; (9) choose an important scenario; (10) develop the sequence diagram; (11) develop "
            "activity/state models; (12) check consistency."),
          P("<b>The noun technique:</b> in “a patient books an appointment with a doctor; the "
            "receptionist manages patient records and doctors access their schedules”, candidate nouns "
            "are Patient, Appointment, Doctor, Receptionist, Patient Record and Schedule; candidate "
            "verbs are book, manage and access. This is a useful candidate-identification technique — "
            "not a mechanical rule that every noun must become a class.")]
    s += FIG("w16_exam_approach.png", "Figure 18 — How to approach an exam scenario")

    # PART R — common mistakes -------------------------------------------------------
    s.append(H1("PART R — COMMON STUDENT MISTAKES"))
    s += BUL([
        "<b>Confusing class and object</b> — Student can be a class; student123 is an object/instance.",
        "<b>Every noun becomes a class</b> — “quickly” is not a class; use judgement.",
        "<b>Every verb becomes a method</b> — ask which object has the responsibility.",
        "<b>Confusing include and extend</b> — include = required; extend = optional.",
        "<b>Confusing aggregation and composition</b> — decide from ownership/lifecycle.",
        "<b>Sequence diagrams without class diagrams</b> — messages need a home in the class model.",
        "<b>Beautiful UML, wrong logic</b> — examiners mark correct modelling, not decoration.",
    ])

    # PART S — master revision table -------------------------------------------------------
    s.append(H1("PART S — MASTER REVISION TABLE"))
    s.append(H1("23.  All Major Concepts"))
    s.append(DTABLE(
        ["Topic", "Main Question"],
        [["Business needs", "Why does the organisation need the system?"],
         ["Requirements", "What does the system need to provide?"],
         ["Object / Class", "What entity exists? / What defines similar objects?"],
         ["Encapsulation / Abstraction", "How are data and behaviour controlled? / What details are hidden?"],
         ["Inheritance / Polymorphism", "What can a subclass inherit? / How can one operation behave differently?"],
         ["UML", "How do we communicate the model visually?"],
         ["Use case / Class diagram", "What goal does an actor accomplish? / What structure exists?"],
         ["Association / Aggregation / Composition", "How are classes related? / What whole-part relationship exists?"],
         ["Generalisation", "What is the superclass/subclass relationship?"],
         ["Dynamic model / State / Event", "How does the system change over time?"],
         ["Activity / Sequence / Communication", "What is the workflow? Who communicates, and when?"],
         ["USDP / Reuse / Design / Component", "How is development organised? What can be reused? How is the solution structured?"],
         ["CASE tool / Integration", "How is modelling supported by software? Do all models tell the same story?"]],
        widths=[0.4 * DOC_W, 0.6 * DOC_W]))

    # PART T — 16-week journey -------------------------------------------------------
    s.append(H1("PART T — THE 16-WEEK JOURNEY"))
    s.append(H1("24.  What Students Have Covered"))
    s += BUL([
        "<b>Week 1:</b> business needs, software needs and object technology for business.",
        "<b>Week 2:</b> principles of object modelling.",
        "<b>Weeks 3–4:</b> UML overview, building blocks, rules, mechanisms and architecture.",
        "<b>Weeks 5–6:</b> object modelling I &amp; II — classes, associations, aggregation, inheritance, polymorphism and grouping.",
        "<b>Week 7:</b> dynamic modelling — events, states, operations and concurrency.",
        "<b>Week 8:</b> behavioural modelling — use cases, interactions, sequences, communication and activities.",
        "<b>Week 9:</b> USDP/UP — phases, iterations, workflows, artefacts, risk and reuse.",
        "<b>Weeks 10–12:</b> object-oriented design, refinement and integrated modelling.",
        "<b>Weeks 13–14:</b> multilayer architecture, reusable components and integrated design.",
        "<b>Week 15:</b> complete OOAD case study and CASE-tool implementation.",
        "<b>Week 16:</b> comprehensive revision, integrated application and examination preparation.",
    ])

    # tutorial / practical -------------------------------------------------------
    s.append(H1("25.  Tutorial, Practical and Examination Practice"))
    s += [P("<b>Tutorial:</b> an Online Examination Management System — identify actors; at least 10 use "
            "cases; at least 10 candidate classes; the use-case diagram; the class diagram; a sequence "
            "diagram for Start Examination; an activity diagram for Taking an Examination; a state "
            "diagram for Examination (Created -> Scheduled -> Open -> In Progress -> Submitted -> Marked -> "
            "Released); identify components; explain how the diagrams relate."),
          P("<b>Practical mini-project:</b> choose a Hospital, Banking, Mobile Money, University "
            "Registration, Library, Hotel, E-commerce or Transport system, and submit: problem "
            "statement, objectives, functional and non-functional requirements, actors, use cases, "
            "use-case, class, sequence, activity, state and component diagrams, architecture, model "
            "consistency analysis and conclusion."),
          P("<b>Revision question bank:</b> use the short-answer, comparison, long-answer and case-study "
            "prompts in this module for untimed practice; they are not a complete timed paper. Two "
            "parallel full-length practice papers are provided as "
            "<font name='Mono'>exams/End-Semester-Exam-Paper-A.md</font> and "
            "<font name='Mono'>exams/End-Semester-Exam-Paper-B.md</font>, with a separate confidential "
            "marking guide. Each draft paper is 100 marks with Q1 compulsory (40) plus any three of four "
            "20-mark questions. The course outline assigns 60% to the examination but does not specify a "
            "duration; the three-hour duration in the drafts must be confirmed by the Faculty before "
            "formal issue.")]

    # PART X — exam strategy -------------------------------------------------------
    s.append(H1("26.  Exam Answering Strategy"))
    s += [P("For <b>definition</b> questions, write the full definition and give an example. For "
            "<b>explain</b> questions, use Definition -> Explanation -> Example -> Importance. For "
            "<b>compare</b> questions, use a table. For <b>UML</b> questions, identify the requirement, "
            "actors, use cases, classes, relationships and behaviour — then check consistency. State "
            "assumptions, and let the marks guide the amount of detail. <b>Do not randomly draw diagrams.</b>"),
          P("For the proposed 3-hour practice papers, a possible plan is about 65 minutes for the "
            "40-mark integrated case, about 32 minutes for each of the three chosen Section B questions, "
            "and the remaining time for reading and checking. Adjust this plan if the approved exam "
            "duration differs.")]

    # final takeaway -------------------------------------------------------
    s.append(H1("27.  Final Week 16 Takeaway"))
    s.append(CALLOUT("THE ENTIRE MODULE IN ONE QUESTION",
        ["How can we systematically understand a software problem and represent a solution using "
         "objects, classes, UML models and an appropriate development process? The answer: "
         "<b>Business Problem -> Requirements -> Actors -> Use Cases -> Objects/Classes -> Class Model -> "
         "Dynamic/State Model -> Behavioural/Interaction -> Analysis -> Design -> Architecture/Components -> "
         "Model Integration -> Implementation.</b> OOAD is not simply about drawing UML diagrams — it is "
         "about thinking systematically, identifying what matters, understanding interactions and "
         "behaviour, and transforming that understanding into a coherent design developers can "
         "implement."]))

    # revision checklist -------------------------------------------------------
    s.append(H1("28.  Final Revision Checklist"))
    s += BUL([
        "<b>Object orientation:</b> can I define object, class, encapsulation, abstraction, inheritance, polymorphism?",
        "<b>UML:</b> can I explain UML and distinguish structural, behavioural and interaction diagrams?",
        "<b>Use cases:</b> can I identify actors and use cases, and use include/extend correctly?",
        "<b>Class modelling:</b> can I identify classes, attributes, operations, associations, multiplicities, aggregation, composition and generalisation?",
        "<b>Dynamic &amp; behavioural:</b> can I model events, states, transitions, activity, sequence and communication diagrams?",
        "<b>USDP:</b> can I explain Inception, Elaboration, Construction, Transition, iterations, workflows and artefacts?",
        "<b>Design:</b> can I distinguish analysis from design, combine the models, identify components, explain layered architecture and reuse?",
        "<b>Practical:</b> can I use a CASE tool, model a new system and check consistency?",
        "<b>Examination:</b> can I explain in my own words, give examples, draw diagrams and justify decisions?",
    ])

    # references -------------------------------------------------------
    s.append(H1("29.  References and Further Reading"))
    s.append(H2("Primary standards and process frameworks"))
    s += BUL([
        "Object Management Group (OMG). <i>Unified Modeling Language (UML), Version 2.5.1.</i> OMG — formal UML specification and normative documents.",
        "IBM. <i>Rational Unified Process (RUP)</i> — four phases (Inception, Elaboration, Construction, Transition) with iterations as planned intervals.",
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

    # conclusion -------------------------------------------------------
    s.append(H1("30.  Conclusion of the 16-Week Module"))
    s += [P("Week 1 establishes business/software needs and object technology; Week 2 develops object "
            "modelling principles; Weeks 3–4 cover UML; Weeks 5–6 develop object modelling; Week 7 "
            "covers dynamic modelling; Week 8 covers behavioural modelling; Week 9 introduces USDP/UP; "
            "Weeks 10–12 develop object-oriented design, refinement and model integration; Weeks 13–14 "
            "focus on multilayer architecture, reusable components and design integration; Week 15 "
            "applies the process in a complete case study. In Week 16, <b>the student becomes the "
            "analyst/designer</b> — able to move from Requirements -> Actors -> Use Cases -> Classes -> "
            "Relationships -> Interactions -> Behaviour -> Architecture -> Components -> an Integrated "
            "UML Model. That is the culmination of BICT 3202 Object-Oriented Analysis and Design.")]

    return s


if __name__ == "__main__":
    print("Built:", build(CFG, story))
