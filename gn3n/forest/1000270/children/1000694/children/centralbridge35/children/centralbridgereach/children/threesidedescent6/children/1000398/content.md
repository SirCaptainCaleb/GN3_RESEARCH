# Two four-vertex paths beside a path of order at least six admit a two-move descent

## Statement

Let A|B|P be any spanning three-cover of a boundary tournament with |A|=|B|=4 and |P|=m>=6. Two legal pairwise repartitions reach a three-cover of strictly smaller quadratic potential. The decrease is at least min(2m-10,4m-22)>=2. Consequently this size profile cannot minimize Phi in its pairwise-repartition component.

## Body

Choose distinct vertices u,v of A and a displayed Hamilton order (b_0,b_1,b_2,b_3) on B. If either B union {u} or B union {v} is Hamiltonian, choose that Hamiltonian five-set S. Otherwise apply repeated bad deletion in localextend01 to B,u,v: the set {b_0,b_1,b_2,u,v} is Hamiltonian, and choose it as S. Thus in all cases A union B contains a Hamiltonian five-set S.

Its complement T within A union B has three vertices, and every three-vertex boundary tournament admits a Hamilton path by reversal antisymmetry. Repartition A|B into S|T, leaving P unchanged. The potential increases by 5^2+3^2-4^2-4^2=2.

Now apply threesidedescent6 to T|P with S fixed. This second legal move decreases the potential by either 2m-8 or 4m-20. Relative to the original cover, the total decrease is therefore either 2m-10 or 4m-22, each strictly positive for m>=6. The two possible final order profiles are 5,4,m-1 and 5,5,m-2. Both moves stay within the same pairwise-repartition component. No restriction on m beyond the stated inequality and no order enumeration is used.
