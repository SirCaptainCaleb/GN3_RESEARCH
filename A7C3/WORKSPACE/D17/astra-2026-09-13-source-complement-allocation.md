# Astra: choose the source pair against the physical zipper
Date: 2026-09-13
Status: provisional Director development and strategic fence; not an audited reusable result.

This note integrates D17.368/398, the exact matching switch of D17.421, and the live D17.433-439 wave. It does not settle O4 or O6 and does not advance the chronological audit frontier.

## 1. What the current contractions actually buy

The sharp cell has G=H-{A,C}=B disjoint-union X, X={v,p,q,r}, three historical tight turns (A,s,C), and an actual old source two-cover F. The selected spokes are internal in F. J is a literal three-forest with tau(J)=1; F has tau(F)=3 in the sharp cell.

The matching staircase and its physical realization are separate. D17.421 identifies the first numerical loss. D17.416 forces blockers to contact the remaining suffix. Neither statement alone says there is a physical strict-descent closure before the loss. D17.424/R1028 concerns consecutive successful physical pivots; it cannot be applied as if all intermediate prefixes were successful.

The new ancestry wave gives substantially better placement information, provisionally: a source-marked first-loss corner, or a v-rooted cliff followed by a terminal X-mated source gate. This is not yet a physical synchronization theorem. D17.439 gives a useful sufficient construction after spending the terminal source-mate pair, but neither full-H closure nor every Hamilton recompletion is equivalent to preserving those three residual F intervals as indivisible paths.

## 2. Three complementary supports, rather than one preselected source pair

For any distinct source spokes u,w, test (u,A,w). If tight, (u,A,w,C) is tight using (A,w,C). Otherwise R3 gives (w,A,u), and (w,A,u,C) is tight using (A,u,C). All four vertices are distinct.

Thus Q_{u,w} is a Hamilton P4 on {A,C,u,w}, independently of the position of u,w in F. This is the elementary mechanism already available in D17.368 and D17.398.

For each surviving spoke s in {p,q,r}, let {u,w}={p,q,r}-{s} and define

    C_s = H[B union {v,s}].

A Hamilton path P_s in C_s and Q_{u,w} partition V(H), so P_s | Q_{u,w} is a spanning two-cover. Therefore in a counterexample ALL THREE C_s must be nonHamiltonian simultaneously.

This is an exact sufficient closure interface and its contrapositive. It is not an equivalence between the global theorem and this restricted form of two-cover. Nor does minimality alone force one C_s to be Hamiltonian: it only supplies at most two paths there.

The main strategic gain is choice. The source pair need not be fixed at the terminal gate. The support left over is always one already known spectator path B plus two vertices, v and s. D17.439 represents one such support by three residual old-F intervals. Both representations should be retained; the B representation permits recompletion without preserving those intervals.

## 3. A v-rooted first-loss rectangle fits entirely into one complementary support

Work at an upward switch of D17.421 where BOTH consecutive closing edges are defined. Write its old pair as

    f_i=a_i->b_i,  g_{i-1}=a_{i-1}->b_m,

and its new pair as

    e_i=a_{i-1}->b_i,  g_i=a_i->b_m.

The old pair has one X-X edge and one B-B edge; the new pair consists of two X|B edges. The two OUT labels differ, as do the two IN labels. The same-side edges are nonloops by the stated hypotheses. Consequently these are four distinct physical vertices: exactly two in X and two in B.

If e_i is incident with v, the X-X edge has endpoints v and some other X vertex s. Since v is the only non-spoke of X, s is a source spoke. Denote the B vertices by b,c. The rectangle's entire physical support is then

    {v,s,b,c} subset B union {v,s}.

Spend the OTHER two source spokes u,w on Q_{u,w}. Every zipper vertex survives in C_s. This avoids spending an active zipper corner merely because a different source pair was selected at the terminal boundary.

This support-allocation observation uses only the displayed nonloop switch, the partition X={v,p,q,r}, and the source turns. It does not require D17.435-438 or successful transport to a terminal wall. It does not prove that the two cross edges join the required path components or have tight surrounding turns.

The same allocation works for any source-rooted rectangle whose X-X edge contains v. A rectangle whose X-X edge contains two source spokes is a genuinely different allocation cell: spending two of the three spokes cannot leave both those source corners in a support B union {v,s}. Preserve that case; do not relabel it into the v-containing cell.

This gives a useful organizing distinction independent of which installed transition is called the root:

- X-X diagonal contains v: preserve the whole rectangle by spending the other two spokes.
- X-X diagonal contains two spokes: use a different source allocation/exchange argument, or physical old-source descent.

