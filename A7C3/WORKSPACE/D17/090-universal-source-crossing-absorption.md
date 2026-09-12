# Universal source crossing: transition-one exchange and source pivot

**Workspace:** D17
**State:** working
**Key:** `universal-source-crossing-absorption`

**Summary:** Fixes the source, develops crossing counts and transition-one representatives, boundary singletonization, the common-complement swap square and endpoint shields, source-pivot currentization, source-universe deletion interpretation, and the exchange-or-transfer alternating-cycle mechanism.


### 1. Fixed source and the two crossing counts

Let H be a hypothetical smallest counterexample and retain one literal singleton-deletion source

  C_x = A | B

of H-x, where A and B are the actual Hamilton rail orders. Fix z in A and assume the universal physical source-crossing obstruction:

  every exact two-nonempty-path cover of H-z selects an adjacency with one endpoint in A-{z} and the other in B.

Put

  S=A-{z},   C=B union {x},   D={z}.

The original Hamilton order A is a tight path on D union S. Therefore accepted R508 applies to this exact absorber and gives, for every exact H-z two-cover T,

  tau(T) := number of selected T-adjacencies crossing S|C >= 1.

Write

  delta(T) := number of selected T-adjacencies crossing S|B.

The universal source-crossing hypothesis is exactly delta(T)>=1 for every T. Since x is the only point of C outside B,

  tau(T)=delta(T)+e_T(S,{x}),

where e_T(S,{x}) is 0,1,or 2. Thus the R508 transition obstruction is automatic from the source path A; the new content of universal source crossing is that the mandatory transition can never be paid entirely through the exchanged label x.

Both S union {x}=A-{z}+x and A union {x} are non-Hamiltonian. A Hamilton path on S union {x}, together with the untouched source rail B, would be an exact H-z cover with delta=0. A Hamilton path on A union {x}, together with B, would two-cover H.

### 2. Exact form of a transition-one representative

Assume there exists an exact H-z cover T with tau(T)=1; equivalently the minimum of tau is one. Accepted R511 applies to the R508 packet (D,S,A,T). It gives exactly one maximal S-block U containing all of S, exactly two maximal C-blocks, and, after reversing the displayed rail names if necessary, one of the literal forms

  U - V   |   K

or

  V - U   |   K,

where V and K are the two nonempty C-blocks and the displayed U|V junction is the unique S|C selected transition.

Because delta(T)>=1 while tau(T)=1, the C-side endpoint of this unique transition is a physical vertex b in B, not x. Hence U is an actual Hamilton path on S and the unique direct A-z|B crossing is the selected transition from/to b. In the first orientation b is the first vertex of V and the contiguous subpath U-b is tight; in the second b is the last vertex of V and b-U is tight. In particular delta(T)=1.

This is stronger than the generic R511 normal form only because the universal source-crossing hypothesis identifies the C-side transition endpoint as a B-vertex.

### 3. Boundary-vertex dichotomy and seam-free singletonization

Keep the transition-one cover and its boundary vertex b in B. There is an exact dichotomy.

If b is Q-universally crossing relative to the same source C_x=A|B, retain that as a second universal source crossing, now on the B side.

Otherwise the dual seam-free deleted-label substitution from `extremal-root-compression` supplies an exact H-b cover with support partition

  A | (B-{b}+x).

Let J be the actual Hamilton rail on B-{b}+x in that cover. This statement also covers the incident/compatible case, where the required support partition already exists.

Now discard every vertex of the mixed C-block V beyond its boundary b and replace the whole C-side remainder by J. No new junction is introduced. In the U-V orientation, P=U-b is a contiguous subpath of T; in the V-U orientation, P=b-U is a contiguous subpath of T. Therefore

  C_b^* : A | J                    on H-b,
  C_z^* : P | J                    on H-z

are both literal exact two-covers, with

  V(P)=A-{z}+b,
  V(J)=B-{b}+x.

The second cover still has exactly one S|C transition and exactly one A-z|B transition, but its mixed C-block is now the singleton b. The exchanged label x lies on the pure common rail J, at its actual position in the chosen H-b cover.

