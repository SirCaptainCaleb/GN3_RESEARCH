# D23 — Carrier currentization, deletion rigidity, mate clauses, and anchored capacity

General currentization and recompletion machinery: physical-star currentization, universal-extension deletion rigidity, component-drop pair production, same-representative carrier growth, mate-box/restoration clauses, negative rooted-completion and local-search fences, physical mate-cycle implication, and anchored capacity.

## Rank-two physical-star currentization and the capture-free two-trimer front door

R154 is the clean currentization theorem. Fix a physical vertex `x` and incident supports `{p,x}` and `{x,y}`. They can be simultaneously currentized exactly when they form the compatible two-edge star of a tight trimer, equivalently one of the two composable orders `p,x,y` or `y,x,p` is tight. Boundary antisymmetry decides the unique tight orientation; prescribed-path completion then puts that trimer into a minimum three-cover. A physical star of rank at least three cannot be selected by a path cover because selected degree is at most two.

The theorem is deliberately physical. It currentizes the named supports; it does not inherit old carrier identity, old selected orientations, endpoint roles, or residual rails. This distinction becomes crucial in the later capture repairs.

R155 is the mirror-reentry theorem for a captured crossing and a carrier adjacency. Its durable content is: retain a historical capture event of `x` through a physical crossing `D={x,y}`; if `A` is a certified tight carrier crossed by D and `E={p,x}` is a genuine adjacency of A, then a later exact three-cover can currentize D and E as the two boundaries of their unique mirror trimer while retaining the capture event as ancestry. The later scope correction R528 is developed in D15: A may be certified after the capture, but E must actually be an adjacency of a certified carrier that D crosses. Arbitrary fresh incident supports are not enough.



### Capture-free two-trimer front door

By R169, the exterior E=V(H)-V(K) has at least five vertices. Choose five distinct exterior vertices d_1,d_2,r,y,s. Boundary antisymmetry R3 gives exactly one tight orientation of the three-set {d_1,b,d_2} with middle b; call the resulting tight trimer C. Its two terminal physical supports {d_1,b} and {b,d_2} are distinct supports incident with b, so R154 currentizes their unique compatible mirror packet, equivalently C, as one component of a minimum three-cover. Independently, R3 gives a tight orientation T of {r,y,s} with prescribed middle y. The trimers C and T are vertex-disjoint because b lies on K while all five chosen vertices lie in E and the chosen exterior vertices are distinct. Therefore R41 applies directly: the two terminal dimers of C and the two terminal dimers of T supply the synchronized central-anchor interaction with middle-anchor pair {b,y}. No capture, puncture, crossing, reentry, or ancestry transport is used. Hence the currentizable two-trimer geometry and R41 interaction asserted at the bare structural level by R273 are already forced by R3/R41/R154/R169; only the extra statement that C terminal supports carry ancestry from two particular R264 punctures could constitute additional content.

## Universal-extension deletion rigidity and the cut-deficit interface

R156 gives a useful pure graph lemma. Suppose a proper set X has the property that for every outside vertex r, `X+r` admits a Hamilton tight path. Then the complement `H-X` has path-cover number exactly two, and no exact two-cover of it can contain a singleton rail. If the complement were Hamilton, or if an exact cover had singleton r, the Hamilton path on X+r could be glued to the remaining rail and produce a forbidden two-cover of H.

R157 refines this for a fixed exact complement cover: if r is an endpoint of one complement rail, the Hamilton path on X+r must place r internally unless X itself is Hamilton. The internal-vertex graft then pays the unique terminal state and produces a minimum three-cover while preserving the opposite rail literally. This is a representative-sensitive but exact surgery theorem.

R158 is the local splice-or-full-breach ancestor, superseded by R167. At a selected carrier crossing, either the old carrier incidence is selected and the crossing is a literal splice, or no historical carrier edge at the crossing vertex remains selected. R167 upgrades this to the cut-deficit theorem: for a partition C|Y in an exact k-cover,

`t = 1 + pc(Y) - k + ρ`.

Thus whenever `k≤pc(Y)` a crossing is forced, and the R158 local dichotomy applies there. This is the correct general interface.



## Component drop creates balanced signed pairs

R159 is the component-drop pair theorem. Let a proper residue W have both a literal c-cover and an r-cover with `r<c`. Some selected state of the smaller cover must cross two components of the larger cover; otherwise the smaller cover could not reduce the component count. The selected cross-state, together with the exact deletion/recompletion geometry, feeds the spare-vertex cross-state upgrade already developed as R176 in D16 and yields a graph-intrinsic balanced opposite-sign pair. The pair need not be current in either source representative.

