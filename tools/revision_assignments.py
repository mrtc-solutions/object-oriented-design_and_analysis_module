"""Single source of truth for Week 15/16 PDF and Word assignments."""

ASSIGNMENTS = {
    15: {
        "title": "Complete OOAD Case Study, Model Integration and CASE Tool Implementation",
        "instructions": [
            "Answer ALL questions in Sections A, B and C.",
            "Read the Week 15 module and your lecture notes before attempting each question.",
            "Use the university course registration case study where stated.",
            "Show that your models are consistent: sequence messages must match class operations.",
            "Draw UML diagrams in correct notation, or with a CASE/UML tool.",
            "Submit by the date given by your lecturer. Total: 50 marks.",
        ],
        "short": [
            ("Define a CASE tool and state three ways it supports software development.", 3),
            ("Differentiate functional from non-functional requirements, with one example each.", 3),
            ("Define an actor and explain why an actor need not be a human being.", 2),
            ("Differentiate a domain class from a technical/application class.", 3),
            ("State the multiplicity meaning of Student 1 — 0..* Registration.", 2),
            ("Why should UML diagrams not be developed independently?", 3),
            ("Explain model traceability using the Register Course requirement.", 2),
            ("List the six consistency checks of a model audit.", 2),
        ],
        "application": [
            ("For university online course registration, a student selects an open course. The system checks prerequisites and active duplicates, atomically reserves capacity and persists the registration in one transaction, then sends confirmation only after commit. On failure the transaction leaves no registration or seat claim.", [
                ("Identify the actors and functional requirements.", 2),
                ("Identify candidate domain classes and technical classes.", 2),
                ("Draw the sequence diagram for Register Course, including a rejection path.", 3),
                ("Draw the state machine for Course (Created, Available, Full, Closed).", 2),
                ("Explain how the sequence messages map to class operations.", 3),
            ]),
            ("The activity diagram contains Check Payment, but no payment rule is stated and the class model has no payment-related operation, class or component.", [
                ("Identify the modelling problem.", 2),
                ("Explain how to reconcile the models with the approved requirements.", 3),
                ("Describe how a CASE tool helps manage this change.", 3),
            ]),
        ],
        "case": ("A college wants an Online Library Management System. Students search, borrow, return and view borrowed books. Librarians add or withdraw physical copies, register members and view overdue loans. A Copy is Available until issued, OnLoan while borrowed, and becomes Available on undamaged return; a damaged return enters Maintenance, then becomes Available when repaired. A copy may be Withdrawn only when not on loan. Each Loan links one member and one copy; a copy can have loan history but at most one active loan.", [
            ("Identify actors, use cases and candidate classes.", 3),
            ("Draw a sequence diagram for Borrow Book.", 3),
            ("Draw a state machine for Copy using the stated lifecycle.", 2),
            ("Explain how use-case, class, sequence, activity and state-machine diagrams relate to each other.", 2),
        ]),
        "case_label": "Library management system",
    },
    16: {
        "title": "Comprehensive Revision, Integrated Case Study and Examination Preparation",
        "instructions": [
            "Answer ALL questions in Sections A, B and C.",
            "Read the Week 16 module and your lecture notes before attempting each question.",
            "This 50-mark assignment is revision, not a full end-of-semester examination.",
            "Draw UML diagrams in correct notation and check that your models are consistent.",
            "Submit by the date given by your lecturer. Total: 50 marks.",
        ],
        "short": [
            ("Define object-oriented analysis and object-oriented design.", 3),
            ("Distinguish an object from a class.", 2),
            ("Define encapsulation and abstraction, with one example each.", 3),
            ("Define inheritance and polymorphism.", 2),
            ("What is UML? State whether it is a modelling or a programming language.", 2),
            ("Define an actor and a use case.", 2),
            ("State the meaning of the multiplicity 1 — 0..*.", 2),
            ("Differentiate aggregation from composition.", 2),
            ("Name the four phases of the Unified Process.", 2),
        ],
        "application": [
            ("For a mobile money system, users deposit, withdraw, send, receive and check balances; agents serve customers; administrators manage users and monitor transactions. MoneyTransfer is created Pending, completes when the debit and credit commit together, or becomes Failed if validation or persistence fails, leaving balances unchanged. Assume authentication and state any other policy assumptions.", [
                ("Identify the actors.", 2),
                ("Identify candidate classes. Propose a justified generalisation, or explain why inheritance should not be forced.", 3),
                ("Draw a sequence diagram for Send Money including failure handling.", 4),
                ("Draw a state-machine diagram for MoneyTransfer using the stated lifecycle.", 3),
            ]),
            ("The sequence diagram calls validateTransaction(), but the corresponding class contains only checkTransaction().", [
                ("Identify the modelling problem.", 2),
                ("Explain why consistency matters between diagrams.", 3),
                ("Describe how the team should resolve the discrepancy.", 3),
            ]),
        ],
        "case": ("A university wants online student registration. Students log in, view courses, check prerequisites, register, drop courses and view registrations. Administrators create or modify courses, close registration and view reports. Course starts Created, becomes Available when opened with capacity, becomes Full when its last seat is reserved, returns to Available when a seat is released while registration remains open, and becomes Closed when registration is closed. No new registration is allowed in Closed. Each Registration links one Student and one Course, and only one active registration per student/course pair is permitted.", [
            ("Identify the actors and use cases.", 3),
            ("Draw a class diagram with relationships and multiplicities.", 4),
            ("Draw a state-machine diagram for Course with event labels and guards.", 3),
        ]),
        "case_label": "Online student registration",
    },
}