Thus every transition-one universal crossing has the following cover-valued outcome:

  opposite-side universal crossing at b,
  OR a common-complement swap square with one singleton boundary exchange.

This is an exact cover repair, not a scalar descent assertion.

### 4. The common-complement swap square

In the repair branch put

  X=A union {b},   Y=B union {x}.

Then X intersect Y={b}, X union Y=V(H), and the three retained singleton fibers are

  H-x : (X-{b}) | (Y-{x}) = A | B,
  H-b : (X-{b}) | (Y-{b}) = A | J,
  H-z : (X-{z}) | (Y-{b}) = P | J,

where b is an actual endpoint of P. Deleting that endpoint from the last cover gives the literal pair-deletion cover

  H-{b,z} : U | J.

No trimming across an internal vertex is used here.

The two overlap blocks X and Y are both non-Hamiltonian. If X had a Hamilton path, it would be disjoint from J=Y-{b} and those two paths would span H. If Y had a Hamilton path, it would be disjoint from A=X-{b} and those two paths would span H. On the other hand the following four vertex-deletion Hamilton paths are certified with their actual orders:

  X-{b}=A,
  X-{z}=P,
  Y-{x}=B,
  Y-{b}=J.

Thus the transition-one repair produces two non-Hamiltonian overlapping replacement blocks, but with only two certified deleted vertices on each side. Bare deletion-Hamiltonian-block reasoning is therefore not being invoked.

Retain the literal positions

  z=a_i in the original order A=(a_0,...,a_r),
  b=b_j in the original order B=(b_0,...,b_s),
  x=j_l in the repaired order J=(j_0,...,j_t),

as well as whether P is U-b or b-U. None of these orders is identified or silently reversed.

### 5. Exact endpoint shields forced by the common complement

The common rail J yields graph-intrinsic order data involving the two missing labels b and z. Since A|J is an exact cover of H-b, attaching b to either end of J would close H together with A. Therefore

  (b,j_0,j_1) is bad,        (j_{t-1},j_t,b) is bad,

and boundary antisymmetry gives

  (j_1,j_0,b) tight,         (b,j_t,j_{t-1}) tight.

Likewise P|J is an exact cover of H-z, so endpoint attachment of z to J is impossible and

  (j_1,j_0,z) tight,         (z,j_t,j_{t-1}) tight.

Here |J|=|B|>=2, so the terminal dimers exist. Hence the reverse left terminal dimer (j_1,j_0) carries two same-polarity witnesses b,z, and the reverse right terminal dimer (j_t,j_{t-1}) carries the same witness pair with the opposite endpoint polarity. This is a literal two-ended collision-saturation certificate on one fixed Hamilton complement. It does not by itself close H and is recorded only as order-valued input for the remaining augmentation step.

### 6. Exact remaining obstruction

The universal source-crossing branch is not closed by the preceding normalization. Two logically separate gaps remain.

First, the universal hypothesis only forces delta(T)>=1. It is not yet proved that some exact H-z cover has tau(T)=1, or even that a cover minimizing delta can be repaired until all extra S-x transitions disappear. The cases min tau>=2 therefore remain.

Second, in the tau=1 branch the boundary b may itself be universally crossing from the opposite source rail. If it is not, the common-complement swap square is proved, but no theorem yet consumes the simultaneous data

  A|B,  A|J,  P|J,

with P=A-z+b ending at b and J=B-b+x, into a spanning two-cover. A useful parent target is a common-complement one-vertex exchange theorem which uses the actual orders A,B,P,J, the positions of z,b,x, and the two-ended {b,z} shields on J to either Hamiltonize X or Y, or construct a new exact H-z cover with strictly improved physical transition data. Generic payment, a standalone P4, a standalone R435 order-change output, or an unverified potential decrease would not settle this residue.

Status: Sections 1-5 are complete internal mathematics conditional only on the stated transition-one representative and the already established seam-free substitution/R508/R511 interfaces. They are working development mathematics, not a canonically reviewed standalone conclusion. The full universal source-crossing absorption theorem remains open at the two gaps in this section.