R160 is the fixed-trimer repeated-birth theorem. If pair births use terminal dimers of one fixed trimer around its shared middle, a later birth cannot simply be treated as a fresh quiet epoch. The corrected preferred proof uses the cross-generation two-pair mechanism; R448 gives an explicit at-anchor formulation. Its strategic warning is important: strict support growth may only replay the original fixed trimer, so “nonquiet” is a historical interaction certificate, not automatically progress.


### Rooted cross-state payment: the spare coordinate need not be lost

There is a direct strengthening of the R159/R176 interface that is useful precisely when the proper residue has a named deleted or punctured vertex. Let H be a hypothetical smallest counterexample, let W be a proper vertex subset, and fix any vertex xi in V(H)\W. Let R be a literal path cover of W and T another literal path cover of W. Suppose T selects a directed state alpha beta whose endpoints lie in two distinct R-components. Then there is a finite chosen continuation yielding either a spanning two-cover of H or an ancestry-bearing both-singleton floor having xi literally as one singleton coordinate. The floor ancestry retains the physical cross-state support {alpha,beta} and the fact that this state crossed the two named R-components; neither source cover is asserted to remain current after payment.

Proof. Since xi is outside W, xi,alpha,beta are distinct. Apply boundary antisymmetry R3 to the reversal pair (xi,alpha,beta) and (beta,alpha,xi). Exactly one is tight. If (xi,alpha,beta) is tight, the oriented dimer (alpha,beta) is head-signed by witness xi. The vacuous two-vertex path (xi,alpha) makes singleton (xi) tail-signed by witness alpha. Thus (alpha,beta) and (xi) are physically disjoint opposite-sign supports, of sizes two and one. If instead (beta,alpha,xi) is tight, the oriented dimer (beta,alpha) is tail-signed by witness xi, while the vacuous path (alpha,xi) makes singleton (xi) head-signed by witness alpha. Again we have a balanced opposite-sign pair with one nontrivial support and singleton xi. The cross-witness convention is legitimate here: a sign witness must lie outside its own support, but may lie on the opposite support, exactly as recorded by R444. Apply accepted fully reconstructible R428 to this singleton/nontrivial pair. It preserves singleton xi throughout the chosen nonclosing descent and terminates at a spanning two-cover or an ancestry-bearing both-singleton floor containing xi. The original cross-state pair-birth certificate remains historical ancestry by R428 persistence.

Consequently the component-drop theorem itself has a rooted paid form. If R is a literal c-cover and T an r-cover of W with r<c, the counting step in the fully reconstructed proof P555 finds such a selected cross state alpha beta. Therefore for every chosen spare xi outside W, component drop yields either closure or an ancestry-bearing floor containing xi. In the common puncture application, where W is obtained by deleting an internal vertex xi from a larger exact-cover rail, one may choose that very puncture as the preserved floor coordinate. This bypasses the coordinate loss in the abstract R159 conclusion and does not require R176 payment.

Two useful specializations follow. First, if two exact covers of one pair-deletion residue H-D have different support partitions, the R410 crossing state can be fed to the argument above with either chosen d in D as xi; thus the noisy R410 branch can be paid to a floor preserving either deletion label. Second, in an endpoint-universal component-drop fan such as R409, every puncture-indexed 3-to-2 comparison can be paid to a floor retaining that exact puncture. These are source/provenance strengthenings, not closure: R428 does not preserve the old source covers as current, and R444 still forbids treating an anonymous singleton remint as progress.

This rooted payment lemma is proved internally from R3, the elementary component-drop crossing count when that corollary is used, and accepted R428. It is not yet a separately reviewed standalone claim.


## Literal carrier growth, mate boxes, and local restoration

R161 is a direct owner-growth argument that avoids abstract payment language. Start from any actual three-cover and choose a nontrivial owner rail. Whenever a seam to another rail is tight, absorb the donor head. A singleton donor with a tight final seam would already give a two-cover, so the process cannot terminate that way. Finite growth therefore reaches a state with both boundary seams bad, and their exact reversals provide two same-polarity witnesses on the final boundary. This is a useful alternative route to signed support production because every step stays in one representative.

R163 is the complete mate-box collapse. For a Cartesian box of k-cover proposals, each proposal has only one hole from each coordinate family. If every family had a bad mate, choosing one bad mate from every coordinate would make all reverse holes tight simultaneously and hence produce a forbidden k-cover. Therefore at least one coordinate family consists entirely of tight mates. This finite logical lemma later feeds implication-graph reasoning.

