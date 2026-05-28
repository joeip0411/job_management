---
name: tailor-resume
description: "Generate a tailored, ATS-friendly Markdown resume by aligning a user's master resume to a specific job description. Reads tone and working-style cues from the JD (scrappy startup vs. enterprise, IC vs. collaborative, formal vs. casual), mirrors the JD's vocabulary, re-prioritizes achievements toward what the role values, and rewrites bullets in the target voice — without fabricating experience. Use this whenever a user asks to tailor, customize, adapt, rewrite, or align their resume to a job posting, JD, job ad, or role, even if they don't explicitly say 'tailor'. Triggers on phrases like 'rewrite my resume for this job', 'match my CV to this JD', 'help me apply to X', or 'make my resume fit this role'."
---

# Tailor Resume

Turn a master resume + a job description into a tailored Markdown resume that reads like it was written *for that role* — without inventing experience the user doesn't have.

The user supplies:
- A path to their **master resume** (the full, kitchen-sink version of their experience — Markdown, plain text, or similar)
- A path to a **job description** text file

You produce one file: `./generated_resumes/<Company> - <Role> Resume.md` (create the directory if it doesn't exist).

## Why this skill exists

A master resume is a dump of everything the user has done. A good tailored resume is the *subset* of that, re-framed and re-ordered, so a recruiter or hiring manager reading it for 20 seconds thinks "this person is exactly what we're looking for." The skill exists because doing this well requires three things at once — reading the JD for tone signals, picking the right achievements to surface, and rewriting bullets in a voice that matches the company — and it's easy to get one right while botching the others.

## Workflow

### 1. Read both inputs fully

Read the master resume and the JD end-to-end before writing anything. Do not skim. The master resume tells you what's *available*; the JD tells you what's *wanted*. Mismatches between the two are the most important signal in this whole task — they tell you what to emphasize, what to drop, and where you have a gap you cannot paper over.

### 2. Analyze the JD on four axes

Take a moment (you can do this in your head or scratchpad) to extract:

- **What the role does day-to-day.** Concrete responsibilities, not the marketing fluff. If the JD says "drive cross-functional initiatives" but the bullet list is "write SQL queries, build dashboards, present to leadership," the second is the real job.
- **What the company values.** Speed and shipping? Rigor and correctness? Customer obsession? Look at the adjectives and verbs. "Move fast, ship daily, iterate" reads very differently from "thoughtful, deliberate, high-quality."
- **The tone of voice.** Is the JD written in casual second-person ("you'll wear many hats")? Formal third-person ("the successful candidate will demonstrate...")? Punchy and short, or dense paragraphs? Your resume's bullet voice should rhyme with this.
- **The vocabulary.** Note 5–15 specific terms the JD uses — tools, methodologies, domain words, role-specific phrasings. These are the words the resume should naturally use (where the user's experience genuinely supports them).

### 3. Map master-resume content to JD priorities

For each experience block in the master resume, ask: *does this serve the JD?* Build a mental ranking:

- **Must-keep** — directly relevant; the bullet under it might need a rewrite but the role/project stays.
- **Could-keep, deprioritize** — adjacent or shows breadth; goes lower in the section or compresses to one line.
- **Drop** — not relevant to this JD. Cutting things is how you make room for the things that matter.

Within a kept role, do the same with bullets: surface and rewrite the ones aligned with the JD; drop or compress the rest.

### 4. Rewrite bullets in the target voice

This is where most tailoring goes wrong. Bullets should:

- **Lead with the achievement, not the activity.** "Reduced query latency by 40%" beats "Worked on optimizing queries."
- **Mirror the JD's vocabulary where it's honest.** If the JD says "experimentation" and the user's bullet says "ran A/B tests," prefer "experimentation" — same thing, their word. If the JD says "LLM evaluation" and the user did "model testing," check whether it really was LLM eval before swapping. Never swap in a term the experience doesn't actually support.
- **Match the JD's energy.** A scrappy startup JD wants bullets that feel scrappy: short, verb-forward, outcome-focused, comfortable with ambiguity. A regulated-industry enterprise JD wants bullets that feel measured: precise, methodology-aware, comfortable with process. Same achievement, different framing.
- **Quantify where the master resume has numbers.** Don't make numbers up. If the master resume says "improved performance," you can rewrite the verb but you cannot invent "by 35%."

### 5. Assemble the Markdown file

Default section order (deviate if the master resume's structure or the role obviously calls for something else):

1. Name + contact (preserve exactly from master resume)
2. A 2–3 line summary tuned to this role (optional — include if the master resume has one or if a strong fit narrative emerges)
3. Experience (most-recent first, with the prioritization from step 3 applied)
4. Projects (if relevant to the JD; otherwise drop)
5. Education
6. Skills (curate to what's in the master resume AND relevant to the JD; don't list every tool the user has ever touched)

Use clean Markdown — `##` for section headers, `###` for role/company, bullets with `-`. No HTML, no tables unless the master resume uses them.

### 6. Save the file

Write to `./generated_resumes/<Company> - <Role> Resume.md`. Sanitize the filename: strip `/ \ : * ? " < > |`, collapse whitespace. If `Company` or `Role` can't be confidently extracted from the JD, **stop and ask the user** — never write a file with `Company` or `Role` as literal text.

After writing, tell the user:
- The output path
- A 2–3 sentence summary of what you tailored toward (the tone you picked up, the achievements you surfaced) — this is how the user calibrates trust in the output

## Guardrails (do not violate)

These exist because each one corresponds to a way tailored resumes commonly go wrong — and a way they get the user rejected or, worse, fired after they're hired.

- **Never fabricate experience.** No invented projects, roles, dates, tools, certifications, or metrics. Re-framing what's in the master resume is the entire game; if the JD asks for something the master resume doesn't show, leave the gap honest rather than papering over it. (You may flag the gap to the user at the end, but do not fill it in the resume itself.)
- **Preserve dates and employers exactly.** Company names, titles, and employment dates are immutable. You can rephrase a title only if the master resume's title is verbatim ambiguous (e.g., "Engineer I" → "Software Engineer I" if the role context makes it clear) — when in doubt, leave it.
- **No buzzword stuffing.** If a JD keyword doesn't naturally fit a bullet, leave it out. A resume that reads like a keyword salad fails the human read even if it passes the ATS. The win is keywords *flowing through* genuine accomplishments, not keywords *appended to* them.

## Edge cases

- **JD is sparse / one paragraph.** Do your best with the tone signals you have; default to a neutral, achievement-forward voice. Mention in your summary-to-user that the JD was light on signal.
- **Master resume is much longer than the role needs.** Aggressive cutting is correct. A focused 1.5-page tailored resume beats a 3-page everything-bagel.
- **JD is for a role the user is clearly under-qualified for.** Tailor honestly anyway. Don't invent seniority. Surface what's most relevant and let the user decide whether to apply.
- **Multiple roles in the JD file.** Ask the user which role to tailor for.

## Reference

See `references/tone-examples.md` for side-by-side bullet rewrites under different JD tones — useful when you're unsure how far to push the voice shift.
