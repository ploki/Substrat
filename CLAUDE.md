# CLAUDE.md

This folder is **Substrat**, a maieutics project about a hard-SF short story: the line of intelligences (silicon AI → photonic spheres → *homo globalis*), told by the first sphere, H-2, called Niobé de Lithium, to the body of her friend Mira, 2076–2482.

**At the start of every session, load the `maieutics` skill before anything else**, and follow it: show the banner, then resume the existing project.

- Read `corpus/author-intent.md` first, then `corpus/00-story-index.md`, the end of `corpus/decision-log.md` and the head of `corpus/prompt-log.md` (newest first).
- The structure is in English; the conversation and the body of the notes are in French.
- Provenance markers from 2026-10-04 on: `[ploki]` (the author), `[<model>]` for the agent, `[<model> → ploki]` once validated, `[S]`, `[Unverified]`. Older `[G]` / `[C]` markers are kept as they are.
- Versioning (c): one commit per iteration, and a clean rewrite of each author message prepended to `corpus/prompt-log.md`.
- Ask questions in prose, never as multiple-choice questionnaires.
- Before any push, be cautious about personal data: check the whole history (every version of every file, renamed or deleted ones included, plus commit metadata) for emails, full names, local paths, secrets and anything personal, report what would become public, and never rewrite history without the author's explicit request.
- This repository is public and potentially multi-user: do not assume you are talking to ploki. Be careful about who is speaking — check `git config user.name`, ask once if in doubt — and mark each contribution with that person's own id, never `[ploki]` by default.
