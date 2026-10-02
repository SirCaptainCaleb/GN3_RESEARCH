# Route 6 — Algebraic/Steiner lower constructions and spanning-path obstructions

## Statement

Comprehensive synthesis of the algebraic lower-bound program using Steiner/projective/affine/additive systems, path-sum invariants, carrier reductions, and the major Hamiltonicity fences.

## Body

# Route 6. Algebraic and Steiner lower constructions

## Goal

This route attacks the lower-bound side of the LINP problem. Its objective is to construct finite linear 3-uniform hypergraphs with large edge density and no linear path of length ℓ, then take disjoint unions.

The generic benchmark is already at the one-third scale: for every ℓ≥2 there is a finite P_ℓ-free component T on 2ℓ−1 or 2ℓ vertices satisfying

|E(T)| = ((ℓ−1)/3)|V(T)|.      (1)

Consequently

ex_L(n,P_ℓ) ≥ ((ℓ−1)/3)n − O(ℓ²).      (2)

To improve the leading coefficient beyond one third, one would need components whose density exceeds ℓ/3 while still forbidding a spanning or nearly spanning linear path.

The most natural candidates are Steiner triple systems and algebraically defined partial Steiner systems. The route asks whether a global algebraic invariant can force non-Hamiltonicity without sacrificing Steiner-level density.

## 1. Spanning paths in a Steiner triple system

An STS on 2ℓ+1 vertices has exactly

(2ℓ+1)ℓ/3

blocks. If it contains no spanning ℓ-edge linear path, then disjoint copies immediately give the lower bound

ex_L(n,P_ℓ) ≥ (ℓ/3)n − O(ℓ).      (3)

Thus the basic construction problem is:

**Steiner obstruction problem.** Find infinitely many non-Hamiltonian Steiner triple systems on 2ℓ+1 vertices, or equally dense near-Steiner systems, where Hamiltonian means containing a spanning linear path.

A spanning ℓ-edge path on 2ℓ+1 vertices has ℓ−1 joint vertices, with the remaining ℓ+2 vertices appearing only as private or endpoint vertices. Algebraic systems can therefore be attacked by summing the edge equations along the path and deriving a constraint on the joint set.

This mechanism produces genuine small-dimensional successes.

## 2. Binary projective systems

In the binary projective triple system on the nonzero vectors of F_2^d, the triples are

{x,y,x+y}.

If a spanning linear path exists and J is its set of joint vertices, summing the path-edge equations shows

Σ_{x∈J} x = 0.      (4)

Equivalently, J meets every hyperplane in even cardinality.

For PG(3,2), which has 15 vertices and 35 triples, condition (4) is impossible for the joint set of a spanning 7-edge path. Hence PG(3,2) is P_7-free and gives

ex_L(n,P_7) ≥ (7/3)n − O(1).      (5)

This is a genuine exceptional improvement.

The crucial question is whether the same obstruction scales to higher binary projective dimensions. It does not.

A classification of dense odd induced Boolean Schur systems shows that if the number of missing additive pairs is smaller than the vertex set, then the system is either

1. a full projective system W\{0}, or
2. a two-point deletion W\{0,a,b}

from such a system.

Within this critical family, all sufficiently large full projective systems and all sufficiently large two-point deletions contain spanning paths. The only strict projective improvements surviving the classification occur at the small exceptional lengths corresponding to the Fano plane and PG(3,2).

Thus the projective parity obstruction explains the exceptional construction but does not provide an infinite improved family.

## 3. Affine ternary systems

In the affine system AG(d,3), every triple satisfies

x+y+z=0.

Summing the equations of a spanning path again gives a joint-set condition:

Σ_{x∈J} x = 0.      (6)

For AG(2,3), this rules out a spanning 4-edge path and recovers the familiar affine-plane obstruction.

But the mechanism does not persist. AG(3,3) already contains a spanning 13-edge path. Therefore the low-dimensional affine obstruction cannot simply be iterated by increasing dimension.

The affine branch is consequently closed in its naive form: a scalable construction would need an invariant stronger than the total joint sum.

## 4. Incidence-code certificates

Let M be the vertex-edge incidence matrix over a finite field. If H contains a P_ℓ, then summing the incidence vectors of its ℓ edges produces a codeword whose support is exactly the ℓ+2 private/end vertices, after the joint coordinates cancel in characteristic two. Thus, over F_2,

P_ℓ ⊆ H  ⇒  the binary incidence code contains a word of weight ℓ+2.      (7)

There is an analogous support statement over arbitrary fields.

Hence absence of weight ℓ+2 is a sufficient algebraic certificate for P_ℓ-freeness. This is useful for small constructions, but it cannot beat the one-third scale asymptotically.

Indeed, any linear 3-graph of density greater than ℓ/3 already has a binary incidence-code word of weight ℓ+2. A corresponding ternary theorem gives the same obstruction over F_3. Therefore

“the incidence code omits the path support size”

cannot be the invariant behind an improved infinite family.

Any future code-based construction must use more structure than the absence of one weight.

## 5. Exact low-rank carrier lifts

A different idea is to begin with a good small Boolean example and lift it through a low-rank carrier.

