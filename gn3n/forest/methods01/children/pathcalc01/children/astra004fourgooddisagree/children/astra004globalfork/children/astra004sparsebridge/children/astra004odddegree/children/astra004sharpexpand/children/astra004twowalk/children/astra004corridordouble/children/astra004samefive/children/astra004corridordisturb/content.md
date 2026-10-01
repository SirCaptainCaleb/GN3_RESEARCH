# Every clean degree-two sharp-shell corridor exposes ordered support complexity

## Statement

Let H be a minimum counterexample in the sharp half-order shell and let S_0-S_1-S_2-S_3 be a simple four-support path in the Hamiltonian-support odd graph. Assume both constituent length-two walks take the clean alternative of astra004twowalk. Then the corridor necessarily exposes one of the following concrete witnesses: (i) an explicit reverse cross-bridge through the middle omitted label b between the near-end vertices of S_1 and S_2; (ii) a proper tight five-path W meeting both middle components such that, for arbitrary exact covers of the two endpoint deletions of W, either one has at least two ordinary edges between W minus its deleted endpoint and H-W, or an endpoint cover disagrees in relative order with W, or after deleting both endpoints the two induced exact covers have different support partitions or different Hamilton orders on a common support. In particular a clean degree-two corridor cannot remain support-and-order featureless.

## Body

# Proof

By astra004corridordouble, the middle deletion cover H-b=S_1|S_2 is double-clean. If the two clean endpoint replacements use opposite side types, that theorem directly gives the reverse cross-bridge, which is (i).

Assume the replacements use the same side type. By astra004samefive, either the same explicit reverse cross-bridge occurs, or there is a proper tight Hamilton five-path W on the two replaced endpoints, their adjacent middle-component vertices, and b; moreover H-W is non-Hamiltonian with path-cover number two.

Apply the certified five-path endpoint-deletion theorem contained in transport01 to this proper tight five-path W. It states that arbitrary exact covers at the two endpoints of W satisfy exactly the alternatives listed in (ii): at least two W/complement crossings, inherited-order disagreement, or disagreement of the induced common two-deletion covers at support or order level. Hence the five-window branch is also non-featureless. ∎
