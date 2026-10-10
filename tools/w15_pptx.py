"""
Week 15 PPTX content — COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION.
"""
from pptxengine import build

CFG = {
    "week": 15,
    "title": "Complete OOAD Case Study, Model Integration and CASE Tool Implementation",
    "filename": "Week15_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Analyse ", "a complete software problem using OO techniques."),
        ("Extract ", "actors, functional and non-functional requirements."),
        ("Build ", "use-case, class, interaction, activity, state and component models."),
        ("Refine ", "the analysis model into a design model with responsibilities."),
        ("Check ", "consistency between the UML models."),
        ("Document ", "a complete OOAD solution and use a CASE/UML tool."),
        ("Explain ", "how the final design could be implemented."),
    ], size=16, gap=11)
    d.takeaway(s, "The diagrams must tell one consistent story and guide implementation.")

    # 3. progression
    s = d.slide()
    d.header(s, "Week 14 -> Week 15", "From understanding to a complete application")
    d.pic(s, "w15_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Week 15 applies Weeks 1–14 to one complete system.")

    # 4. journey
    s = d.slide()
    d.header(s, "The OOAD Journey", "The whole module in one flow")
    d.pic(s, "w15_process.png", y=1.5, w=10.2)
    d.takeaway(s, "The most important word: INTEGRATION.")

    # 5. consistency
    s = d.slide()
    d.header(s, "Why Integration Matters", "Three ways a model can go wrong")
    d.pic(s, "w15_consistency.png", y=1.6, w=10.6)
    d.takeaway(s, "A good OOAD model must be internally consistent.")

    # 6. business problem
    s = d.slide()
    d.header(s, "The Business Problem", "University course registration — the pain")
    d.pic(s, "w15_business_problem.png", y=1.6, w=10.6)
    d.takeaway(s, "Students register online; administrators manage courses and reports.")

    # 7. requirements
    s = d.slide()
    d.header(s, "Requirements", "Functional vs non-functional")
    d.pic(s, "w15_requirements.png", y=1.6, w=10.6)
    d.takeaway(s, "FR = what it does · NFR = how well it operates.")

    # 8. actors
    s = d.slide()
    d.header(s, "Actors", "External roles — human or system")
    d.pic(s, "w15_actors.png", y=1.6, w=10.6)
    d.takeaway(s, "Student · Administrator · Lecturer · Notification Service · Payment Gateway.")

    # 9. use-case diagram
    s = d.slide()
    d.header(s, "Use-Case Diagram", "Student and Administrator goals")
    d.pic(s, "w15_use_case_diagram.png", y=1.6, w=10.6)
    d.takeaway(s, "Produce the exact notation with a UML tool in the practical.")

    # 10. use-case specification
    s = d.slide()
    d.header(s, "Use Case: Register for Course", "Do not stop at the diagram")
    d.pic(s, "w15_use_case_spec.png", y=1.5, w=10.4)
    d.takeaway(s, "Document the main scenario AND the alternative flows.")

    # 11. candidate classes
    s = d.slide()
    d.header(s, "Candidate Classes", "Domain vs technical")
    d.pic(s, "w15_candidate_classes.png", y=1.6, w=10.6)
    d.takeaway(s, "Domain = the problem · Technical = the implementation support.")

    # 12. class model
    s = d.slide()
    d.header(s, "The Class Model", "Controller -> Service -> Domain -> Repository")
    d.pic(s, "w15_class_model.png", y=1.5, w=10.3)
    d.takeaway(s, "From “register a course” to an implementation-ready design.")

    # 13. associations
    s = d.slide()
    d.header(s, "Associations & Multiplicity", "Reading the numbers")
    d.pic(s, "w15_associations.png", y=1.6, w=10.6)
    d.takeaway(s, "Student 1 — 0..* Registration — 0..* 1 Course.")

    # 14. inheritance
    s = d.slide()
    d.header(s, "Inheritance", "A shared User abstraction")
    d.pic(s, "w15_inheritance.png", y=1.6, w=10.6)
    d.takeaway(s, "Use inheritance only when it is genuinely appropriate.")

    # 15. sequence
    s = d.slide()
    d.header(s, "Sequence Diagram", "Which object talks to which, in what order")
    d.pic(s, "w15_sequence.png", y=1.5, w=10.4)
    d.takeaway(s, "reserveSeat() + save in one transaction; send confirmation only after commit.")

    # 16. state machine
    s = d.slide()
    d.header(s, "State Machine: Course Lifecycle", "States and their triggering events")
    d.pic(s, "w15_state_machine.png", y=1.5, w=10.4)
    d.takeaway(s, "Guard: enrolledCount <= capacity · seat reservation drives Available <-> Full.")

    # 17. activity
    s = d.slide()
    d.header(s, "Activity Diagram", "The registration workflow")
    d.pic(s, "w15_activity.png", y=1.5, w=10.4)
    d.takeaway(s, "Check prerequisite + duplicate; reserve seat atomically; reject without saving on failure.")

    # 18. components
    s = d.slide()
    d.header(s, "Components & Layers", "Presentation -> Application -> Domain -> Persistence")
    d.pic(s, "w15_components.png", y=1.5, w=10.4)
    d.takeaway(s, "Connects directly with the architecture covered earlier.")

    # 19. traceability
    s = d.slide()
    d.header(s, "Model Traceability", "Following one requirement through the design")
    d.pic(s, "w15_traceability.png", y=1.5, w=10.4)
    d.takeaway(s, "FR5 -> registerStudent() · FR6 -> existsActiveFor() + unique constraint · FR7 -> reserveSeat().")

    # 20. consistency audit
    s = d.slide()
    d.header(s, "The Model Audit", "Six consistency checks")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Use Case <- Class: ", "does every use case have supporting classes?"),
        ("Class <- Sequence: ", "does every message match an operation?"),
        ("Sequence <- State: ", "do messages cause the right transitions?"),
        ("Activity <- Sequence: ", "does the workflow match the interaction?"),
        ("Class <- Component: ", "are classes sensibly allocated?"),
        ("Requirements <- Design: ", "can each requirement be traced in?"),
    ], size=16, gap=13)
    d.takeaway(s, "“Check payment” with no payment class = something is missing.")

    # 21. documentation
    s = d.slide()
    d.header(s, "Complete OOAD Documentation", "What the document contains")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. Introduction ", "· 2. Requirements · 3. Actors · 4. Use cases · 5. Use-case diagram."),
        ("6. Domain/class model ", "· 7. Interaction models · 8. Dynamic model · 9. Activity model."),
        ("10. Design ", "· 11. Architecture · 12. Model validation · 13. Conclusion."),
    ], size=15, gap=12)
    d.takeaway(s, "A professional analysis/design document is complete and consistent.")

    # 22. CASE tools
    s = d.slide()
    d.header(s, "CASE Tools", "Computer-Aided Software Engineering")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Why: ", "diagram editing, model repositories, documentation, consistency, code engineering."),
        ("Examples: ", "Enterprise Architect · Visual Paradigm · StarUML · Modelio · diagrams.net."),
        ("Course outline: ", "CASE Tool — Select Enterprise Demonstration."),
    ], size=16, gap=14)
    d.takeaway(s, "The tool matters less than understanding the modelling principles.")

    # 23. tool mindset
    s = d.slide()
    d.header(s, "The Tool Does Not Do the Thinking", "Four classic mistakes")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Diagrams without requirements ", "— follow the correct order."),
        ("Too many classes ", "— Manager/Processor/Handler/Helper without justification."),
        ("Copying diagrams ", "— the model must represent YOUR system."),
        ("Inconsistent naming ", "— Registration vs Enrollment vs CourseSignup."),
    ], size=15, gap=12)
    d.takeaway(s, "Understand Problem -> Model -> Design, then use the tool.")

    # 24. integrated model
    s = d.slide()
    d.header(s, "The Complete OOAD Journey", "The big picture")
    d.pic(s, "w15_integrated.png", y=1.6, w=10.6)
    d.takeaway(s, "Actors -> Use cases -> Analysis -> Class/Dynamic/Behaviour -> Design -> Implementation.")

    # 25. summary
    s = d.slide()
    d.header(s, "Week 15 Summary", "The most important lesson")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "OOAD is not about drawing many diagrams — it is about a coherent model."),
        ("2. ", "Requirements, use cases, classes, interactions, behaviour and design support one another."),
        ("3. ", "Requirement -> Use Case -> Class -> Interaction -> Behaviour -> Design -> Components -> Documentation."),
    ], size=16, gap=14)
    d.takeaway(s, "That is exactly what Week 15 is designed to test.")

    # 26. closing
    d.closing("REVISION & NEXT STEPS", [
        "Complete the ten-deliverable major assignment on a real information system.",
        "Cross-check your models: messages match operations, transitions have events.",
        "Use a CASE/UML tool to organise the University Registration case study.",
        "Next week: comprehensive revision and the integrated examination.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
