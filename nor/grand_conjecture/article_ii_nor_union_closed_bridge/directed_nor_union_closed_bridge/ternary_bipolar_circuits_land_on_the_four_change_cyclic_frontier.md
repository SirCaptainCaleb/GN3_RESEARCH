# Ternary bipolar circuits land on the four-change cyclic frontier

## Composition

In a minimum ternary counterexample, the singleton-cap sandwich of a bipolar circuit has linear word tau sigma^p tau^q with p=|P|-2 and q=|X|-1. Deleting the initial singleton gives a one-change deletion order ending in tau, so endpoint blocking forces the first cyclic wrap status to be sigma. The resulting cyclic order therefore has exactly four changes and, up to rotation and reversal, run profile 1,p,q,2. Thus ternary bipolar circuits are instances of the four-change cyclic frontier from Article I; circuit sizes two and three correspond to the singleton- and two-window middle-run regimes.

## Development

## Ternary bipolar circuits land on the four-change cyclic frontier

Work in a minimum counterexample to directed ternary NOR. Let \(P\) be a maximal \(\sigma\)-tight path with omitted set \(X\), and suppose \(X\) is a bipolar circuit at the two ends of \(P\). Put \(\tau=1-\sigma\),
\[
p=|P|-2,\qquad q=|X|-1.
\]
Assume \(|X|\ge2\).

Fix \(x\in X\). By the bipolar sandwich theorem there is a spanning order \(S_x\) with linear status word
\[
\tau\,\sigma^p\,\tau^q.
\tag{1}
\]
Concretely, put the singleton \(x\) on the left pole and use a rear-pole witness for \(X\setminus\{x\}\) on the right. Deleting the initial singleton \(x\) leaves a one-change order \(D_x\) of \(V\setminus\{x\}\) whose word is
\[
\sigma^p\tau^q.
\]

### Theorem: cyclic closure has four changes and a 1--p--q--2 profile
Regard \(S_x\) as a cyclic coordinate order. The resulting cyclic status word has exactly four changes. Up to cyclic rotation and reversal, its four run lengths are
\[
1,\ p,\ q,\ 2.
\tag{2}
\]

### Proof
Write the last two vertices of \(D_x\) as \(u,v\), so the first cyclic wrap status after the linear word of \(S_x\) is
\[
z_1=h(u,v,x).
\]
The deletion order \(D_x\) ends in color \(\tau\). Since the ambient coloring is a minimum counterexample, endpoint blocking for the omitted vertex \(x\) gives
\[
z_1=\sigma.
\tag{3}
\]
The second wrap status, call it \(z_2\), is unrestricted by endpoint blocking. The cyclic word is therefore
\[
\tau,\sigma^p,\tau^q,\sigma,z_2.
\tag{4}
\]
If \(z_2=\sigma\), the cyclic run lengths are directly
\[
1,p,q,2.
\]
If \(z_2=\tau\), the final \(\tau\) merges cyclically with the initial singleton \(\tau\), giving run lengths
\[
2,p,q,1.
\]
Reversing the cyclic order reverses the run-length list (while complementing colors), so this is equivalent to
\[
1,q,p,2.
\]
which has the same canonical form (2) after renaming the two middle runs.

In either case the cyclic word has four changes. It cannot have fewer by the displayed run decomposition; equivalently, a two-change cyclic word could be cut to give a spanning one-change linear order, contrary to counterexamplehood. \(□\)

### Consequences
A ternary bipolar circuit is therefore not a new independent obstruction. It canonically produces the same minimum-variation four-change cyclic geometry isolated in Article I. Moreover one of the two non-end run lengths is exactly
\[
q=|X|-1.
\]
Hence:

- \(|X|=2\) gives the four-change profile with a singleton middle run;
- \(|X|=3\) gives the profile with a two-window middle run, landing in the rigid rear-polarization regime already developed in Article I;
- larger bipolar circuits correspond to the same cyclic frontier with longer middle residual run.

This identifies the no-descent branch of Article II with Article I's full-support interval-reversal frontier. Any proof that eliminates the canonical four-change profile \(1,p,q,2\) simultaneously eliminates ternary bipolar circuits. Conversely, Article II supplies an interpretation of the middle residual run length as the size of the punctured-Boolean circuit minus one.
