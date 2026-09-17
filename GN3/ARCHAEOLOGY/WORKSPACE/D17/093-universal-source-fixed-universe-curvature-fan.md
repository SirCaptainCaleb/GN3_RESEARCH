# A bad deletion of one source universe emits local curvature in every good source fiber

**Workspace:** D17
**State:** established
**Key:** `universal-source-fixed-universe-curvature-fan`

**Summary:** Fix a non-Hamiltonian source universe Omega disjoint from a Hamilton complement B. Good deletion labels q with Omega-q Hamiltonian are literal source pivots C_q=P_q|B, while bad deletion labels z have Omega-z non-Hamiltonian and remain the same support obstruction in every such fiber. For every good q, every retained Hamilton word P_q on Omega-q, and every bad z, the in-place replacement z->q fails on the non-Hamiltonian support Omega-z, so one of at most three local turns reverses to a q-labelled tight trimer within distance two of z in P_q. Thus universal-source obstruction is source-invariant and generates a curvature fan over all good deletion fibers, not an isolated one-source event.

### 1. Fixed source universe and good/bad deletion labels

Let H be a hypothetical smallest counterexample and suppose

  V(H)=Omega disjoint_union B,

where B carries a retained Hamilton tight path and Omega is non-Hamiltonian. Define

  G(Omega)={q in Omega : Omega-{q} is Hamiltonian},
  D(Omega)=Omega-G(Omega).

For every q in G(Omega), choose and retain one ACTUAL Hamilton path P_q on Omega-q. Then

  C_q := P_q | B

is a literal exact singleton-deletion source cover of H-q. Thus changing q inside G(Omega) is a genuine source pivot which leaves BOTH the physical universe Omega and the literal complementary support B fixed. No path order is identified across different q.

For z in D(Omega), the support Omega-z is non-Hamiltonian by definition. In the source fiber C_q, z lies on P_q because q is good and z is bad, hence q!=z. The accepted seam-free source substitution mechanism underlying R927 identifies this same support defect with the universal-crossing obstruction in every good source fiber: a crossing-free exact H-z representative relative to (Omega-{q,z})|B would repair to the forbidden Hamilton support Omega-z paired with B. Thus the bad-deletion set D(Omega) is source-invariant across all q in G(Omega).

The curvature statement below actually needs only the support non-Hamiltonicity Omega-z, not the universal-crossing terminology or the repair direction.

### 2. Fiberwise local curvature fan

Fix q in G(Omega), z in D(Omega), and write the retained source word

  P_q=(v_0,v_1,...,v_m),   z=v_i.

Replace the physical occurrence of z by the omitted source label q in exactly the same position:

  P_q[q/z]=(v_0,...,v_{i-1},q,v_{i+1},...,v_m).

This word has vertex set exactly Omega-z. Since z is bad, Omega-z is non-Hamiltonian, so P_q[q/z] cannot be tight. Every consecutive turn not containing q is inherited literally from P_q and is tight. Therefore at least one available member of

  (v_{i-2},v_{i-1},q),
  (v_{i-1},q,v_{i+1}),
  (q,v_{i+1},v_{i+2})

(with the obvious endpoint omissions) is bad. Boundary antisymmetry R3 reverses a bad member to a proper tight trimer containing q and source vertices at P_q-distance at most two from z.

Thus for EVERY pair

  (good source label q, bad deletion label z) in G(Omega) x D(Omega)

and for EVERY retained Hamilton word P_q on Omega-q, there is a graph-intrinsic q-labelled source-local reverse trimer J(q,z;P_q). The carrier dimer and exact failed window are retained; different fibers are not silently synchronized.

Because B is nonempty and z lies outside the resulting trimer, each J(q,z;P_q) is proper in H. Accepted R4 currentizes it as one component of a literal maximum spanning three-forest. Accepted R508 then forces the two boundary-dimer recompletion cuts exactly as in `universal-source-local-substitution-curvature`.

### 3. Source-pivot invariance is the new content

The point is not merely that one universal source crossing produces one trimer. The SAME physical bad deletion z survives every legal source pivot q->q' inside G(Omega), because the predicate is simply Omega-z non-Hamiltonian. Each new source fiber therefore regenerates a local curvature carrier around z in its own actual Hamilton order.

This separates two finite objects attached to one source universe:

  GOOD labels G(Omega): legal fixed-B source fibers,
  BAD labels D(Omega): source-invariant universal defects.

The complete bipartite incidence G(Omega) x D(Omega) is decorated by literal local reverse trimers. In this sense Arm U is naturally a CURVATURE FAN over a fixed non-Hamiltonian universe rather than a sequence of unrelated representative-relative crossings.

There are two extremal regimes. If G(Omega) is large, one bad z appears in many independently current source fibers and should be attacked by synchronizing the resulting q-labelled curvature cells, for example through R435/endpoint-return structure. If D(Omega) is large, one fixed source word contains many source-invariant bad deletion positions, and the appropriate representation is the replacement-barrier profile (accepted R950 when every literal substitution fails). The theorem here does not assert either synchronization or a quantitative threshold.

### 4. Relation to the R927 U/M architecture

Accepted R927 says that global absence of universal source crossing forces the saturated odd uniform branch M. The present fixed-universe theorem sharpens the complementary U side: once one bad deletion is present, it is not tied to the source label that first exposed it. It persists across every good deletion source of that universe and emits fresh local curvature in each such fiber.

Therefore a plausible parent target is no longer transition-count reduction for one H-z cover. It is a CURVATURE-FAN CONSUMER: prove that a nonempty bad-deletion set D(Omega), together with the full family of good source fibers G(Omega), cannot support all of these source-local reverse trimers without either a spanning two-cover, a universal one-extension core, or a nontrivial current R435/maximum-forest curvature cell that strictly descends under the global portal calculus.

No such final consumer is claimed here. In particular the trimers for different q may use different neighboring source vertices, and their maximum-three-forest currentizations need not share complements or representatives. Those are the genuine remaining synchronization difficulties.

Status: complete internal working mathematics, unreviewed. Dependencies are accepted R3, R4, R508, and the seam-free source substitution mechanism in accepted R927; the local curvature fan itself only needs R3 plus the definitions of G(Omega),D(Omega).

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "comparison",
        "revision_id": "R950"
    }
]
```
