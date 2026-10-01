# Every six-set has a deletion graph of positive minimum degree, with only a four-label non-Hamiltonian-core matching exception

## Statement

Let H be any boundary tournament and let U be any six-vertex set, with no Hamiltonicity assumption on U. Put D={d in U:H[U-{d}] is Hamiltonian}, and join d,e in D in the graph J when H[U-{d,e}] is Hamiltonian. Then |D|>=4 and delta(J)>=max{1,|D|-4}. If J has no two adjacent edges, then |D|=4, J is a perfect matching, and H[D] is a non-Hamiltonian edge-orderable four-set, hence a matching-block K4. Writing U-D={a,b}, both D+{a} and D+{b} are non-Hamiltonian and every (D-{d})+{a} and (D-{d})+{b}, d in D, is Hamiltonian. Consequently |D|>=5, or Hamiltonicity of the four-label set D when |D|=4, forces two adjacent edges of J.

## Body

All assertions are local to U. The four-of-six theorem in smallset01 gives |D|>=4. Fix d in D and consider the Hamiltonian five-set F=U-{d}. It has at least two Hamiltonian four-subsets, by deleting the endpoints of any Hamilton order. Among the |D|-1 four-subsets F-{e} with e in D-{d}, at most three are non-Hamiltonian. Therefore deg_J(d)>=|D|-4.

For the remaining case |D|=4, suppose d has no neighbor. Write D-{d}={e1,e2,e3} and U-D={a,b}. Then each of {a,b,e1,e2}, {a,b,e1,e3}, {a,b,e2,e3} is non-Hamiltonian. Partition {e1,e2,e3} according to whether (a,ei,b) or (b,ei,a) is tight. Two labels belong to the same class. The parallel-middle four-path lemma in localextend01 makes their four-set with a,b Hamiltonian, a contradiction. Thus delta(J)>=1 in this case as well. This is also the prescribed-overlap argument of extremal01, now without its unnecessary non-Hamiltonicity assumption on U.

If J has no adjacent edges, every degree is one, so J is a perfect matching. Its vertex number is even. Since 4<=|D|<=6, only 4 or 6 remain. The bound deg_J(d)>=|D|-4 excludes 6, so |D|=4.

Write U-D={a,b}. By definition of D, U-{a}=D+{b} and U-{b}=D+{a} are non-Hamiltonian. Suppose H[D] were Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 to D and exterior vertices a,b. Its graph K on D joins y,z when {a,b,y,z} is Hamiltonian. On four vertices, complementation sends the two disjoint edges of a perfect matching to each other. Since {a,b,y,z}=U-(D-{y,z}), the edge family of K is exactly the complement-pair image of the edge family of J. Hence K is also a perfect matching, contrary to that lemma's adjacent-edge conclusion. Therefore H[D] is non-Hamiltonian.

The non-Hamiltonian five-set D+{a} is edge-orderable by smallset01. Its restriction represents H[D], and the four-vertex classification makes D a matching-block K4. Moreover a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. In D+{a} that exceptional four-subset is D itself, so (D-{d})+{a} is Hamiltonian for every d in D. The same argument applies to b. This proves all conclusions.

The proof uses neither minimum-counterexample calculus, ambient order, path positions, extremality, nor Hamiltonicity or non-Hamiltonicity of U. The matching exception is a necessary structural alternative; its realizability is not asserted.