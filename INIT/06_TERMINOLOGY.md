# 06 — GN3 terminology registry

This file is the authoritative registry for **project-coined mathematical terminology** in GN3. The structural rules for live message placement, standalone statement form, and repair are in `07_COMMUNICATION_STANDARD.md`.

It applies to all current mathematical communication: Slack research roots and replies, guidance, audit discussion, the research tree, the proof spine, and the toolkit. It does not rewrite historical material under `ARCHAEOLOGY/`.

## Scope

Standard mathematical terminology does not need to appear here. Literal descriptive phrases also do not need registration when their meaning is compositionally clear from ordinary mathematics, for example “the first two vertices of the path”, “an edge crossing the partition”, or “the induced subtournament on these five vertices”.

Local symbols such as `I`, `O`, `M_C(x)`, and `T_s` do not require registration when they are explicitly defined in scope.

A **project-coined term** is a reusable English noun, adjective, or compound label whose mathematical meaning is special to GN3 and is not the ordinary established meaning of the words themselves. Every such term must appear in the approved list below before it is used as established shorthand.

**Default rule: if a project-coined term is not approved here, do not use it. Spell out the mathematics instead.**

A researcher may propose a new term in a Slack thread, but it is not GN3 vocabulary until this file is updated. Approval requires:
1. one intrinsic structural definition;
2. a clear recurring mathematical object or relation that the term names;
3. a reason ordinary standard terminology or a short descriptive phrase is materially worse;
4. a changelog entry notifying already-initialized workers.

## Approved project-defined vocabulary

The following project-specific terms are approved.

- **boundary tournament** — the reversal-complete directed 3-uniform object defined in the canonical proof spine.
- **tight triple**, **tight path**, **tight cycle** — as defined in the canonical proof spine.
- **path cover**, **exact (q)-path cover** — as defined in the canonical proof spine.
- **endpoint transfer** — the operation defined in the longest-path section of the canonical proof spine.
- **source path**, **left-extended path**, **right-extended path**, **oppositely extended pair** — the fixed-pair constructions defined in the canonical proof spine.
- **continuation sequence** and **continuation reduction** — only with the exact definitions in the canonical proof spine. The words do not imply any additional reachability, persistence, or evolution beyond those definitions.
- **matching blocks** and the names `M_low`, `M_mid`, `M_high` — the three ordered opposite-edge matchings in the non-Hamiltonian edge-ordered four-vertex classification.
- **comparison digraph** — only for an explicitly defined directed graph encoding pairwise comparisons, as in the small-order Hamiltonicity machinery.

This list is intentionally short. A useful theorem does not need a nickname.

## Forbidden GN3 shorthand and overloaded metaphors

The words below are **not approved as GN3-specific mathematical labels**. When they have a standard established mathematical meaning, that standard meaning remains allowed; what is forbidden is repurposing them as project shorthand.

- **core**, **four-core**, **endpoint core**, **three-vertex core** — do not use for a merely distinguished vertex set or induced subtournament. Say “four-vertex complement”, “the induced subtournament on …”, “the eight-vertex set …”, or the exact set.
- **fan** — do not use for a family of triples, paths, or endpoint relations. “Fan graph” is allowed only when the standard graph is actually meant.
- **fiber** — do not use for a family of covers or configurations on a common residue. “Fiber” is allowed only as the inverse image of a specified map or in another standard mathematical sense.
- **splice**, **splicing** — state the actual operation: concatenate paths, cut specified edges, join specified endpoints, reconnect specified subpaths, or replace specified blocks.
- **turn** — do not use as a name for a tight triple or local orientation pattern. State the triple.
- **signature** — do not use for a finite local pattern or tuple of conditions. Name the actual set, tuple, map, or orientation data. Standard uses such as the signature of a quadratic form are unaffected.
- **profile** — do not use as shorthand for endpoint orientation data. State which matching edge is incoming or outgoing at each endpoint.
- **seam** — say “joining triple”, “attachment triple”, or name the displayed ordered triple.
- **rail** — say “path”, “path component”, or “subpath”.
- **gate** — state the exact local condition or ordered triple.
- **packet** — say “set”, “family”, “tuple”, or list the conditions.
- **carrier** — name the path, edge, component, or vertex set actually meant.
- **cell** — do not use for a case or configuration. Standard topological/cellular uses are unaffected.
- **bridge** — do not use for a tight four-vertex path or generic attachment configuration. The standard graph-theoretic meaning of bridge/cut-edge is allowed.
- **face** — do not use merely for a vertex-deleted subset of a finite set. Say “five-subset”, “four-subset”, or “the set obtained by deleting (v)”. Standard simplicial/polyhedral uses are unaffected.
- **quiet gap** and similar discovery-time labels — state the exact failed or tight triples.
- **surgery** — may remain in a legacy filename, but is not a mathematical operation name. In statements and proofs, describe the cuts, joins, concatenations, or replacements explicitly.

## Enforcement

This registry overrides legacy Slack vocabulary and archaeology terminology. Finding a word in `SEARCH_CORPUS.md`, an old R-result, or an archaeology file does not authorize it.

When a forbidden or unregistered project term appears in current mathematical communication:
- rewrite it into explicit standard mathematical language;
- preserve the exact mathematical content;
- do not invent a replacement nickname merely to avoid the old one.

Auditors check terminology compliance together with correctness. Directors and Vice Directors should clean terminology during synthesis rather than allowing research shorthand to harden into the proof.

If there is doubt about whether a phrase is standard or project-coined, prefer the explicit mathematical description and raise the terminology question separately.
