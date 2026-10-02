# Weighted path principle holds under six-vertex concentration

## Statement

Let H be a finite boundary tournament with nonnegative vertex weight w and total weight W. For every vertex set S with |S|<=6, H contains a tight path P with w(V(P)) >= 3w(S)/4. Consequently, if some six-vertex set S has w(S)>=2W/3, then P has weight at least W/2; in particular Astra idea 001 holds for every boundary tournament of order at most nine.

## Body

For |S|<=3, S itself is Hamiltonian, so there is nothing to prove. For |S|=4, every three-vertex deletion is Hamiltonian. Delete a minimum-weight vertex of S; the remaining three vertices form a tight path of weight at least 3w(S)/4.

For |S|=5, if H[S] is Hamiltonian then again there is nothing to prove. Otherwise the small-set structure theorem says that at most one four-vertex deletion is non-Hamiltonian. Hence at least four vertices d in S have S-{d} Hamiltonian. Among these at least four good deletion labels choose one of minimum weight. Its weight is at most w(S)/4, and a Hamilton path on S-{d} therefore has weight at least 3w(S)/4.

For |S|=6, the four-of-six theorem gives at least four vertices d in S such that S-{d} is Hamiltonian. Choose a minimum-weight good deletion label. Again w(d)<=w(S)/4, so a Hamilton path on S-{d} has weight at least 3w(S)/4.

Now suppose |S|=6 and w(S)>=2W/3. The preceding paragraph gives a tight path of weight at least (3/4)(2W/3)=W/2, proving the weighted longest-path inequality.

Finally, if |V(H)|=n<=9 and n>=6, take S to be the six heaviest vertices. Then w(S)>=6W/n>=2W/3, so the weighted inequality follows. For n<=5 it follows directly from the first two cases.

Thus any counterexample to Astra idea 001 must have order at least ten and, more sharply, every six-set must carry strictly less than two thirds of the total weight. This is a diffuseness condition on a dual obstruction.