### 7. Source-pivot currentization gives an induced compatibility path

The common-complement repair has an exact compatibility interpretation which is stronger than merely having two neighboring singleton fibers. Keep

  C_x : A | B,
  C_b : A | J,
  C_z : P | J,

with V(P)=A-{z}+{b}, V(J)=B-{b}+{x}, and b an endpoint of P.

First, x and b are compatible. On the common residue H-{x,b}, the restrictions are

  C_x : A | (B-{b}),
  C_b : A | (J-{x}) = A | (B-{b}).

Second, b and z are compatible. On H-{b,z}, deleting the endpoint b from P leaves the literal Hamilton path U on A-{z}, so

  C_b : (A-{z}) | J,
  C_z : (P-{b}) | J = (A-{z}) | J.

Third, x and z are not compatible. On H-{x,z}, C_x restricts to

  (A-{z}) | B,

whereas C_z restricts to

  (A-{z}+{b}) | (B-{b}).

Both A-{z} and B-{b} are nonempty, because every singleton-deletion rail in a counterexample has order at least two. Thus the two restrictions disagree on the placement of b. Hence the three selected fibers induce the compatibility path

  x -- b -- z

with xz absent.

Equivalently, relative to the NEW source C_b=A|J, the old offending vertex z is quiet: the retained exact H-z cover P|J has no selected adjacency between A-{z} and J. Its only boundary exchange from A-{z} is to b, and b is not a vertex of J. So the transition-one repair does not merely relocate a universal crossing certificate; it currentizes z into a source for which the specific obstruction has disappeared.

In the rail-incidence root this has a literal distance-two form. Let the root edge x have endpoints P_0,Q with universes

  Omega_{P_0}=A union {x},   Omega_Q=B union {x}.

After the b-rebuild and z-currentization, the three physical edges x,b,z form a root path

  P_0 --x-- Q --b-- R --z-- S,

with

  Omega_R=A union {b},
  Omega_S=(B-{b}) union {x,z}.

Thus an obstructed same-side vertex z which could not be attached directly to the P_0 port has, in the transition-one repair branch, been attached to the port R at root distance two from P_0, through the physical boundary vertex b. No path-order transport is hidden in this statement: every root incidence above comes from the three displayed literal exact covers.

This suggests a source-pivot strategy: repeatedly replace a universally blocked direct port move by a verified distance-two currentization. What is NOT yet proved is that such pivots admit a monotone global objective, that every pivot source again has a transition-one representative, or that a finite pivot cycle closes H. Those are the exact requirements for turning this local currentization into a parent absorption theorem.


### 8. Universal crossing is exactly a bad deletion of a source universe

The universal quantifier has an exact support-level reformulation. For a general source label p, write an actual source cover as

  C_p = A | B

of H-p and define its two overlapping source universes

  Omega=A union {p},   Lambda=B union {p}.

Both Omega and Lambda are non-Hamiltonian. If Omega were Hamiltonian, a Hamilton path on Omega together with the source rail B would two-cover H; the argument for Lambda is dual. The source label p is nevertheless a Hamilton deletion of both universes, since Omega-{p}=A and Lambda-{p}=B are Hamiltonian.

Fix z in A. Then

  z is universally crossing relative to C_p

if and only if

  Omega-{z}=A-{z}+{p} is non-Hamiltonian.

Indeed, if Omega-{z} is Hamiltonian, that Hamilton path together with B is an exact H-z two-cover with no selected A-{z}|B adjacency, so z is not universal. Conversely, if z is not universal, choose a zero-crossing exact H-z cover. The seam-free deleted-label substitution proved in `extremal-root-compression` produces an exact replacement cover

  (Omega-{z}) | B,

so Omega-{z} is Hamiltonian. The same equivalence holds dually for vertices of B and deletions of Lambda.

Thus universal source crossing is not an additional mysterious orientation predicate once the seam-free substitution is available: it is exactly failure of one vertex deletion to Hamiltonize one of the two non-Hamiltonian source universes.

