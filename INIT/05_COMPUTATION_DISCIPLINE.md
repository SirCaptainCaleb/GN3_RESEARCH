# 05 — GN3 computation discipline

This file specializes the conservative-computation rules in `03_RESEARCH_PROTOCOL.md`. It is mandatory startup policy for all GN3 workers. Its purpose is to keep computation subordinate to mathematical search and to prevent solver runs or large tool output from stalling a research wave.

## Default presumption

GN3 is proof-first. MILP, SAT, SMT, exhaustive enumeration, and comparable finite-search tools are auxiliary instruments, not default research modes. Use them when they answer a sharply bounded question more cheaply and cleanly than hand analysis, especially for tiny counterexample searches, sanity checks, finite classifications, or verification of a deliberately small combinatorial claim.

Do not reach for MILP or SAT merely because a statement is finite, because a case split exists, or because encoding it is possible. A mathematically awkward question can become an even less informative solver instance.

## MILP/SAT admission gate

Before launching a MILP or SAT computation, the worker must be able to answer all of the following positively.

1. **The question is exact and finite.** State the precise feasibility, optimization, counterexample, or classification question. The intended mathematical inference from `SAT`, `UNSAT`, feasible, infeasible, or an optimum value must already be clear.
2. **The instance is deliberately small.** There is strong reason to expect the chosen encoding to resolve in one short, clean run. The worker understands the rough scale of the variables, clauses/constraints, symmetry, and search space well enough that the run is not an open-ended experiment.
3. **The output can be compact.** Before running, decide what small answer is needed: normally a status, one objective value, one small witness/counterexample, a short count table, or a compact certificate. If useful interpretation would require reading a huge assignment, solver log, enumeration, trace, or diagnostic dump, do not launch that formulation.
4. **The computation will not monopolize the mathematical task.** If the solver stalls, the research can immediately return to a conceptual route without losing the whole work cycle.

If any of these conditions is doubtful, prefer mathematical analysis, a smaller hand-checkable subproblem, or a more aggressively reduced encoding first.

## Specific caution for MILP

MILP is appropriate for small feasibility or extremal questions with a transparent encoding and a compact optimum or witness. It is a poor default for discovering the structure of a proof.

Prefer feasibility over unnecessary optimization, fixed small parameters over parameter sweeps, strong mathematical preprocessing over feeding the solver a raw combinatorial universe, and symmetry reduction over asking the branch-and-bound search to rediscover obvious equivalences.

Do not repeatedly enlarge a stalled MILP, add layers of auxiliary variables in hopes that the solver will discover the right abstraction, or spend a research cycle tuning formulations whose mathematical meaning is becoming less clear. If the first sensible bounded formulation does not resolve cleanly, step back and extract a smaller mathematical question.

## Specific caution for SAT

SAT is appropriate when the desired conclusion is naturally a small exact consistency question and a satisfying assignment or contradiction can be summarized compactly. It is especially useful for a small local configuration whose variables have an immediate mathematical interpretation.

Do not use SAT as a substitute for understanding a large case tree. Avoid broad all-solution enumeration, repeated blocking-clause loops, large symmetry-unreduced searches, enormous UNSAT cores, or models whose significance depends on inspecting hundreds or thousands of Boolean assignments.

When SAT succeeds, report the mathematical witness or obstruction, not the raw model. When it returns UNSAT, preserve a compact independently checkable reduction or certificate when feasible; otherwise the result remains exploratory evidence rather than a canonical proof dependency.

The same caution applies to SMT, CP-SAT, CSP, and similar general-purpose solvers.

## Output-budget rule

Large tool output is itself a research hazard. It consumes context, obscures the mathematical signal, makes follow-up reasoning brittle, and is a common cause of agent stalls.

Every substantial computation should therefore have an **output budget chosen before execution**. Aim for output that can be inspected directly in a few dozen lines at most, and preferably much less. Suppress progress logs, branch-and-bound traces, solver diagnostics, full variable dumps, giant matrices, exhaustive solution lists, and repeated near-duplicate cases unless one tiny excerpt is specifically needed to diagnose a failure.

Code should aggregate internally and print only the final mathematical summary. If there are many solutions, return counts, canonical representatives, extremal examples, or the small statistic actually needed. If there are many constraints or variables, report counts and the few active mathematical features, not the full generated model.

If a tool begins producing unexpectedly large output, stop. Do not respond by requesting more pages, dumping the remainder into Slack, or running increasingly verbose variants. Redesign the computation so that filtering and compression occur before output reaches the research context.

A useful rule of thumb is: **if the output itself needs substantial summarization before it can be reasoned from, the computation was not yet designed conservatively enough.**

## Stop rules

A solver run is not entitled to consume the rest of a research task merely because an encoding has already been written.

Stop the computational route when any of the following occurs:

- the first sensible bounded instance does not resolve promptly enough to remain an obviously small experiment;
- memory, branch count, clause/constraint count, or solver diagnostics begin growing unexpectedly;
- interpreting the result would require a large raw dump;
- repeated reformulations are changing solver engineering more than mathematical understanding;
- the computation answers examples but no longer has a clear route to a theorem, obstruction, or counterexample relevant to the live target.

After stopping, record only the concise null information that matters—for example, that the proposed bounded check did not resolve cleanly—and return to mathematical search. Do not mistake sunk effort for a reason to keep escalating the solver.

## Team-level concurrency

A research wave should not allow many workers to converge independently on MILP or SAT merely because the same frontier admits an encoding. That creates correlated failure and can stall the whole team at once.

Unless the Director explicitly identifies a finite computational question as the common primary target, **at most one worker should normally pursue a solver-heavy version of a given subproblem at a time**. Other researchers should continue proof-first approaches, structural synthesis, conceptual ascent, direct constructions, or independent mathematical attacks.

A computational worker who obtains a useful compact result should publish the mathematical conclusion quickly so the rest of the team can use it without reproducing the computation. A computational worker whose run stalls should report that compactly and relinquish the route rather than drawing other workers into parallel solver tuning.

## What may survive from computation

The durable mathematical object is the inference, not the transcript. Retain only:

- the exact finite question encoded;
- the mathematical meaning of the variables and constraints when that matters;
- enough scale information to establish that the computation was genuinely bounded;
- the concise output, witness, counterexample, optimum, count, or certificate;
- the precise mathematical conclusion drawn from it;
- reproducible code only when future verification or reuse is genuinely valuable.

Do not canonize raw solver logs, giant models, search traces, or large generated tables. A computation that cannot be compressed into a small checkable mathematical payload may still guide exploration, but it should not become a hidden load-bearing dependency of the proof.

## Strategic principle

Use computation to **collapse uncertainty**, not to manufacture more state for the team to inspect. The best computational intervention should leave the mathematical problem smaller, clearer, and easier to reason about than it was before the tool was called. If the likely effect is the opposite, do not run it.