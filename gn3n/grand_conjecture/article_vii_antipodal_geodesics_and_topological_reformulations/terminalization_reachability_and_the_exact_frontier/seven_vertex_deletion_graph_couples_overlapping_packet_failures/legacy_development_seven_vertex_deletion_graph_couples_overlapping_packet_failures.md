# Seven-vertex deletion graph couples overlapping packet failures — preserved pre-item development

## Composition

(none yet)

## Development

Let W be a seven-vertex set in a boundary tournament. Define an ordinary graph G_W on W by
iv in E(G_W) if and only if H[W-{i,v}] is non-Hamiltonian.
Then Delta(G_W)<=2.

Proof. For a fixed i, the packet S_i=W-{i} has order six. Its non-Hamiltonian five-deletions are precisely S_i-v=W-{i,v}, indexed by the neighbors v of i in G_W. Four-of-six in [[smallset01]] permits at most two such deletions. QED. Thus G_W is a disjoint union of isolated vertices, paths, and cycles. No claim that cycles are excluded is needed.

Now place W inside an arbitrary larger H. For each i let D_i be any available family of two-path covers T|U of H-S_i, with both actual displayed paths of order at least two. If H has no two-cover, every packet bridge v occurring in any D_i must satisfy iv in E(G_W): otherwise S_i-v is Hamiltonian and the bridge concatenation completes a two-cover.

This links the packet obstructions in two ways:
(1) a bridge v forced bad in packet S_i imposes the same bad five-set in packet S_v, since the deletion relation is symmetric;
(2) the union of all forced neighbors of each i has order at most two, regardless of how many tail decompositions are tested.

Saturation certificate. Suppose distinct i,j,v lie in W, and v is a bridge for some cover in D_i and for some cover in D_j. If both tests fail, iv and jv are edges. The degree bound exhausts the possible neighbors of v. Therefore, if some available cover in D_v has a bridge w not in {i,j}, that third test must succeed: vw cannot be another bad deletion, so S_v-w is Hamiltonian and its two tails join through w.

For neighboring mobile-cut packets, their union has order seven whenever the packets differ by one corridor vertex. The same graph therefore tests their consistency. However the third packet S_v need not automatically have a two-tail complement: its removal may introduce an additional fragment or leave an exterior vertex outside the packet. The certificate requires the actual cover in D_v; it cannot be inferred by simply deleting an internal vertex of a tight path.

This is a structural compatibility condition across overlapping packet tests. It supplies sufficient repairs when the specified three tests exist. It does not exclude all maximum-degree-two deletion graphs, nor does it reduce the whole unbounded corridor theorem to a seven-vertex computation.
