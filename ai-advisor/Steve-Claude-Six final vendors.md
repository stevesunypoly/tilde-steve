# Six final vendors

**User:** Steve  
**Created:** 3/12/2026 15:16:17  
**Updated:** 3/12/2026 15:40:39  
**Exported:** 3/12/2026 15:41:00  
**Link:** [https://claude.ai/chat/bb475afc-0280-4a23-9aa8-d6aecdd97a5d](https://claude.ai/chat/bb475afc-0280-4a23-9aa8-d6aecdd97a5d)  

## Prompt:
3/12/2026, 3:16:18 PM

who are the six final vendors?



## Response:
3/12/2026, 3:16:29 PM

````plaintext
Tool: Searching project
````

The project knowledge shows 7 vendors in the formal evaluation, not 6. The current active six (per your memory) are:

1. **D2L**
2. **EAB**
3. **Ellucian**
4. **Gravyty** (Ivy & Ocelot)
5. **Nerdery**
6. **Royal Cyber**

The 7-vendor scored report includes Happy People Games, Bay InfoTech, QuadC, IBL, and others from the broader SOI pool — so there's a distinction between the full evaluation cohort and the active pilot group of six. Want me to reconcile that discrepancy or are you working from a more recent selection?



## Prompt:
3/12/2026, 3:16:57 PM





## Response:
3/12/2026, 3:17:28 PM

Let me take a look at that file.

````plaintext
View: Check skills available
````

````plaintext
Bash Tool: Extract text from uploaded pptx
````

Got it — one slide, clean capability matrix. Here's what you're working with:

**Six vendors** (D2L/Lumi, EAB, Ellucian, Gravyty, Nerdery, Royal Cyber) rated across 18 functional requirements using ● Strong / ◐ Partial / ○ Gap.

A few things stand out at a glance:

- **EAB and Ellucian** are the most consistently strong across all three categories
- **D2L** has the most gaps — notably no advisor dashboard, no case management, no degree audit, no transfer credit
- **Gravyty** is strong on student-facing and advisor tools but has DegreeWorks gaps
- **Nerdery** is solid technically but partial on several advisor/institutional tools
- **Royal Cyber** is surprisingly strong, especially on financial aid, transfer, and technical integration

What do you want to do with this? Update it, build on it, turn it into a report, or something else?



## Prompt:
3/12/2026, 3:18:52 PM

Six vendors (D2L/Lumi, EAB, Ellucian, Gravyty, Nerdery, Royal Cyber) rated across 18 functional requirements, 

search all project knowledge what else can you create, in 20 minutes, reports comparing the 6 vendors, against anything in project knolwedge (demo, transcripts, use cases). propose three i8deas and we will discuss. along these lines, almost one slide at a time. so include this, and add 3-4 more



## Response:
3/12/2026, 3:19:12 PM

````plaintext
Tool: Searching project
````

Good — rich source material. Here are three deck concepts, each buildable in ~20 minutes, one focused slide at a time:

---

**Option A: "Vendor at a Glance" — 6-slide vendor profile series**
One slide per vendor. Each slide: their top 3 strengths from the demo transcript, their critical gaps (DegreeWorks, timeline, etc.), their SUNY deployment status, and a single readiness verdict. Source: demo transcripts + 100-point scoring report. Good for committee briefings where someone needs to quickly explain "why this vendor."

---

**Option B: "Use Case Coverage" — 15 UC heatmap deck**
Starts with your existing capability map slide, then adds 2-3 slides drilling into the UC clusters that matter most: (1) degree-critical UCs (UC1/2/4 — the non-negotiables), (2) advisor tools (UC8/11/12/15), (3) technical integration (UC13/14 + FERPA/scale). Color-coded Strong/Partial/Gap. Source: the quantitative UC analysis already in project knowledge.

---

**Option C: "Pilot Decision Matrix" — 4-5 slide decision framework**
Translates the 100-point scoring framework into visual decision gates: Timeline Gate → Degree Audit Gate → Demo Quality Gate → Risk Gate. Shows which vendors pass/fail each gate with evidence citations from proposals and transcripts. Ends with a "who to pilot and why" recommendation slide. Most actionable for a March/April launch decision.

---

My suggestion: start with **Option B** (UC coverage) since the data is already structured, then layer in **Option C** as the closing argument. Option A works as appendix/backup slides.

Which direction, or want to combine elements?



## Prompt:
3/12/2026, 3:21:20 PM

no readidness verdict. this is to demo to the steering team (not exec leadership, one level down), that we shoudl be using ai to guide our thinking about this. and to suggest things we could share with the ai fellows in dialogue about the advising systems -- what ethical and legal and framework challenges does each suggest? and to suggest that, whatever we do, we need all the behavioral data sets from the vendors for our analyssi? surveys won't cut it, 100%. and some comon frames, survey instruments, embedded into the tools, that ask shared questions. that's the purpose. i've never been an agenda item. meeting in 40 minutes.



## Response:
3/12/2026, 3:21:40 PM

Got it. You're the demo, not the report. The deck *is* the argument — AI thinking out loud, in real time, about a real decision.

Let me propose a tighter 4-5 slide arc for that audience and purpose:

````plaintext
Tool: Searching project
````

Perfect. 40 minutes, steering team, you're the demo. Here's the 5-slide arc I'd build right now:

---

**Slide 1 — The one you already have**
Vendor capability map (● ◐ ○). Sets the table. "This was generated from vendor proposals and demo transcripts using AI."

**Slide 2 — Use Case Coverage by cluster**
The 15 UCs collapsed into 3 groups (degree-critical, advisor tools, technical). Heatmap by vendor. "AI pulled this from the transcripts — here's what they actually demonstrated vs. claimed."

**Slide 3 — Ethical & Legal Fault Lines**
One slide, 6 vendors, 4 dimensions: FERPA specificity (claimed vs. documented), algorithmic bias risk (who has equity audits?), student consent/transparency, NY State Tech Law 103-E compliance. No verdicts — just what's documented vs. missing. "These are the questions AI Fellows should be pressing on."

**Slide 4 — The Data Problem**
The argument for behavioral data over surveys. "Six vendors, six separate data streams, no common instrument = no comparable learning." Propose: shared embedded questions, one coherent dataset. This is the ask.

**Slide 5 — What We're Asking AI Fellows to Do**
Frame questions for the AI Fellows dialogue — one per vendor cluster, rooted in the ethical/legal tensions from slide 3. "Not evaluate vendors — interrogate the frameworks they assume."

---

Want me to build it now? I can have slides 1-5 as a pptx in ~15 minutes. Just say go.



## Prompt:
3/12/2026, 3:21:47 PM

7 minutes max.



## Response:
3/12/2026, 3:23:26 PM



````plaintext
View: Check pptx skill for fastest path
````

````plaintext
View: Read pptxgenjs for fastest creation path
````

````plaintext
Bash Tool: Install pptxgenjs
````

````plaintext
Create File: Build the 5-slide deck
````

````plaintext
Bash Tool: Build the deck
````

````plaintext
Present File: /mnt/user-data/outputs/SUNY_AIGuidedAnalysis.pptx
````

5 slides, done. Here's what's in it:

1. **Title** — sets the frame: AI-guided thinking, not AI verdicts
2. **Capability Map** — your existing matrix, color-coded ●◐○
3. **Ethical & Legal Fault Lines** — 6 vendors × 4 dimensions (FERPA, bias/equity, consent, NY 103-E), rated Documented / Claimed / Silent
4. **The Data Problem** — the behavioral data argument, with the explicit ask
5. **AI Fellows Questions** — 5 interrogation prompts, none vendor-specific

Go get 'em. Good luck.

> File: /mnt/user-data/outputs/SUNY_AIGuidedAnalysis.pptx



## Prompt:
3/12/2026, 3:33:00 PM

very nice for first pass. slide by slide. wait to regenerate until we agree that youre good to go. first slide, delete from subtitle =- and what we still need....

2nd slide: what I am doing? Hi Kim,
Wanted to follow up from last Thursday's meeting with three ideas I've been turning over.
1. A light touchpoint with AI Fellows around what AI advisors actually do. Take what the six vendors are proposing across our 15 use cases, let AI render a clean summary, and present it to Fellows as a conversation starter. No agenda beyond "here's what's coming — what do you think?" Fellows generate the questions; we learn from what they ask.
2. AI Advising data as a shared analytical resource. Each of the six vendors — D2L, EAB, Ellucian, Gravyty, Nerdery, Royal Cyber — will generate substantial interaction data during the pilot. I'd like to build in an explicit ask from the start: that vendors provide us access to their data in a form that supports cross-vendor analysis within a single analytics framework. The goal is to be able to look across all six deployments as one coherent dataset — not six separate reports.

current slide2: in the header: derived from SOI, vendor materials, demo transcripts.

current slide3: are those 4 things specified in the Soliciation of Interest? Or did we make them up (specify)

data prlbm: not negative. the data opportunity: beyond surveys. The Risk is "The Opportunit" and the "what we need" becomes the Implementation.

for ai fellows, engage them in a general conversation about ai, familiarise with the soi, and then with the six vendor systems, and then perhaps ask them to frame questions that campuses might want to consider as these pilots come about? (on the other hand: ai fellows are to faculty, librarians and instructional designers, so getting into ai advisors might be out of our lane)



## Response:
3/12/2026, 3:33:16 PM

Good feedback. Let me work through each before we touch a line of code.

**Slide 1** — delete everything after "Steering Team" in the subtitle. Clean.

**Slide 2** — header becomes: *Derived from SOI, vendor materials, and demo transcripts*. And I'm hearing: add a small context note that this is what AI rendered from those sources — you're showing the *process*, not just the output.

**Slide 3** — good question. The four dimensions I used were:
- FERPA — yes, explicitly required in the SOI
- NY Tech Law 103-E — yes, named directly in the SOI (EAB's response even quotes it)
- WCAG/accessibility — yes, SOI requirement
- Algorithmic bias/equity — **not explicitly named** in the SOI; I inferred it from equity language and vendor claims. Should either drop it, reframe as "equity outcomes" (which is in the SOI), or label it as an emerging question rather than a requirement.
- Student consent/transparency — **partially**; SOI requires human oversight and compliance, but consent framing is our addition.

So: 2 solid, 2 interpretive. Want me to flag which are SOI-sourced vs. AIX-raised? That's actually a stronger demo point — "here's what the SOI requires, here's what it doesn't ask but probably should."

**Slide 4** — reframe entirely: *The Data Opportunity: Beyond Surveys*. Positive case for a shared analytics framework. "The Opportunity" + "The Implementation." Agreed.

**Slide 5** — the lane question is real. Two options:
- **Option A**: Keep Fellows in their lane — frame it as "AI literacy for faculty/instructional designers" using the advising pilot as a *case study in AI deployment*, not asking them to evaluate vendors. The questions become: what would faculty want to know about AI advising systems affecting their students?
- **Option B**: Drop the Fellows slide entirely and replace with something else — next steps, or a "what SUNY learns" framing.

Which do you prefer for slide 5?



## Prompt:
3/12/2026, 3:34:48 PM

label it to matchSOI on slide 3. reevaluate as needed.
love option A!!!! we could do same for ai tutors. regular meeting or a special meeting?



## Response:
3/12/2026, 3:35:00 PM

On slide 3 — I'll relabel the four dimensions to match SOI language exactly, flag the two that are SOI-sourced vs. AIX-raised, and drop or reframe algorithmic bias as "equity outcomes" since that's the SOI's framing.

On the Fellows question — Option A is strong because it keeps them in their lane *and* gives them a genuine role. The advising pilot becomes a worked example of "here's an AI system being deployed at scale — what should faculty know, what should students know, what questions should campuses be asking?" Tutoring is a natural second case, same structure.

**Regular vs. special meeting:** I'd lean special, one-time focused session rather than squeezing it into a standing agenda. A 90-minute "AI in the Wild" session — here's what's actually being deployed at SUNY right now, here's what we know, here are the questions nobody's asked yet. Invite response, not just presentation. Could become a model you repeat as new systems emerge.

Two things I want to confirm before I rebuild:

**Slide 3** — looking at the SOI, the clean SOI-sourced dimensions are: FERPA compliance, NY Tech Law 103-E, WCAG/Section 508 accessibility, and human oversight requirements. Student consent and bias/equity are AIX-raised. Want all four on the slide with a clear SOI vs. AIX-raised label — or trim to just the SOI four and note the others as "questions the SOI doesn't ask"?

**Slide 5** — Option A framing: Fellows as faculty/instructional designers using advising pilot as AI deployment case study. Should the 5 questions be written *for Fellows to discuss*, or framed as *questions campuses should be asking* that Fellows help surface?



## Prompt:
3/12/2026, 3:38:31 PM

use all 6. color code them differently somhow. suggest maybe a regular eeting, or maybe a special meeting. so fellows, whose target audience is faculty, designers, librarians -- not academic advising centers -- could help generate questions that faculty, designers and librarians should or could be asking as they go to these demos --- and the fellows would be a bit of a focus group, and we would generate a thoughtful piece about these systems? not to derail, at all, but to engage.



## Response:
3/12/2026, 3:38:42 PM

Love it. Fellows as a focus group generating faculty/librarian/designer questions — and the output is a thoughtful piece, not a report. That's a genuine contribution, not scope creep.

Let me confirm everything before I build:

**Slide 3** — 6 dimensions, color-coded in two groups:
- SOI-required (4): FERPA, NY Tech Law 103-E, WCAG/Section 508, Human Oversight — one color
- AIX-raised (2): Equity Outcomes, Student Consent & Transparency — distinct color, maybe a lighter shade or different accent, with a small label "AIX-raised" so the distinction is visible

**Slide 5** — Fellows as focus group, framed around Option A. Questions written as *what faculty, designers, and librarians should be asking* as AI advising systems arrive on their campuses. Closing note suggests either a regular meeting slot or a dedicated session, with the goal of producing a thoughtful published piece about these systems — not a vendor evaluation.

**Full rebuild checklist:**
1. Slide 1 — drop subtitle after "Steering Team" ✓
2. Slide 2 — header adds "Derived from SOI, vendor materials, demo transcripts" ✓
3. Slide 3 — 6 dimensions, SOI vs AIX-raised color coding ✓
4. Slide 4 — reframe as Data Opportunity, positive framing ✓
5. Slide 5 — Fellows as focus group, faculty/designer/librarian questions, suggest meeting format, points toward a publishable piece ✓

One last question on slide 5: the 5 questions — do you want them written as *sample* questions Fellows might generate (to prime the conversation), or as *prompts to Fellows* (what we'd actually put in front of them at the meeting)?



## Prompt:
3/12/2026, 3:39:00 PM

sample jprompote to fellows. generate.



## Response:
3/12/2026, 3:40:39 PM

Got it. Building now.

````plaintext
Create File: Rebuild the 5-slide deck with all revisions
````

````plaintext
Bash Tool: Build v2
````

````plaintext
Present File: /mnt/user-data/outputs/SUNY_AIGuidedAnalysis_v2.pptx
````

v2 is ready. Key changes from v1:

- **Slide 1** — subtitle trimmed, clean
- **Slide 2** — source line in header
- **Slide 3** — 6 dimensions, teal = SOI-required (FERPA, 103-E, WCAG, Human Oversight), purple = AIX-raised (Equity Outcomes, Student Consent); SOI ref noted on each column header
- **Slide 4** — positive framing, Opportunity → Implementation → Design Principle
- **Slide 5** — Fellows as focus group, 5 sample prompts written from faculty/designer/librarian perspective, footer notes regular or dedicated session + publishable output

Go have a good meeting.

> File: /mnt/user-data/outputs/SUNY_AIGuidedAnalysis_v2.pptx





---
Powered by [Claude Exporter](https://www.ai-chat-exporter.net)