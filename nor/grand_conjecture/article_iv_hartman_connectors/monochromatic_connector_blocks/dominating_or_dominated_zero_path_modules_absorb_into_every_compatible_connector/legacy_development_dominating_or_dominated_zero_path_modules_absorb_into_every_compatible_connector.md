# Dominating or dominated zero-path modules absorb into every compatible connector — preserved pre-item development

## Relative absorption of a whole extremal shore module

Work in the fixed flat split B→z→A→x with z→A→x and z→x. A compatible zero connector C on U=R∪{x,z} is an order with every consecutive ternary color zero and both exposed ordered pairs forward in the fixed representing tournament t. A *ported zero path* P on a nonempty subset H⊆A has zero ternary word and forward first/last ordered pair whenever the pair exists (singletons qualify).

THEOREM (source-module and sink-module absorption). Let A=H⊔R, H nonempty, and suppose H admits a ported zero Hamiltonian path P. If either H→R or R→H holds, EVERY compatible zero connector C on R∪{x,z} can be enlarged to a compatible zero connector on all A∪{x,z}, preserving the relative order and internal windows of C away from a single boundary insertion. The x,z positions need not be adjacent. Both endpoint ports in the resulting connector are forward.

PROOF. The flat ternary identities are h(z,a,b)=h(a,b,x)=1−t(a,b) for shore a,b; also h(a,x,z)=h(x,z,a)=0. For a shore b,c with b→c, and any p∈H, when H→R both (p,b,c) and (p,b,x) have color zero, whereas when R→H both (b,c,p) and (z,b,p) have color zero. For consecutive p,q of P with p→q, mixed triples z,p,q; p,q,x; b,p,q in the dominated-module case; and p,q,b in the dominating-module case all have color zero when their outside orientation is as indicated. Only the first and last edges of P enter any splice.

CASE H→R. A compatible C starts either with a shore vertex b or with z: it cannot start with x, and a forward first pair cannot run from a shore vertex to z.

(i) If C starts b,c with b∈R, its first port b→c is forward and c belongs to R or is x. Prepend P: (P,b,c,...). H dominates b and c; the two mixed ternary windows are zero using the final forward edge of P and b→c. For |P|=1 the sole mixed triple is (p,b,c), also zero. The first port is the first port of P, or p→b in the singleton case. The last port is unchanged.

(ii) If C starts z,b with b∈R, and has next vertex c, the zero window (z,b,c) forces b→c (c∈R or c=x). Insert P directly after z: (z,P,b,c,...). The mixed windows (z,p_1,p_2), (p_{s−1},p_s,b), and (p_s,b,c) are zero (with the evident shortening for s=1). The first port z→p_1 and the old final port are forward.

(iii) A compatible zero connector cannot begin z,x,b with b in R: the unchanged flat signature is α(z,x,b)=1. Thus if it begins z,x, its entire order is C=(z,x) and R is empty. Then z,P,x is a compatible zero connector, using the source/sink signatures and both ports of P.

Cases (i) and (ii), together with the degenerate C=(z,x), exhaust compatible starts. In case (ii) the next vertex exists because x is still in C.

CASE R→H. Dually check the right end directly. A compatible C ends either with a shore vertex b∈R or with x. If it ends u,b, its final port u→b is forward, u∈R or u=z, and both u,b dominate H. Append P: (...,u,b,P). If it ends u,b,x, its zero window (u,b,x) forces u→b; insert P between b and x: (...,u,b,P,x). All mixed windows are zero by the initial and final forward P edges, uniform R→H, and H→x. For a singleton P, use h(u,b,p)=h(b,p,x)=0. The only compatible connector ending z,x is the length-two connector (z,x): any preceding shore coordinate u would give h(u,z,x)=1. For C=(z,x), use z,P,x. Thus the new final pair is forward, and the former first port remains forward. QED.

COROLLARY 1. An inclusion-minimal shore A lacking a spanning compatible zero connector contains neither a universal shore source nor a universal shore sink: deleting such a vertex gives a connector by minimality and the singleton absorption restores it. This is valid for separated x,z and for every connector state, with no extra boundary-collar hypothesis.

COROLLARY 2. Such a minimal obstruction has no proper extreme dominating or dominated subset H that possesses a ported zero Hamiltonian path. Any connector on the complementary proper shore extends through H.

COROLLARY 3. A transitive dominating or dominated shore module of arbitrary size always absorbs: use its forward topological order as P. Consequently these transitive extreme modules can be removed before the whole-shore Hartman problem.

The theorem is a genuine full-support extension under an extremal-module hypothesis, stronger than individual cap absorption: it works with an arbitrary compatible connector and independently moving x,z. It does not assert absorption for a general strong extreme module that requires two ported zero paths.
