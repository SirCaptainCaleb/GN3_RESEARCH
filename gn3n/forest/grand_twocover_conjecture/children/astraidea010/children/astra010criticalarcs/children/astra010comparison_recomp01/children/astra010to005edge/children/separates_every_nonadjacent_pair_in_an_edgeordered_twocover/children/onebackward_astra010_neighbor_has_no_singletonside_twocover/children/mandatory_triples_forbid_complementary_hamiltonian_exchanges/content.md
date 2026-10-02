# Endpoint-minimal mandatory triples forbid complementary Hamiltonian exchanges

## Statement

Let H have a mandatory ordered tight triple T, and let A|B be a spanning two-cover chosen so that A contains T consecutively and |A| is minimum. Let u,v be the endpoints of the displayed path A, and let C=A-{u,v}. For any subset S of V(B), suppose H[C union S] and H[(V(B)-S) union {u,v}] are both Hamiltonian. Then every Hamilton path on C union S must contain T consecutively; moreover this can occur only when T is contained in C. Consequently, if either T meets {u,v} or H[C union S] has a Hamilton path avoiding T, the two complementary supports cannot both be Hamiltonian.

## Body

Let P be any Hamilton path on C union S and Q any Hamilton path on (V(B)-S) union {u,v}. Their supports are disjoint and partition V(H), so P|Q is a spanning two-cover.

Because T is mandatory, one of P,Q must contain T consecutively. The support of Q meets A only in {u,v}, whereas the support of P meets A exactly in C.

If T meets {u,v}, then since T is a consecutive three-vertex subpath of A, at least one vertex of T lies in C as well. Thus neither support contains all three vertices of T, so P|Q cannot contain T, contradiction. Therefore simultaneous Hamiltonicity of the two complementary supports implies T subset C.

Now assume T subset C. Then Q contains no vertex of T, so mandatoryness forces P to contain T consecutively. Since P was an arbitrary Hamilton path on C union S, every Hamilton path on that support must contain T consecutively.

In particular, if H[C union S] admits even one Hamilton path avoiding T, then choosing it together with Q produces a spanning two-cover avoiding the mandatory triple, contradiction. This proves all assertions. ∎