def blocks(week):
    """Yield simple semantic blocks shared by both renderers."""
    data = ASSIGNMENTS[week]
    yield "h1", "Assignment Instructions"
    for item in data["instructions"]:
        yield "bullet", item
    yield "h1", "Section A — Short-Answer Questions (20 marks)"
    for n, (question, marks) in enumerate(data["short"], 1):
        yield "h2", f"Question A{n}"
        yield "p", f"{question} [{marks} marks]"
    yield "h1", "Section B — Application Questions (20 marks)"
    for n, (scenario, questions) in enumerate(data["application"], 1):
        yield "h2", f"Question B{n} ({sum(m for _, m in questions)} marks)"
        yield "p", scenario
        for i, (question, marks) in enumerate(questions):
            yield "bullet", f"({chr(97+i)}) {question} [{marks} marks]"
    yield "h1", "Section C — Case Study (10 marks)"
    yield "p", data["case"][0]
    for i, (question, marks) in enumerate(data["case"][1]):
        yield "bullet", f"({chr(97+i)}) {question} [{marks} marks]"
    yield "h1", "Marking Scheme"
    yield "table", [
        ["Section", "Content", "Marks"],
        ["A", f"Short-answer questions ({len(data['short'])} questions)", "20"],
        ["B", "Application questions (12 + 8)", "20"],
        ["C", data["case_label"], "10"],
        ["", "TOTAL", "50"],
    ]
    yield "h1", "Submission & Academic Integrity"
    for item in [
        "Submit a typed document (or neatly handwritten, as directed by your lecturer).",
        "This is individual work. Plagiarism or copying attracts a penalty under university regulations.",
        "Use correct UML notation, including multiplicities, messages, events and guards.",
        f"Cite sources using the format in the Week {week} module references.",
    ]:
        yield "bullet", item


def pdf_story(week):
    import html
    from pdfengine import H1, H2, P, BUL, DTABLE, DOC_W
    story = []
    for kind, value in blocks(week):
        if kind == "table":
            story.append(DTABLE(value[0], value[1:], widths=[.15*DOC_W, .7*DOC_W, .15*DOC_W]))
        elif kind == "bullet":
            story.extend(BUL([html.escape(value)]))
        else:
            story.append({"h1": H1, "h2": H2, "p": P}[kind](html.escape(value)))
    return story


def docx_content(week, doc, helpers):
    from docxengine import heading, para, bullet
    from build_exam_docs import docx_table
    for kind, value in blocks(week):
        if kind in ("h1", "h2"):
            heading(doc, value, level=1 if kind == "h1" else 2)
        elif kind == "table":
            docx_table(doc, value)
        elif kind == "bullet":
            bullet(doc, value)
        else:
            para(doc, value)
