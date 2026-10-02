# Route 1 — Snake/contact-defect and post-43/48 stability

## Statement

Comprehensive synthesis of the direct snake/contact-accounting route from the rank-sensitive 43/48 theorem through near-extremal switching, paid strict-gap structure, and the current global-reuse closure gap.

## Body

# Route 1. Snake/contact-defect stability beyond the 43/48 bound

## Goal and status

Let H be a finite linear 3-uniform hypergraph. For a vertex v, let φ(v) be the maximum length of a linear path whose last vertex is v; for an edge e, let φ(e) be the maximum length of a linear path whose last edge is e. An edge e is special if every vertex of e can occur as the last vertex of a longest path ending in e. Otherwise e has a unique entrance x; it is ascending when φ(x)=φ(e)−1. The other two vertices are terminals of e.

This route starts from the certified rank-sensitive 43/48 inequality and asks whether equality can persist. The current mathematics reduces a near-extremal counterexample to a large family of clean, strict-rank-gap, cycle-certified payment objects. The first genuinely unsupported step is global: the same higher-rank path, blocker, switcher triangle, or superlevel output may be reused by many different centers. No local case analysis presently rules out that reuse.

The theorem sought by this route is therefore a bounded-reuse theorem strong enough to turn the already-forced linear mass of local certificates into a positive global defect.

## 1. Exact contact identity

For each nonisolated vertex v, put p_v=φ(v). Let T(v) be the family of ascending nonspecial edges terminal at v, let t(v)=|T(v)|, and, when T(v) is nonempty, let q(v)=max{φ(e): e∈T(v)}. For p≥7 define

β(p)=⌊(11p−16)/8⌋,

with β(1),…,β(6)=0,1,2,2,3,5.

Choose for every v a maximum p_v-edge path P_v, aligned with a rank-p_v ascending terminal edge whenever one exists. For an edge incident with v, record how many off-v vertices it has on the precursor of P_v. Let D_v be the excess coming from double contacts, and set

η_v = β(p_v) − t(v) + D_v.

The fixed-entrance and central-window estimates imply η_v≥0. More precisely, if q(v)=p_v then

t(v)−D_v ≤ ⌈(3p_v−4)/4⌉,

whereas if q(v)<p_v then

t(v) ≤ γ(q(v)),  γ(q)=⌊(11q−5)/8⌋ for q≥4,

and the central window also gives t(v)−D_v ≤ max(0,2p_v−7). Combining the cases yields t(v)−D_v≤β(p_v).

Let A be the number of ascending edges, C the number of clean ascending-source incidences in the chosen path system, D=Σ_v D_v, η=Σ_v η_v, and Q≥0 the total unused contact capacity on the paths P_v. The exact contact count is

3m − C + D = 2Σ_v p_v − n_+ − Q,

where n_+ is the number of nonisolated vertices. Since every ascending edge has two terminals, Σ_v t(v)=2A, and therefore

Σ_v β(p_v)=2A−D+η.

Substitution gives the exact identity

6m = Σ_v(4p_v−2+β(p_v)) − D − η − 2(A−C) − 2Q.      (1)

Every term subtracted on the right is nonnegative.

If H is P_ℓ-free, then p_v≤ℓ−1. Since 4p−2+β(p) is increasing,

m ≤ ((43ℓ−75−ρ_ℓ)/48)n ≤ ((43ℓ−75)/48)n      for ℓ≥8,

where ρ_ℓ is the residue produced by the floor in β. This is the certified starting theorem for the route.

## 2. What near equality forces

Write S=Σ_v p_v. Along a sequence with m=(43/48−o(1))S and S/n_+→∞, identity (1) forces

D + η + 2(A−C) + 2Q = o(S).      (2)

Thus almost all endpoint-rank mass lies at vertices where η_v is small.

For p=p_v≥8, the aligned case q(v)=p is expensive:

η_v ≥ β(p)−⌈(3p−4)/4⌉ ≥ (5p−24)/8.

Hence a near-extremal high-rank vertex cannot usually be aligned. In the misaligned case,

η_v ≥ β(p)−γ(q(v)).

Because β(p)=γ(p−1), exact zero deficit forces

q(v)=p−1,   t(v)=γ(p−1)=β(p),   D_v=0.

Thus the unique dangerous shell is the gap-one shell.

Fix p=q+1, a rank-q ascending terminal anchor, a maximum rank-q anchor path Q, and the chosen maximum p-path P_v. Let

δ_v = γ(q) − (t(v)−X_v^T)

be the gap-one switching slack, where X_v^T is the excess contact multiplicity of T(v) on P_v. Since X_v^T≤D_v, δ_v≤η_v. The gap-one switching theorem then gives at least

⌊5q/8⌋ − δ_v

members of T(v) that are double on Q but single on P_v. Their two off-v vertices form a matching crossing the cut between anchor vertices retained by P_v and anchor vertices omitted by P_v. Hence small η_v forces a switching matching of size (5/8−o(1))q, and its retained endpoints give the same order of balanced endpoint lenses.

Thus near equality is not merely a density statement: it manufactures a large, organized switching geometry at almost every high-rank center.

## 3. Paid strict-gap extraction

The switching geometry can be sharpened. After discarding o(S) center-edge incidences, one obtains for almost every relevant center v a family G_v with

|G_v| ≥ p_v/8 − o(p_v)

such that every e={x,v,u}∈G_v satisfies all of the following:

1. x is the unique entrance and e is source-clean on the chosen maximum path at x;
2. e is terminal-single on the chosen maximum paths at both terminals v and u;
3. e has strict rank gap at both terminals: φ(e)<min{φ(v),φ(u)};
4. e carries the common-anchor payment certificate produced by the switching argument.

There is already a certified theorem-closing criterion at this point: if these selected certificates can be assigned so that a rank-p vertex is used by only g(p)=o(p) centers, then no 43/48-near-extremal sequence exists. Thus the local extraction is strong enough; the missing issue is congestion.

## 4. Fundamental-cycle normalization

Form the terminal-pair graph J whose edges are the terminal pairs of the source-clean, doubly-terminal-single ascending edges. Give each terminal-pair edge the rank of its hyperedge. In every component choose a spanning tree of maximum total rank, and let F be the resulting forest.

Because F has fewer than n_+ edges while S/n_+→∞, deleting paid incidences whose terminal pair belongs to F costs only o(S). We retain subfamilies H_v⊆G_v satisfying

Σ_v (p_v/8 − |H_v|)_+ = o(S).      (3)

For e∈H_v, the terminal pair of e is a nonforest edge. Let C_e be its fundamental cycle. If a tree edge f on C_e had smaller rank than e, replacing f by e would increase the total tree rank, contradicting maximality. Hence e is a minimum-rank edge on C_e.

Let f be either cycle-neighbor of e and let w be their common terminal. Since φ(f)≥φ(e), a maximum path witnessing w as a terminal of f cannot meet e only at w; otherwise appending e would force φ(e)>φ(f). Therefore e has an additional blocker contact with each of the two neighboring terminal witnesses.

Consequently almost all of the local p_v/8 paid mass may simultaneously be required to be source-clean, terminal-single at both ends, strict-gap at both ends, a minimum-rank nonforest chord, and equipped with canonical blocker contacts on both sides.

## 5. Three enriched currencies

A further theorem, proved but still pending independent audit, compresses the remaining local alternatives. After discarding centers carrying only o(S) total rank, every relevant center v has a selected family H_v as above and at least one of the following occurs:

- U: at least (1/16−o(1))p_v members of H_v are terminal-retained on the host path;
- T: at least (1/128−o(1))p_v distinct early doubly occupied certificate cells occur, hence that many switcher triangles;
- Z: at least (1/128−o(1))p_v distinct early paid cells have distinct standard output edges lying in the superlevel V_{≥p_v}={w:φ(w)≥p_v}.