This gives a useful fixed-universe parametrization. Put

  G(Lambda)={ q in Lambda : Lambda-{q} is Hamiltonian }.

For every q in G(Lambda), the fixed physical set A=V(H)-Lambda and a chosen Hamilton path on Lambda-{q} give an actual source cover

  C_q = A | (Lambda-{q})

of H-q. For z in A, the preceding equivalence becomes

  z is quiet relative to C_q
    iff A-{z}+{q} is Hamiltonian,

  z is universal relative to C_q
    iff A-{z}+{q} is non-Hamiltonian.

Hence one may encode the whole family by the Hamilton-extension matrix

  M(z,q)=1  iff  A-{z}+{q} is Hamiltonian,

with rows z in A and columns q in G(Lambda). Every entry M(z,q)=1 is cover-valued: together with the fixed Hamilton complement Lambda-{q}, it is an exact H-z two-cover. The old universal obstruction is precisely a zero entry of this matrix.

### 9. Transition-one is an exchange-or-transfer step; persistent failure yields an alternating cycle

Return to one source column p in G(Lambda) and a bad row z in A, so M(z,p)=0. Suppose a transition-one H-z representative exists. Section 2 gives a physical boundary vertex b in B=Lambda-{p} and a literal Hamilton path

  P_zb on A-{z}+{b}

with b as an actual endpoint. This conclusion does NOT require b to be quiet. There are exactly two possibilities, now stated entirely in support language.

(EXCHANGE.) If Lambda-{b} is Hamiltonian, equivalently b in G(Lambda), then b is quiet on the opposite source side. The section-3 normalization gives the exact balanced exchange

  H-b : A | (Lambda-{b}),
  H-z : (A-{z}+{b}) | (Lambda-{b}).

The source pivot p->b keeps the non-Hamiltonian universe Lambda fixed, replaces the other universe A+{p} by A+{b}, and changes the bad deletion z into a good deletion of the new universe because A-{z}+{b} is Hamiltonian.

(TRANSFER.) If Lambda-{b} is non-Hamiltonian, then by section 8 the same physical b is itself universally crossing on the B side relative to the unchanged source C_p. Thus the bad-deletion obstruction has transferred from z in the first universe to b in the second universe. The endpoint-certified Hamilton replacement A-{z}+{b} is retained even though no source pivot is yet available.

This yields a finite conditional normal form if transition-one representatives are available whenever a universal vertex is encountered. Keep the source C_p fixed whenever the TRANSFER branch occurs. Starting from a bad z in A, choose a transition-one boundary b in Lambda-{p}. If b is good in Lambda, stop in EXCHANGE. If b is bad, apply the dual transition-one statement to b. Its boundary is some a in A and certifies a Hamilton path on

  (Lambda-{p,b}) union {a}

with a as endpoint. If a is a good deletion of Omega=A+{p}, the dual EXCHANGE occurs; if a is bad, transfer again.

Therefore, if every encountered boundary remains bad and no EXCHANGE occurs, finiteness forces an alternating directed cycle of bad physical vertices

  z_0 -> b_0 -> z_1 -> b_1 -> ... -> z_r -> b_r -> z_0,

with z_i in A and b_i in Lambda-{p}. Every arrow retains an actual endpoint-certified Hamilton one-for-one replacement of the corresponding fixed source rail. No simultaneous compatibility of the Hamilton orders around the cycle is asserted.

The length-two cycle is especially concrete. If z->b and b->z, the two certified endpoint paths

  A-{z}+{b},
  (Lambda-{p,b})+{z}

are disjoint and together span H-p. Hence they form a second literal exact H-p two-cover obtained from the original A | (Lambda-{p}) by swapping z and b across the two supports; both exchanged vertices are actual endpoints in the swapped representative. This is a genuine same-residue representative switch, not merely a signed packet. It still does not by itself insert the omitted source label p.

Consequently, conditional on transition-one compression, the universal-crossing arm reduces further to two parent consumers: a monotone theorem for EXCHANGE pivots, or an order-valued theorem consuming an endpoint-certified alternating bad-deletion cycle. Neither theorem is proved here.



