# A minimum shortcut-free signature shore cannot have size three

## Metadata

- ID: a_minimum_shortcut_free_signature_shore_cannot_have_size_three
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 349
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A minimum shortcut-free signature shore cannot have size three

Assume the minimum shortcut-free shore is
\[
A=\{u,v,w\}.
\]
By §343/§344, after cyclic naming
\[
u\to v\to w\to u,
\]
and the two five-coordinate connector orders
\[
S_0=(u,x,z,v,w),\qquad S_1=(w,v,z,x,u)
\]
have words \(000\) and \(111\).

Since \(A\) has exactly three vertices,
\[
V=B\sqcup\{x,z,u,v,w\}.
\]
Thus inserting one of these connector blocks into an order of \(B\) produces a spanning full order.

Take any NOR-good order
\[
P=(b_1,\ldots,b_r)
\]
of \(B\), which exists by minimum-counterexample induction.

If its word is monochromatic, append or prepend the connector with either matching or opposite color; the resulting spanning word has at most one change. Hence assume
\[
c(P)=0^p1^q,\qquad p,q\ge1.
\]

For \(1\le j\le r-1\), define the uniform extension bit
\[
e_j=\alpha(b_j,b_{j+1},a),
\]
where \(a\) is any coordinate of \(A\cup\{x,z\}\). The split dominance makes this independent of \(a\).

### Interior insertion law

Insert \(S_\eta\), \(\eta\in\{0,1\}\), in the gap
\[
b_i\mid b_{i+1}.
\]
Away from the global endpoints, the two old windows straddling that gap are replaced by
\[
\boxed{e_{i-1},\ \eta,\eta,\eta,\eta,\eta,\ e_{i+1}.}
\]
All other old windows are unchanged.

### Both phases long

Assume \(p,q\ge2\). The switch of \(c(P)\) lies between
\[
c_p=0,\qquad c_{p+1}=1.
\]

Insert the connector one gap to the left of the switch, between
\[
b_p\mid b_{p+1}.
\]
The unchanged windows before the packet are all \(0\), and those after the packet are all \(1\). For neither connector color to give a one-change full word, the packet endpoints must form the forbidden descent
\[
e_{p-1}=1,\qquad e_{p+1}=0.
\tag{L}
\]

Now insert one gap to the right of the switch, between
\[
b_{p+2}\mid b_{p+3}.
\]
The same monotonicity test says failure of both connector colors requires
\[
e_{p+1}=1,\qquad e_{p+3}=0.
\tag{R}
\]

But (L) and (R) give simultaneously
\[
e_{p+1}=0,\qquad e_{p+1}=1,
\]
impossible.

Hence one of the two neighboring insertions, with one of \(S_0,S_1\), is a spanning NOR-good order.

### Short left phase

If \(p=1\), insert the connector in the first gap
\[
b_1\mid b_2.
\]
The new word begins
\[
\eta^5,e_2
\]
and all unchanged later windows are \(1\). Choose
\[
\eta=e_2.
\]
If \(e_2=0\), the word is \(0^*1^*\); if \(e_2=1\), it is monochromatic \(1\) through the junction. In either case the full word has at most one change.

### Short right phase

If \(q=1\), use the symmetric final gap
\[
b_{r-1}\mid b_r.
\]
The unchanged earlier windows are all \(0\), and the new suffix is
\[
e_{r-2},\eta^5.
\]
Choose
\[
\eta=e_{r-2}.
\]
Again the spanning word has at most one change.

### Theorem

Every shortcut-free switching split with minimum shore of size three yields an explicit spanning NOR-good order. Therefore a minimum counterexample satisfies
\[
\boxed{|A|\ge4.}
\]

The proof is entirely local and uses only the monochromatic connector seed plus the one-change order on the opposite proper shore. No protected-root extraction is needed in this branch.

## Frontier

- Development version when composed: None
- Development version now: 1
