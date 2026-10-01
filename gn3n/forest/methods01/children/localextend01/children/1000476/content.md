# Two Hamiltonian five-sets with a common four-core yield a Hamiltonian six-set or four-good-deletion transport

## Statement

Let H be a minimum counterexample, let K be a four-vertex set, and let a,b be distinct vertices outside K. Suppose K union {a} and K union {b} are Hamiltonian five-sets. Put U=K union {a,b}. Then either (1) U is a proper Hamiltonian six-set and H-U is non-Hamiltonian with path-cover number two; or (2) U is non-Hamiltonian, its Hamiltonian-deletion set D={d in U: U-{d} is Hamiltonian} has order at least four and contains a,b, and with L=H-U every L+d for d in D is non-Hamiltonian with path-cover number two. Moreover the graph J on D defined by de in E(J) iff U-{d,e} is Hamiltonian has minimum degree at least one, and every edge de gives L+d+e non-Hamiltonian with path-cover number two.

## Body

If U is Hamiltonian, it is proper in a minimum counterexample. If H-U were Hamiltonian then Hamilton paths on U and H-U would form a spanning two-cover of H. Hence minimum-counterexample calculus gives path-cover number two for H-U, proving (1). Assume U is non-Hamiltonian. Since U-a=K union {b} and U-b=K union {a} are Hamiltonian, a,b belong to the Hamiltonian-deletion set D. Apply d2205c472e75 to the non-Hamiltonian six-set U. It gives |D|>=4; for every d in D, L+d is non-Hamiltonian with path-cover number two; and the graph J on D defined by Hamiltonian two-deletions has minimum degree at least one, with every edge de yielding L+d+e non-Hamiltonian with path-cover number two. This is exactly (2).