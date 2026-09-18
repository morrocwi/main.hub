# GOAL

**Outcome.** An AI agent that has never seen the programme lands on this repository and, without
asking anyone, reaches the right public repository, the right file and the right gate for its
task - reading a handful of files instead of cloning and searching a dozen repositories.

**How we will know.**
- A fresh agent given only this repository's URL and a task picks the route a maintainer would pick.
- In paired runs with and without Step 0, the Step 0 runs restate a reported claim as a fact less
  often (an untested hypothesis, recorded with its falsifier in `logbook.jsonl`).
- `python scripts/hub.py check --remote` passes: every pin resolves, every edge's evidence is present.
- No research content, non-public name or local detail is ever found in a tracked file.

**What would count as this hub failing** (record it in `logbook.jsonl` as a `negative_result`):
- an agent following a route arrives at a file that does not answer the route's question;
- an edge passes the checker while the relation it states is false in the target repository;
- the hub is trusted over a repository that has moved on, and work is done against a stale pin;
- agents run with and without Step 0 show no difference in how they treat unverified claims
  (then Step 0 is ceremony and should be removed or changed);
- a lens facet label drifts from the one sentence it paraphrases, or a surface is listed that the
  repository no longer ships.

**Not a goal.** Describing the repositories, summarising their results, or ranking them.