R164 is deleted-neighbor restoration collision: a tight edge/segment with both an old and a fresh endpoint extension yields either strict restoration or the exact reverse contact, by testing the relevant three-set. R166 is the analogous two-sided middle-incidence seam observation.



## Sharp rooted-completion and local-descent counterexamples

R165 is an explicit eight-vertex Strong counterexample to rooted endpoint completion. The graph has an unrooted two-cover, but no two-cover whose first rail begins at the prescribed vertex 0. The preferred exhaustive proof lists all tight simple paths beginning at 0, shows their maximum length is three, and checks that none has Hamilton complement; a displayed order-seven path plus a singleton gives the ordinary two-cover. Thus an unrooted two-cover theorem may not be silently strengthened to a rooted one.

R178 is a second negative result: on an explicit eight-vertex system, single-vertex relocations and proper segment reversals do not form a complete local descent basis for the cyclic defect statistic. Every such local move stays at defect at least three, while a two-block transposition drops the defect to two. This explains why later proofs use structural replacement/payment rather than a generic local-search monotone.



## Physical mate-clause implication calculus

R173/R463 is the physical mate-clause implication calculus. A certified two-hole proposal with mate literals A,B would become a forbidden spanning k-cover if both hole turns were tight. Hence at least one hole is bad, and R3 converts this into the valid disjunction A∨B. More precisely, if bar(A) is tight then A is bad, so B must be tight; thus each physical clause gives implications bar(A)→B and bar(B)→A. Composing these labelled implications along a directed path preserves the actual path-cover proposal behind every edge.\n\nA path bar(X)→...→X forces X: if X were bad, R3 would make bar(X) tight and propagation would make X tight as well. The original finite R173 mate-cycle is exactly this pattern for a cyclic list of physical clauses. R463 also permits collision-decorated sinks. If a sink literal L=(w,p,q) is accompanied by a retained same-polarity certificate (wprime,p,q) with wprime≠w, then once L is forced, R38 gives the named same-support collision; the tail-signed version is dual. Therefore a source clause whose two alternatives each have a physical implication path to decorated sinks forces one of those collisions.\n\nIn the all-internal R359 state, the R453 U-to-V splice clause has endpoints A=(v_1,u_r,u_{r-1}) and B=(v_2,v_1,u_r). R359 supplies shield turns (x,u_r,u_{r-1}) and (v_2,v_1,x), so A and B are already collision-decorated. R463 with zero-length paths therefore forces one of the two residual-terminal collisions; swapping U,V gives the other directional channel.\n\nThis is the selected P478 argument. The implication logic itself is explicit here, but the route service correctly marks the whole dependency closure not fully reconstructible because R38, R359, and R453 retain legacy-dependent routes. Physical proposals and decorated support/witness identities must therefore remain attached; abstract SAT implication without them is not a substitute.

## Anchored capacity and the one-reservoir boundary

R179-R182 form one compact extremal proof.

Fix two signed anchors/witnesses and maximize the total size of two disjoint supports P,T. Any reservoir vertex x outside them cannot be appended at an unsigned end, else capacity increases. Boundary antisymmetry therefore forces the reverse-star turn at that end. This is R179.

R180 observes that every reservoir vertex consequently signs one of two fixed reverse terminal dimers in the same tested orientation/polarity class. If the reservoir has at least two vertices, two distinct witnesses hit the same physical support and the same-support interaction theorem applies. If the reservoir is empty, the supports and their witnesses already absorb the graph into at most two paths. Exactly one reservoir vertex is the sole unresolved case.

R181 is a specialized floor collision obtained by counting: a pair of singleton floor supports, retained anchor data, and a disjoint reserve trimer leave at least two reservoir vertices, so R180 fires. R182 is the historical selected-wrap alignment theorem used to keep the final quiet branch on an old residual boundary. It is representative-sensitive and should not be generalized into arbitrary overlap transport.



## Generic payment and fixed-turn descent are centralized in D16

The historical terminal-payment theorem R162 and its reconstructible replacement R532, the proper-turn front door R170, literal pair-frame discharge R171, fixed-turn clock R172, and carrier refund theorems R174/R175 are expanded in D16. Their alternative routes are retained there: the literal same-frame R171 route is not collapsed into the shorter abstract descent proof, and the two R532 terminal-payment factorizations remain distinguished. D23 uses those theorems as interfaces but no longer carries a second derivation.