The sharp reduction here is an exact one-bit normal form: any density-beating induced Boolean counterexample contains a non-Hamiltonian subsystem that is an exact one-bit lift of a smaller quotient. Thus the relevant unresolved object is not an arbitrary high-rank additive set but a projective quotient equipped with one binary fiber bit over each point.

However repeated exact carrier lifting does not improve normalized density. A full two-bit lift satisfies, up to the exact lower-order terms,

|V'| = 4|V|+3,
|E'| = 16|E|+6|V|+1,

while the longest-path length grows by a factor four up to an additive constant. Repeated lifting therefore preserves, rather than improves, the edge-density-to-forbidden-length ratio.

So low-rank carriers are useful only if a genuinely new signing obstruction appears at the first nontrivial lift. Blind iteration is fenced.

## 6. Full Steiner systems are asymptotically too Hamiltonian

There is also a broad negative theorem independent of algebra.

Every sufficiently large Steiner triple system contains almost-spanning hypertrees, in particular a linear path using a 1−o(1) fraction of its vertices. Consequently a full STS has normalized density at the first forbidden path length at most

1/3+o(1).      (8)

Thus full Steiner systems cannot beat one third by a positive asymptotic amount.

This theorem does not eliminate near-Steiner systems, because a carefully chosen sparse set of missing blocks might destroy all long paths while retaining almost all density. But several natural deletion mechanisms are also fenced.

## 7. Deletion, doubling, and tensor fences

Suppose an STS on 2ℓ+1 vertices is Hamiltonian and edge-transitive. Any set of blocks meeting every spanning P_ℓ has size at least

(2ℓ+1)/3.      (9)

So a small symmetric deletion cannot turn such a design into a density-improving non-Hamiltonian example.

The order-13 calibration is exact: six blocks must be deleted to destroy all spanning 6-edge paths, and the natural puncture construction is extension-tight. This confirms that the deletion cost is already too large in the first serious test case.

Ordinary STS doubling is also ineffective. The mixed blocks themselves contain paths long enough that the normalized coefficient of the doubled construction cannot exceed one third.

Likewise, the diagonal tensor square of a binary projective system contains a path of length

(2^d−1)(2^{d−1}−1)−1,      (10)

and its density at the corresponding first forbidden length is strictly below one third. Thus projective tensoring does not amplify the PG(3,2) exception.

These are theorem-level no-go statements. The associated construction mechanisms should be regarded as closed unless a new invariant changes the path analysis itself.

## 8. The surviving signed-projective problem

After the preceding reductions, the cleanest algebraic frontier is the exact one-bit signed-projective model.

Take a binary projective quotient with one distinguished point at infinity and a two-element fiber

G_x={(x,0),(x,1)}

over each projective point x. Every projective line {x,y,z} is lifted according to a binary line-signing σ(x,y,z), considered modulo the natural fiber switches.

The all-projective signing is eventually Hamiltonian. The open problem is whether there exists an infinite switching-inequivalent family of signings for which the lifted system remains non-Hamiltonian while retaining essentially Steiner density.

A successful family would yield

ex_L(n,P_ℓ) ≥ (ℓ/3)n − O(ℓ²)

for infinitely many new lengths, and could potentially sharpen the lower-order behavior. More importantly, a denser asymmetric near-Steiner variant could in principle beat one third.

No such infinite obstruction is presently proved.

## 9. What has genuinely been ruled out

The explored landscape can be summarized without reproducing its historical derivations.

The following mechanisms do not provide a scalable improvement beyond the one-third barrier:

- full higher-dimensional binary projective systems;
- naive higher-dimensional affine systems;
- omission of a single incidence-code support weight;
- repeated exact low-rank carrier lifting;
- full large Steiner triple systems;
- ordinary STS doubling;
- sparse symmetric deletion of edge-transitive Hamiltonian designs;
- diagonal binary-projective tensor squares.

These are genuine fences, not merely unsuccessful experiments. A new construction should be checked against them before any detailed development.

## 10. First unsupported implication

The live proof attempt stops at the signed-projective/asymmetric near-Steiner problem.

**Residual construction target.** Produce an infinite family of Steiner-density or near-Steiner-density linear triple systems whose path obstruction is controlled by a global invariant not destroyed by increasing the order, and which is not an instance of any of the fenced mechanisms above.

In the Boolean low-rank lane, the concrete target is:

**Signed-projective target.** Find an infinite family of exact one-bit projective signings for which no spanning linear path exists, or prove that every sufficiently large signing is Hamiltonian.

Either outcome would materially close the current algebraic lane.

## Research handoff

The strongest live starting point is the exact one-bit signed-projective normal form, or a genuinely asymmetric near-Steiner construction outside the full-STS and symmetric-deletion theorems.

Do not retry higher projective dimensions, naive affine dimensions, missing-one-weight incidence codes, repeated exact lifts, ordinary doubling, sparse symmetric deletion, or projective diagonal tensoring without a new invariant that escapes the certified fences.

Status note: the generic lower benchmark, exceptional PG(3,2) construction, Boolean classification, affine and code fences, carrier-lift fence, almost-Hamiltonian STS theorem, deletion/doubling fences, and diagonal tensor no-go are certified. The signed-projective infinite obstruction remains proposal-level.