# The neutral longest-six branch forces a three-corner exact-cover fan at one deletion

## Statement

Let H be a hypothetical order-eleven minimum counterexample with a longest six-path Y=(a,m1,m2,m3,m4,c), and suppose codim5_01 reaches its neutral distinct-endpoint exchange branch, producing a second six-path (ell,m1,m2,m3,m4,r). Then for some s among the three remaining vertices, H-s has at least three distinct exact 6|4 covers whose six-sides are three corners of the common-middle square. For every such corner six-side P with complementary four-side Q in H-s, both restorations P union {s} and Q union {s} are non-Hamiltonian.

## Body


Write
M=(m_1,m_2,m_3,m_4)
and suppose the neutral codim5 branch gives distinct exterior endpoints a,ell,c,r with

(a,M,c)
and
(ell,M,r)

tight. By common-middle rectangle closure, all four corner paths

(a,M,c), (a,M,r), (ell,M,c), (ell,M,r)

are tight six-paths.

Let T be the three vertices outside M union {a,ell,c,r}. For each corner uv, let

C_uv = V(H) - V(u,M,v),

a five-set. Since H has no spanning two-cover and (u,M,v) is Hamiltonian, C_uv is non-Hamiltonian.

Define
D_uv = {x in T : C_uv - {x} is Hamiltonian}.

The certified multiplicity theorem in commonmiddle01 gives |D_uv|>=2 for every corner and therefore a vertex s in T belonging to at least three of the four sets D_uv.

Fix this s. For every corner uv with s in D_uv, let

P_uv=(u,M,v),
Q_uv be any Hamilton path on C_uv-{s}.

Then
P_uv | Q_uv
is an exact two-path cover of H-s: the two supports partition V(H)-{s}; and H-s cannot itself be Hamiltonian, because a Hamilton path on H-s together with singleton s would be a spanning two-cover of H.

Thus H-s has at least three distinct exact covers of component orders 6 and 4, with the six-sides equal to at least three corners of the same common-middle square.

There is also a two-sided restoration barrier for each such cover.

First, P_uv union {s} is non-Hamiltonian. Otherwise a Hamilton path on P_uv+s together with Q_uv would be a spanning two-cover of H.

Second, Q_uv union {s}=C_uv is non-Hamiltonian by the definition of C_uv above.

Hence every member of this same-deletion three-corner fan is a 6|4 deletion cover for which restoring s to either component fails to Hamiltonize that component.

The endpoint-barrier theorem further supplies, for the same s,

(m_1,a,s), (m_1,ell,s), (s,c,m_4), (s,r,m_4)

tight. These are barriers, not extension triples: definitions01 forbids reversing them.

Therefore the correct neutral lambda-six residue is a same-deletion fan of at least three exact 6|4 covers on a common-middle square, with simultaneous two-sided restoration failure and four signed endpoint barriers.
