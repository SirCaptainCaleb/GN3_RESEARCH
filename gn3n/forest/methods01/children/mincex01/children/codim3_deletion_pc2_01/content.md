# Deleting at most three vertices from a minimum counterexample leaves a non-Hamiltonian two-coverable subtournament

## Statement

Let H be a minimum counterexample. For every nonempty vertex set S with |S|<=3, the induced subtournament H-S is non-Hamiltonian and has path-cover number two.

## Body

Because H is a minimum counterexample, every proper induced subtournament has path-cover number at most two. Fix nonempty S with |S|<=3. The induced subtournament H[S] is Hamiltonian: for |S|=1 or 2 this is vacuous, and every three-vertex boundary tournament has a tight Hamilton path because exactly one of an ordered triple and its boundary flip is tight. If H-S were Hamiltonian, a Hamilton path on H-S together with a Hamilton path on S would form a spanning two-cover of H, contradicting that H is a counterexample. Hence H-S is non-Hamiltonian. Since H-S is proper and nonempty in a minimum counterexample, its path-cover number is exactly two.