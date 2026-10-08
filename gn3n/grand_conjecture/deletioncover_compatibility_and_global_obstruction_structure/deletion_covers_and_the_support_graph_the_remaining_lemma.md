# The remaining lemma

The preceding argument reduces the deletion-cover method to the following statement.

**Remaining Lemma.** Let \(H\) be a minimum counterexample and let \(H-x=P\mid Q\) be a deletion cover. Suppose that the selected deletion covers yield, relative to \(P\mid Q\) or to a consecutive double deletion,
- an order disagreement attached to the displayed supports;
- an edge in an endpoint deletion cover joining surviving vertices of \(P\) and \(Q\);
- an inherited displayed path edge whose endpoints lie in different paths of an endpoint deletion cover; or
- an edge joining distinct inherited path pieces in the odd-cycle configuration.

Then \(H\) has a spanning ordering of defect span at most \(2\).

By Lemma 1, this would contradict the choice of \(H\). In the odd-cycle case it would also suffice to prove that the rank transport of Lemma 10 forces a Hamiltonian vertex cover of the ground cycle of order \(k+1\), since Lemma 11 would then give a two-cover directly.

No further production of isolated reversals is required: Lemma 10 already supplies many. The unresolved point is to use their positions to remove one of the two independent defects in the spanning order arising from a deletion cover.
