# A three-component beside any component of order at least five is never quadratic-potential minimal

## Statement

Let H be any boundary tournament and let F be any spanning path cover. If F has a component X of order three and another component P of order m>=5, then one legal pairwise repartition of X|P, leaving every other component unchanged, produces a spanning path cover with strictly smaller quadratic potential. Consequently, in any cover that is locally minimum for quadratic potential under pairwise repartitions, every component accompanying a three-component has order at most four.

## Body

Let F be the given spanning path cover, with a three-vertex component X and another component P=(p_1,...,p_m), m>=5. Only X and P will be changed.

If m=5, the induced boundary tournament on V(X) union V(P) has eight vertices. By the certified universal balanced-eight result, it has a partition into two Hamiltonian four-vertex paths. Replacing X|P by those two paths changes the quadratic contribution from 3^2+5^2=34 to 4^2+4^2=32, so the total quadratic potential strictly decreases.

Now assume m>=6. If X union {p_1} is Hamiltonian, replace X|P by a Hamilton path on X union {p_1} and the inherited path (p_2,...,p_m). The quadratic contribution drops by
(3^2+m^2)-(4^2+(m-1)^2)=2m-8>0.
The same argument applies if X union {p_m} is Hamiltonian.

It remains to suppose that both endpoint four-sets X union {p_1} and X union {p_m} are non-Hamiltonian. Apply the certified two-bad-extension lemma in localextend01 to the tight three-path X and the exterior vertices p_1,p_m. It gives a Hamilton tight path on X union {p_1,p_m}. Replace X|P by that five-vertex path and the inherited interior path (p_2,...,p_{m-1}), which is nonempty because m>=6. The quadratic contribution drops by
(3^2+m^2)-(5^2+(m-2)^2)=4m-20>0.

Every other component of F is unchanged in all cases. Hence a legal pairwise repartition of X|P strictly decreases the total quadratic potential, proving the statement for an arbitrary spanning path cover.