Partitioning centers according to a witnessing case shows that at least one of U,T,Z has total center-indexed mass Ω(S); using the weakest displayed coefficient gives at least (1/384−o(1))S.

The fundamental-cycle certificate survives in every branch. Optimistically, the near-extremal proof has therefore reached a theorem-wide trichotomy: one of three globally meaningful currencies has linear mass, and every unit of that mass carries strict rank gap plus a cycle/blocker certificate.

This trichotomy is not yet certified, so a final proof would have to audit it before using it as a theorem.

## 6. Local hostile configurations already normalized

Several proved-but-pending-audit results show that further local case splitting is unlikely to be the missing ingredient.

Near-saturated gap-one vertices already force a (5/8)q−O(1) switching matching across every anchor/maximum-path cut. Lens-free near-top source rails retain a linear family of whole distinguished chords and have overlap at least (5/4−o(1))q, while stronger pairs have (16/11−o(1))q common vertices. Reciprocal unique source-rail contacts force balanced terminal lenses in the remaining one-low configuration. At the odd central boundary p=2q−3, two low-rank members force a double contact, and the sole all-single one-low state has a rigid terminal-only pattern. Rigid zero-slack states expose either the target/return cut needed for a fixed-target exchange or a common half-neighborhood with parity-forced transverse connectors. The small rank-five 4455 branches collapse to explicit rail forms, Class-III blocker defects reduce to one or two alternating chains, lens-free flat terminal cycles have late aligned joints and no 5-cycle, and good-residue two-hole witnesses produce four large edge-disjoint blocker matchings.

The common message is that the surviving local configurations already expose shared global resources. None of these local theorems bounds how many centers may reuse those resources.

## 7. Known dead ends

Several natural continuations have already failed. Cumulative fixed-entrance bounds do not imply that a positive proportion of paid mass has uniformly lower rank. Clean strict-gap edges need not satisfy naive four-edge spacing, even inside favorable-looking double cells; the common-anchor switching data are essential. A switcher triangle belonging to a double cell cannot be charged independently to every occupant. Most importantly, center-indexed certificates are not globally distinct objects: counting them as distinct is precisely the unresolved congestion error.

These failures do not kill the route. They identify the level at which a new theorem is required.

## 8. First unsupported implication

The attempted proof stops at the following statement.

**Residual bounded-reuse target.** In a 43/48-near-extremal sequence normalized as above, suppose one of U,T,Z has Ω(S) center-indexed mass and every selected edge carries strict two-terminal rank gap and its clean minimum-rank fundamental-cycle certificate. Prove that this much center-indexed mass cannot be supported with unbounded multiplicity by o(S) global resources unless one of the defect terms D, η, A−C, or Q in (1) is itself Ω(S).

Any inequality of this form contradicts (2) and therefore yields a strict improvement below 43/48. The older sufficient condition g(p)=o(p) for the selected strict-gap certificates is a certified special case of the same desired phenomenon.

There is presently no justified implication from the enriched local trichotomy to this global bounded-reuse conclusion. The proof must stop here.

## Research handoff

The strongest next target is a global charging theorem for one of U,T,Z, preferably using the surviving fundamental-cycle certificate to control how many centers can share one witness, blocker, triangle, or superlevel output. A successful theorem need only force a positive proportional defect; it need not solve the full two-thirds or one-third problem.

Do not return to local coefficient polishing or another finite normal-form split without a genuinely new global invariant. The local equality theory is already highly constrained; the unresolved mathematics is cross-center reuse.

Status note: the exact 43/48 identity and the strict-gap/fundamental-cycle extraction are certified. The three-currency compression and several local normal-form theorems summarized above are proved but pending audit and are included because they determine the current frontier.