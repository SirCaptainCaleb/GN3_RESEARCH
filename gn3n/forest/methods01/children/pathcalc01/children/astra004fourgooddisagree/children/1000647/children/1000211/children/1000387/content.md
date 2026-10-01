# Every minimum counterexample contains an explicit reversing tight triple

## Statement

Every minimum counterexample H contains a tight path P of order at least three and a tight triple T such that T reverses an ordered edge of P.

## Body

By 4cf010e3e5b3, a minimum counterexample contains two tight paths R,S, each of order at least three, whose common vertices occur in different relative orders.

Apply Section 4 of the path-intersection calculus pathcalc01 to R,S.

If pathcalc01 gives a tight triple reversing an ordered edge of R or S, the conclusion holds.

If it gives a common ordinary edge traversed oppositely, say (u,v) is an ordered edge of R and (v,u) an ordered edge of S, choose a consecutive tight triple of R containing (u,v). Such a triple exists because R has order at least three. That tight triple contains (u,v), hence reverses the ordered edge (v,u) of S.

It remains that pathcalc01 gives a vertex-simple tight cycle C. Opening C at any cyclic cut gives a Hamilton tight path on V(C). The cycle cannot span H, because then H would be Hamiltonian. Put K=H-V(C). Minimum-counterexample calculus gives pc(K)<=2. The subtournament K cannot be Hamiltonian, because an opened Hamilton path on C together with a Hamilton path on K would two-cover H. Hence K is non-Hamiltonian with pc(K)=2. Since every boundary tournament of order at most three is Hamiltonian, |K|>=4.

Choose a displayed two-cover A|B of K. Some component, say A=(a_0,...,a_m), has order at least two. Fix a cyclic cut c_i|c_{i+1} and open the cycle as (c_i,c_{i+1},...,c_{i-1}). If both (a_{m-1},a_m,c_i) and (a_m,c_i,c_{i+1}) were tight, concatenating A with this opened cycle would give a tight path and, together with B, a spanning two-cover of H. Hence at least one is non-tight. Boundary reversal antisymmetry gives respectively (c_i,a_m,a_{m-1}) or (c_{i+1},c_i,a_m) tight. The first reverses the displayed edge (a_{m-1},a_m) of A; the second reverses the displayed cycle edge (c_i,c_{i+1}).

Thus every output of pathcalc01 yields a tight path of order at least three together with a tight triple reversing one of its ordered edges.
