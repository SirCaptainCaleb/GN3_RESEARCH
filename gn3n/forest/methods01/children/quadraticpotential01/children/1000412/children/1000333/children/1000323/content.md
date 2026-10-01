# Every trapped local 4-by-5-long quadratic minimum forces order disagreement

## Statement

Let H be a boundary tournament and let C=X|Y|P be a Phi-minimal three-cover in a trapped connected component of the pairwise-repartition graph, with |X|=4, |Y|=5, and |P|=a>=7. Then H contains explicit relative-order disagreement between Hamiltonian paths on overlapping induced supports contained in X union Y.

## Body

Put W=X union Y. By the certified theorem 6cb8966e16c9, H[W] has no Hamiltonian induced subset of order at least six.

Choose any six-element subset S of W. Then H[S] is non-Hamiltonian. By the certified four-of-six theorem in smallset01, at least four vertices d in S have H[S-{d}] Hamiltonian. Choose arbitrary Hamilton tight paths on four such five-vertex deletions. The certified theorem astra004fourgooddisagree applies to the non-Hamiltonian induced subtournament H[S] and forces two of those Hamilton paths to order a common pair of vertices differently.

Thus explicit relative-order disagreement already occurs inside S, hence inside W. No plateau migration, crossing classification, or additional orientation argument is needed.
