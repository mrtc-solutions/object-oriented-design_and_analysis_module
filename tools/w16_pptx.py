"""
Week 16 PPTX content — COMPREHENSIVE REVISION, INTEGRATED CASE STUDY AND EXAMINATION PREPARATION.
"""
from pptxengine import build

CFG = {
    "week": 16,
    "title": "Comprehensive Revision, Integrated Case Study and Examination Preparation",
    "filename": "Week16_Presentation_BICT3202_OOAD.pptx",
}


def slides(d):
    # 2. learning outcomes
    s = d.slide()
    d.header(s, "Learning Outcomes", "By the end of this week, you should be able to…")
    d.bullets(s, 0.9, 1.6, 11.6, 5.0, [
        ("Explain ", "the principles of OOAD and the strengths/limitations of OO development."),
        ("Distinguish ", "analysis from design; explain UML and its diagram families."),
        ("Construct ", "use-case, class, state, activity, sequence and communication diagrams."),
        ("Explain ", "relationships, inheritance, polymorphism and the Unified Process."),
        ("Combine ", "object, dynamic and behavioural models and check consistency."),
        ("Apply ", "OOAD to an unfamiliar problem and answer exam questions effectively."),
    ], size=16, gap=11)
    d.takeaway(s, "The student becomes the analyst / designer.")

    # 3. progression
    s = d.slide()
    d.header(s, "Week 15 -> Week 16", "From application to independence")
    d.pic(s, "w16_progression.png", y=1.6, w=10.6)
    d.takeaway(s, "Here is a real-world problem. Analyse it and design the system.")

    # 4. module picture
    s = d.slide()
    d.header(s, "The Entire Module in One Picture", "Connected stages, not exam topics")
    d.pic(s, "w16_module_picture.png", y=1.5, w=10.2)
    d.takeaway(s, "You should reproduce this journey from memory.")

    # 5. analysis vs design
    s = d.slide()
    d.header(s, "Analysis vs Design", "Understand the problem vs construct the solution")
    d.pic(s, "w16_analysis_design.png", y=1.6, w=10.6)
    d.takeaway(s, "Analysis = Student/Book/Loan · Design = LoanController/Service/Repository.")

    # 6. OO principles
    s = d.slide()
    d.header(s, "Core OO Concepts", "Object · Class · Encapsulation · Abstraction")
    d.pic(s, "w16_oo_principles.png", y=1.6, w=10.6)
    d.takeaway(s, "Class = blueprint · Object = instance · Encapsulation controls access.")

    # 7. inheritance & polymorphism
    s = d.slide()
    d.header(s, "Inheritance & Polymorphism", "Is-a relationships and one operation, many behaviours")
    d.pic(s, "w16_inheritance_polymorphism.png", y=1.6, w=10.6)
    d.takeaway(s, "Generalisation = UML relationship · Inheritance = implementation mechanism.")

    # 8. UML families
    s = d.slide()
    d.header(s, "UML Diagram Families", "Structural · Behavioural · Interaction")
    d.pic(s, "w16_uml_families.png", y=1.6, w=10.6)
    d.takeaway(s, "UML is a modelling language, not a programming language.")

    # 9. use-case relations
    s = d.slide()
    d.header(s, "Actors, Use Cases, Include & Extend", "The goal an actor accomplishes")
    d.pic(s, "w16_use_case_relations.png", y=1.6, w=10.6)
    d.takeaway(s, "Include = required · Extend = optional — do not use them randomly.")

    # 10. class notation
    s = d.slide()
    d.header(s, "Class Diagram Notation", "Attributes, operations and visibility")
    d.pic(s, "w16_class_notation.png", y=1.6, w=10.6)
    d.takeaway(s, "+ public · - private · # protected · ~ package.")

    # 11. relationships
    s = d.slide()
    d.header(s, "Class Relationships", "Association · Aggregation · Composition · Generalisation")
    d.pic(s, "w16_relationships.png", y=1.6, w=10.6)
    d.takeaway(s, "Choose the diamond from ownership/lifecycle, not aesthetics.")

    # 12. multiplicity
    s = d.slide()
    d.header(s, "Multiplicity", "How many objects can participate")
    d.pic(s, "w16_multiplicity.png", y=1.6, w=10.6)
    d.takeaway(s, "1 · 0..1 · * · 0..* · 1..* — Student 1 — 0..* Registration.")

    # 13. state diagram
    s = d.slide()
    d.header(s, "State Diagram: Course Lifecycle", "Events cause transitions")
    d.pic(s, "w16_state_diagram.png", y=1.5, w=10.4)
    d.takeaway(s, "Dynamic modelling asks “what happens?”, not “what exists?”.")

    # 14. sequence vs activity
    s = d.slide()
    d.header(s, "Sequence vs Activity", "A classic exam comparison")
    d.pic(s, "w16_sequence_vs_activity.png", y=1.6, w=10.6)
    d.takeaway(s, "Sequence = who talks to whom? · Activity = what happens next?")

    # 15. integration chain
    s = d.slide()
    d.header(s, "Full Model Integration", "One requirement traced through every model")
    d.pic(s, "w16_integration_chain.png", y=1.5, w=10.4)
    d.takeaway(s, "Requirement -> Use Case -> Classes -> Sequence -> State -> Activity -> Design.")

    # 16. consistency
    s = d.slide()
    d.header(s, "UML Model Consistency", "Six checks")
    d.pic(s, "w16_consistency.png", y=1.5, w=10.4)
    d.takeaway(s, "checkCapacity() vs checkAvailableSeats() — are they the same operation?")

    # 17. USDP
    s = d.slide()
    d.header(s, "The Unified Process — Four Phases", "Iterative and incremental")
    d.pic(s, "w16_usdp.png", y=1.6, w=10.6)
    d.takeaway(s, "Inception -> Elaboration -> Construction -> Transition.")

    # 18. iterative
    s = d.slide()
    d.header(s, "Iterative Development", "Build, evaluate, learn, repeat")
    d.pic(s, "w16_iterative.png", y=1.6, w=10.6)
    d.takeaway(s, "Iterations are planned, measured intervals within phases.")

    # 19. reuse
    s = d.slide()
    d.header(s, "Software Reuse", "Use what exists — wisely")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Reuse: ", "component, class, library, framework, service, design, architecture."),
        ("Benefits: ", "less duplication, less effort, better consistency, easier maintenance."),
        ("But: ", "base reuse on suitability, security, maintainability, compatibility, licensing."),
    ], size=16, gap=14)
    d.takeaway(s, "Reuse should not be “because something already exists.”")

    # 20. mobile money
    s = d.slide()
    d.header(s, "Case Study: Mobile Money System", "Actors · inheritance · associations · send money")
    d.pic(s, "w16_mobile_money.png", y=1.5, w=10.4)
    d.takeaway(s, "User <- Customer/Agent/Admin · Customer 1—1 Wallet · Wallet 1—0..* Transaction.")

    # 21. practical challenge
    s = d.slide()
    d.header(s, "Practical Challenge", "Six diagrams + one deliberate error")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Diagrams: ", "use-case, class, sequence (Send Money), activity, state (Transaction), component."),
        ("Introduce: ", "sequence calls validateTransaction() but the class has checkTransaction()."),
        ("Then: ", "identify the inconsistency and correct it."),
    ], size=16, gap=14)
    d.takeaway(s, "Modelling is complete when the model is logically consistent.")

    # 22. exam approach
    s = d.slide()
    d.header(s, "How to Approach an Exam Scenario", "Never start drawing immediately")
    d.pic(s, "w16_exam_approach.png", y=1.5, w=10.4)
    d.takeaway(s, "Read twice -> nouns -> objects -> actors -> use cases -> models -> consistency.")

    # 23. exam strategy
    s = d.slide()
    d.header(s, "Exam Answering Strategy", "Definition · Explain · Compare · UML")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Define: ", "full definition, then an example."),
        ("Explain: ", "Definition -> Explanation -> Example -> Importance."),
        ("Compare: ", "use a table (class vs object: meaning, memory, example, quantity)."),
        ("UML: ", "requirement -> actors -> use cases -> classes -> relationships -> behaviour -> consistency."),
    ], size=15, gap=12)
    d.takeaway(s, "Examiners mark correct modelling, not artistic decoration.")

    # 24. mock exam
    s = d.slide()
    d.header(s, "Full-Length Practice Papers", "Two parallel forms; sit one under timed conditions")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("Paper A: ", "Community Clinic Appointment System."),
        ("Paper B: ", "Campus Equipment Lending System."),
        ("Format: ", "100 marks; Question 1 compulsory (40); choose any three of Questions 2–5 (20 each)."),
        ("Approval: ", "3 hours is a proposed duration; confirm Faculty rules. Marking guide is lecturer-only."),
    ], size=16, gap=14)
    d.takeaway(s, "The course outline weights the examination at 60% of the module grade.")

    # 25. summary
    s = d.slide()
    d.header(s, "Final Takeaway", "The whole module in one question")
    d.bullets(s, 0.9, 1.6, 11.6, 4.9, [
        ("1. ", "OOAD is not simply about drawing UML diagrams."),
        ("2. ", "Think systematically: identify what matters, how things interact and behave."),
        ("3. ", "Transform understanding into a coherent design developers can implement."),
    ], size=16, gap=14)
    d.takeaway(s, "Business Problem -> Requirements -> … -> Model Integration -> Implementation.")

    # 26. closing
    d.closing("GOOD LUCK IN THE EXAMINATION", [
        "Work through the final revision checklist before sitting the exam.",
        "Practise the noun technique and the 12-step scenario process.",
        "Use the OMG UML 2.5.1 specification to verify notation.",
        "You are now ready to analyse and design real systems independently.",
    ])


def build_pptx():
    return build(CFG, slides)


if __name__ == "__main__":
    print("Built:", build_pptx())
