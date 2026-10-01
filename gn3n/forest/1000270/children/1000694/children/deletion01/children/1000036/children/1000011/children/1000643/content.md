# Wrapped end-adjacent form A reduces to a Hamiltonian four-set or one matching-block K4

## Statement

In form (A) of 05612b48c326, namely H-p_1=(x,p_0,p_2,...,p_m)|Q, put K={x,p_0,p_1,p_2}. Then either H[K] is Hamiltonian, in which case H-K is non-Hamiltonian with path-cover number two, or H[K] is edge-orderable and is a matching-block K4 with the uniquely forced block order {p_0p_1,xp_2} < {xp_0,p_1p_2} < {p_0p_2,xp_1}.

## Body

Write a=p_0, b=p_1, c=p_2, z=x. From the original deletion cover H-z=(a,b,c,...)|Q and endpoint-hook forcing we have (a,b,c), (b,a,z), and (c,z,a) tight. From form (A), H-b=(z,a,c,...)|Q, and endpoint-hook forcing for this deletion cover, we have (z,a,c), (a,z,b), and (c,b,z) tight. Suppose first that H[K] is Hamiltonian. Then H-K has the displayed two-cover (p_3,...,p_m)|Q. If H-K were Hamiltonian, a Hamilton path on K together with one on H-K would two-cover H, impossible. Hence pc(H-K)=2 and H-K is non-Hamiltonian. Now assume H[K] is non-Hamiltonian. On the three vertices {a,b,z}, the tight triples (b,a,z) and (a,z,b) give comparison arcs ab->az and az->bz. Thus this comparison triangle is transitive. By the certified four-vertex comparison classification used in d26c575019cc, the exceptional non-edge-orderable non-Hamiltonian K4 has cyclic comparison orientation on every three-vertex subset. Therefore H[K] is edge-orderable. Apply the matching-block classification. Let M0={ab,cz}, M1={ac,bz}, M2={az,bc}. The tight triples (b,a,z) and (c,z,a) give M0<M2. The tight triples (z,a,c), (a,z,b), and (c,b,z) give M2<M1. Hence the block order is uniquely M0<M2<M1, which is {p_0p_1,xp_2} < {xp_0,p_1p_2} < {p_0p_2,xp_1}. No cyclic rotation of an ordered tight triple is used.
