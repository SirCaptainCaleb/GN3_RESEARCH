# Above order seventeen deletion-generated descent reaches one of two synchronized transport residues

## Statement

Let H be a minimum counterexample of order n>=18 and let H-x=P|Q be any one-vertex deletion two-cover. The trapped pairwise-repartition component containing the singleton lift P|Q|{x} contains, after three strict quadratic-potential-decreasing moves, a spanning three-cover with a Hamiltonian side of order four or five. Moreover, within the same trapped component at least one of the following occurs: (1) a further legal pairwise repartition strictly decreases quadratic potential; (2) a reachable Hamiltonian four-side state carries the bounded path-cover-two transport package of four_window_transport15; (3) a reachable Hamiltonian five-side X has another component R=(r_1,...,r_m), m>=7, and some four-set C⊂V(X) such that both C∪{r_1} and C∪{r_m} are Hamiltonian.

## Body

Start from the singleton lift S_0=P|Q|{x}. By bc151d5d2a89, two strict legal pairwise repartitions reach a deletion-generated three-side state S_2=X|R|T with |X|=3. Since n>=18, the larger inherited side in S_2 has order at least ceil((n-1)/2)-1>=8, so threesidedescent6 applies and gives a third strict legal repartition.

Inspect the output of threesidedescent6. If one endpoint of the long side is absorbed into X, the new side has order four; call the resulting reachable state W|A|B. Apply four_window_transport15. Its first alternative is a further strict legal endpoint-transfer descent, giving (1). Otherwise its explicit bounded one/two-label path-cover-two transport package gives (2). All moves up to W|A|B, and any strict descent supplied there, lie in the same pairwise-repartition component as S_0.

If instead both endpoint four-extensions of X are non-Hamiltonian, threesidedescent6 replaces X together with both ends of the long path by a Hamiltonian five-side Y and leaves the inherited interior of that long path. Thus the reachable state has component orders 5,p-3,q-1 up to relabelling, where p+q=n-1. The two non-five sides sum to n-5, so one has order at least ceil((n-5)/2)>=7 for n>=18. Call such a side R. Apply bc48e8bb931a to Y|R and the third component. Its endpoint-transfer alternative is a further strict legal repartition, again giving (1). Otherwise there is y∈V(Y) such that C=V(Y)-{y} extends Hamiltonianly with either displayed endpoint r_1,r_m of R, giving (3).

Hence, after the universal deletion-generated descent segment, large-order trapping can only persist through one of two synchronized transport residues: an explicit pc2 square/extension package attached to a reachable four-side, or a common four-core on a reachable five-side extending to both ends of a long path. Bare order disagreement is not used.