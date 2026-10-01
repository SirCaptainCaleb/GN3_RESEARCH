# From order fifteen onward a global four-side minimum forces order disagreement

## Statement

Let H be a minimum counterexample of order n>=15 and let X|P|Q be a spanning three-cover minimizing the quadratic potential Phi among all spanning three-covers. If one component X has order four, then H contains explicit order disagreement of the standard four-side type. In particular, a globally Phi-minimal four-side cannot remain order-neutral from order fifteen onward.

## Body

By the certified global minimum-side theorem, all component orders are at least four. Write |X|=4 and |P|=p>=q=|Q|>=4.

If p>=7, apply a25b748fb338 to X|P|Q. Its strict-descent alternative contradicts global Phi-minimality, so its explicit order disagreement alternative holds.

Hence an order-neutral counterexample must have p<=6. Since p+q=n-4>=11 and q<=p, only two possibilities remain: n=15 with {p,q}={6,5}, or n=16 with p=q=6. (For n>=17, p+q>=13 is already impossible under p<=6.)

Consider n=16, profile 4|6|6. Certified b7606848ddee applies to every cross-endpoint six-set of a global four-side minimum with both complementary paths of order at least six and forces order disagreement. Thus this case is not order-neutral.

It remains to exclude n=15, profile 4|6|5. Write P=(p_1,...,p_6) and X=(x_0,x_1,x_2,x_3). Global minimality rules out Hamiltonicity of X union {p_1} and X union {p_6}, because either endpoint transfer would change 4|6 to 5|5 and decrease Phi by 2. Therefore the certified repeated-bad-extension argument in foursidedescentobstruction supplies the crossed Hamiltonian five-set
F={x_0,x_1,x_2,p_1,p_6}
inside the ten-vertex induced subtournament K=H[V(X) union V(P)].
The certified order-ten theorem in extremal01 states that every ten-vertex boundary tournament with a Hamiltonian five-set admits a partition into two Hamiltonian five-sets. Hence K has a Hamiltonian 5|5 partition. Replacing X|P by this partition and leaving Q unchanged gives a spanning three-cover of H whose potential contribution on X union P drops from 4^2+6^2=52 to 5^2+5^2=50, contradicting global Phi-minimality.

Thus the 4|6|5 profile is impossible and the only remaining four-side profiles from order fifteen onward force explicit order disagreement.