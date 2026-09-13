# Nick

Founder, [Allocera Intelligence](https://alloceraintelligence.com) — building CDAI and VINDEX. Also operate Full Send Organicks LLC.

I build backend systems and automation that touch real money and real operations — lead pipelines, margin reconciliation, deal analysis — and ship them to production alone, end to end: schema, API, integrations, deploy, and the incident write-up when something breaks.

📫 **nick@alloceraintelligence.com** · [LinkedIn](https://www.linkedin.com/in/nick-b-57a14821b/)

---

### What I've shipped

| Project | What it does | Stack |
|---|---|---|
| **[Sofl-Wholesale](https://github.com/fullsendorganicks-collab/Sofl-Wholesale)** | Backend for a real estate wholesaling operation — sources distressed-property leads from BatchData, scores and analyzes deals, drafts offers, matches buyers, and generates contracts. Runs a live daily automated brief. | Python, FastAPI, PostgreSQL |
| **[cdai-calculator](https://github.com/fullsendorganicks-collab/cdai-calculator)** | Standalone lead-capture microservice for Allocera's margin distortion calculator — OTP-verified email capture, live results delivery, Beehiiv newsletter integration. Deployed independently of the main engine with its own isolated schema. | Python, FastAPI, PostgreSQL |
| **[command-center](https://github.com/fullsendorganicks-collab/command-center)** | A unified operations dashboard consolidating email, analytics, and site management behind one login — Google OAuth, a Claude-powered chat assistant wired through a secured edge function, and a Supabase schema with row-level security scoping every table to its workspace. | React, Vite, Supabase |

### How I work

- I write down what actually happened when something breaks — real error, root cause, real fix, not a guess. [Sofl-Wholesale's admin manual](https://github.com/fullsendorganicks-collab/Sofl-Wholesale/blob/master/ADMIN_MANUAL.md) is a live example: a real billing incident, the wrong assumption that caused it, and the fix that shipped.
- I don't ship claims I can't back with a number. Allocera's directive engine is scored for accuracy on a 30-day retest cycle, not just shipped and left alone.
- Solo-founder pace: I'm the backend, the ops, and the person on call when a pipeline burns budget overnight. These repos reflect that — real incidents, real fixes, no filler.

---

*Open to backend/full-stack contract work, and talking to anyone interested in Allocera's CDAI margin-reconciliation engine.*
