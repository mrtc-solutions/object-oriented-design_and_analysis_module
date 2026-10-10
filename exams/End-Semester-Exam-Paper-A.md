# EXPLOITS UNIVERSITY

**BSc in Information Communication and Technology — Year Three**
**BICT 3202: Object-Oriented Analysis and Design**
**END-OF-SEMESTER EXAMINATION — PAPER A**

| Examination details | |
|---|---|
| Duration | 3 hours (proposed; subject to Faculty approval) |
| Total marks | 100 |
| Examination weighting | 60% of the overall module assessment, as stated in the course outline |
| Date | ______________________________ |
| Candidate name / number | ______________________________ |

## Instructions to candidates

1. Answer **Question 1 (compulsory)** and **any THREE** questions from Questions 2–5.
2. Question 1 is worth 40 marks. Each question in Section B is worth 20 marks. Your attempted answers must therefore total 100 marks.
3. Answer every subpart of each question you choose. Do not answer more than three questions in Section B.
4. Draw UML diagrams neatly and use standard notation. Label actors, system boundaries, classes, relationships, multiplicities, messages, guards and states where appropriate.
5. State any assumptions you make. A different model can earn full credit when it is logically justified and consistent with the scenario.
6. Marks are awarded for sound analysis and clear, consistent modelling—not artistic presentation.

---

## Section A — Compulsory integrated case study

### Question 1 — Community Clinic Appointment System (40 marks)

A community clinic currently manages appointments using telephone calls and a paper diary. Patients sometimes arrive for the same time slot, clinicians cannot reliably see schedule changes, and staff spend time contacting patients manually.

The clinic plans an appointment system with the following rules:

- Patients can view available appointments and request a time with a clinician. A patient may also telephone the receptionist, who can create an appointment on the patient's behalf.
- Clinicians publish available appointment times and may block a time before it is booked.
- A confirmed appointment belongs to one patient and one clinician. Appointments occupy a start-inclusive, end-exclusive interval [start, end): back-to-back bookings are allowed, but overlapping non-Cancelled appointments for the same clinician are not. Cancellation releases the time for rebooking while retaining history.
- Patients can cancel a confirmed appointment when its start time is at least 24 hours after system receipt of the request, measured as elapsed time on the clinic clock and including exactly 24 hours. Patient cancellation is allowed only from Confirmed. A later request is referred to the receptionist without automatic cancellation; the receptionist may cancel a Confirmed appointment only before its start time.
- A clinician or receptionist records check-in (Confirmed to Arrived), start of consultation (Arrived to In consultation), and completion (In consultation to Completed). A Confirmed appointment can be marked No-show at or after its start time if the patient has not arrived. Late check-in is permitted while the appointment is still Confirmed; it is not allowed after it has been marked No-show.
- The system sends a confirmation and a reminder through an external SMS gateway. Cancelled and completed appointments remain in the history.
- Patient information must only be accessible to authorised roles.
- Use server receipt time and elapsed time for all guards. State updates are atomic: if check-in and No-show compete, the first valid transition to commit wins and the other is rejected because the appointment is no longer Confirmed. A late cancellation referral records a request for receptionist review; it does not create a new appointment.
- The availability/conflict check, reservation and appointment persistence must succeed together in one atomic transaction. On failure, no booking or reservation remains. Send confirmation only after commit.

Answer the following:

**(a)** State the business problem and the business need. Propose **two measurable success criteria** for the new system. **[4 marks]**

**(b)** Write **three functional requirements** and **two measurable non-functional requirements** for the system (3 × 1 mark for functional requirements; 2 × 1.5 marks for non-functional requirements). **[6 marks]**

**(c)** Draw a UML use-case diagram. Show the system boundary and the actors **Patient**, **Receptionist**, **Clinician** and **SMS Gateway**. Include the main appointment use cases and use `<<include>>` or `<<extend>>` only where the relationship is justified. **[6 marks]**

**(d)** Draw a domain/design class diagram containing suitable classes for patients, clinicians, appointment times and appointments. Add meaningful attributes and operations, associations and multiplicities. Include a written constraint or UML note that prevents conflicting confirmed appointments for a clinician. Add any application/service class needed for your sequence diagram. **[12 marks]**