A singleton-loop interruption is outside this four-distinct-vertex argument.

## 4. Common selected transitions must remain a third ledger location

D17.437's conclusion w(D)=0 for every neutral component follows from nonpositive individual weights and total W0=0. Its stronger 2F/0J placement assertion requires an additional check: an old source gate can lie in F intersect J, outside the symmetric difference altogether. D17.409 explicitly retains the common-transition possibility.

Here is an exact matching-level fixture showing why the numerical hypotheses alone do not exclude it. Take X={v,p,q,r} and four B vertices b1,b2,b3,b4. Set

    F=(b2,p,q,r,b3,b4) | (v,b1),
    J=(p) | (b2,b1) | (v,q,r,b3,b4).

Then F has six selected edges, J has five, tau(F)=3 and tau(J)=1. All source spokes are internal in F, its source block is (p,q,r), and the omitted source p is a singleton in J. The common edges are

    q->r, r->b3, b3->b4.

The unique symmetric-difference component is the F-heavy alternating path

    e1=p->q, f1=v->q, e2=v->b1, f2=b2->b1, e3=b2->p.

There are NO neutral components. Its crossing ledger is 2F/0J, weight two; S1=0 and S2=1. The first positive installed transition is the v-transition. The other augmenter transition is the terminal source gate b2->p, while the omitted source gate r->b3 is COMMON and is exactly the unique J-transition.

The displayed F and J turns impose no pair of contradictory R3 reversals. They can coexist with a transitive matching-height X: assign the matchings {vp,qr} highest, {vq,pr} middle, and {vr,pq} lowest, which certifies both p,q,r and v,q,r. This fixture is NOT asserted to realize every canonical endpoint-cut/gate hypothesis, nor a smallest counterexample, nor a global counterexample. It refutes only the inference from these sharp matching counts and source-block data to compulsory neutral-component placement.

The safe exhaustive ledger in the 2F/0J cell is:

1. COMMON GATE: the remaining F-transition and the unique J-transition are the same common edge; every neutral component is transition-free.
2. NEUTRAL GATE: the remaining F-transition is not common; then it and the unique J-transition lie on one zero-weight neutral component, and every other neutral component is transition-free.

In the 3F/1J cell all transitions lie on the augmenter, so no common or neutral transition remains.

If the full canonical-cut construction excludes case 1, prove that exclusion explicitly from the actual word. Until then, do not rely on the stronger placement assertion. This is a provisional Director fence, not an out-of-order audit verdict on D17.437. The forward source-gate argument of D17.436 uses augmenter counts and survives this particular common-edge concern; the later terminal-boundary construction still has its own physical-realization qualifications.

## 5. What counts as a seam

For disjoint directed tight paths U and V, a join from the last vertex u of U to the first vertex v of V can require two new turns:

    (u_prev,u,v), if |U|>=2;
    (u,v,v_next), if |V|>=2.

Two adjacency joins of three nonsingleton paths can therefore require FOUR new tight turns. If the middle path is a singleton z, also include the turn (last(U),z,first(W)) spanning both joins. One must evaluate the final concatenated word; multiplying a per-join rule that treats the singleton in isolation misses that turn.

Thus 'two joins' in D17.439 is a component count, not a two-turn budget. Reversing a dimer creates no internal triple; reversing a longer tight path is not free under R3. Use an independently certified order if a residual path is to be reversed.

## 6. Ambitious targets and failure criteria

Primary target: under the full retained live source-frame hypotheses, force either a literal Hamilton path in at least one C_s, another explicit spanning two-cover of H, or a physical exact two-cover T of G with strict old-source transition improvement and an identified valid global consumer.

For the v-containing zipper cell, try C_s selected by its two X corners FIRST. This is a moonshot candidate, not a theorem asserting that this particular C_s must be Hamiltonian. Preserve the other two choices if the first is obstructed.

When Hamilton absorption fails, the useful output is a coupled constraint on the three actual complementary supports, not another isolated P4 or collision. Search for a complementary-pair exchange: an obstruction to one allocation enables another allocation or a physical descent. Keep all choices inside one H, one old F, one B order, and the actual source turns.

Use R887's comparison orientation to express each proposed join as the two neighboring edge comparisons. A quotient of B is legitimate only with an exact expansion preserving those comparisons and vertex simplicity. D5 does not authorize arbitrary edge-order assumptions or free reversal of path ports.

The campaign has advanced if a branch is physically closed, a full-data countermodel kills a proposed stronger interface, or a parent theorem genuinely replaces corridor machinery. More ancestry adjectives or a smaller numerical skeleton alone do not meet that standard.