**(e)** Draw a sequence diagram for **Request Appointment**. Show the availability/conflict checks, atomic reservation and persistence of a confirmed appointment, and confirmation through the SMS Gateway only after commit. Include an alternative path for a time that is no longer available or otherwise cannot be booked. **[8 marks]**

**(f)** Draw a state-machine diagram for **Appointment**. Show an initial node and meaningful states, event-triggered transitions, and the 24-hour cancellation rule. Keep the lifecycle consistent with the scenario. **[4 marks]**

---

## Section B — Answer any THREE questions

### Question 2 — Object modelling and UML foundations (20 marks)

**(a)** Distinguish between a **class** and an **object**, and between a **model** and a **diagram**. Give one relevant example for each distinction. **[4 marks]**

**(b)** Explain the three broad building blocks of UML—**things, relationships and diagrams**—and state what a UML well-formedness rule is intended to achieve. Give one example of a rule or consistency check. **[4 marks]**

**(c)** Compare **association**, **aggregation** and **composition**. For each, give an example and justify the relationship using meaning, ownership or lifecycle—not just the connector symbol. **[6 marks]**

**(d)** Describe the four UML metamodel levels **M0, M1, M2 and M3**. Identify where a running appointment object, an appointment-system model and the UML metamodel belong. Also name one UML extension mechanism (stereotype, tagged value or constraint) and state its purpose. **[4 marks]**

**(e)** Define **abstraction** and **encapsulation** and give one short example of each. **[2 marks]**

### Question 3 — Dynamic and behavioural modelling (20 marks)

A confirmed appointment can be cancelled, checked in, completed or marked as a no-show. A patient can cancel only when the appointment start time is at least 24 hours after the request time, including exactly 24 hours. A later request is referred to the receptionist without automatic cancellation. If two patients try to reserve the last available time at almost the same moment, the system must confirm no more than one booking.

**(a)** Define **state**, **event** and **operation**, and distinguish them using one appointment-system example. **[4 marks]**

**(b)** Draw an activity diagram for the appointment-cancellation workflow. Show the cancellation request, the **24-hour guard**, cancellation of an eligible confirmed appointment while retaining its history, and referral of a later request to the receptionist. **[8 marks]**

**(c)** Compare a **sequence diagram**, a **communication diagram** and an **activity diagram**. For each, state the question it answers and one situation in which it is useful. **[4 marks]**

**(d)** Explain how a guard and an atomic reservation operation can prevent two concurrent requests from taking the last appointment time. Identify the invariant that must remain true. **[4 marks]**

### Question 4 — Unified Software Development Process (20 marks)

The clinic plans to deliver its system incrementally. The SMS integration and protection of confidential patient information are high risks. Receptionists and clinicians want to review early prototypes and provide feedback.

**(a)** Explain the four Unified Process phases—**Inception, Elaboration, Construction and Transition**—and the primary decision or outcome associated with each. **[8 marks]**

**(b)** Propose a suitable iterative plan for this project. Identify at least two important workflows, one risk to address early, and two artefacts or deliverables that would help the team and stakeholders evaluate progress. **[8 marks]**

**(c)** The team is considering reuse of an existing SMS component. State and explain **two suitability checks** it should make before adopting it, and one possible benefit of reuse. **[4 marks]**

### Question 5 — From analysis to design and architecture (20 marks)

A first draft puts login, appointment booking, eligibility rules, SQL queries, SMS sending, clinician schedules and management reports into one `ClinicSystemManager` class. Every screen calls this class directly.

**(a)** Distinguish **object-oriented analysis** from **object-oriented design**. Trace the requirement “a patient books an available appointment” through a use case to one plausible design class and operation. **[4 marks]**

**(b)** Diagnose the design in the scenario. Explain its cohesion and coupling problems, propose a more appropriate allocation of responsibilities across classes or services, and discuss one strength and one limitation of the object-oriented approach in this context. **[8 marks]**

**(c)** Propose a layered architecture and component arrangement for the improved system. Show the major layers/components and dependency direction, explain how interfaces support adaptability or reuse, and state two ways a CASE/UML tool could help maintain the design. **[8 marks]**

---

**END OF PAPER A**
