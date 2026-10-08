# Minimum ternary counterexamples have exactly one threshold defect — preserved pre-item development

## Composition

(none yet)

## Development

## Minimum counterexamples have threshold defect one

Work in ternary arity and assume a minimum counterexample on n coordinates. For a full coordinate order pi, a cut k and polarity eta, let B(pi,k,eta) be the length of the maximal contiguous interval of linear ternary-window ranks containing the cut on which the actual word agrees with the one-change threshold target. A full order has n-2 linear windows.

Delete any vertex x. By minimum counterexamplehood, the induced problem on V\{x} has a spanning one-change order O on n-1 coordinates. Its linear ternary word has n-3 windows and agrees exactly with some threshold target.

Append x to O (or prepend it). The old n-3 windows are unchanged. Extend the same threshold target across the one new endpoint window in the evident way. Therefore the resulting full order has a target-compatible contiguous band of length at least n-3. Hence
B_max >= n-3.

If B_max=n-2, all windows of some full order agree with a one-change target and NOR is solved. Therefore in a minimum counterexample
B_max = n-3.

### Endpoint-defect normal form
Choose a B-maximal bad switch state. Since there are n-2 linear window ranks and the matched band has length n-3, exactly one rank lies outside the band.

That rank must be an endpoint rank. If the unique unmatched rank were interior, deleting it would separate the linear window ranks into two components, and no contiguous matched band could contain n-3 ranks: the largest component has at most n-4 ranks.

Thus, after reversal if necessary, every minimum counterexample has a full coordinate order whose word differs from a one-change threshold word at exactly the first window and nowhere else.

Write the threshold target as
eta^p (1-eta)^q.
The first rank must lie in the eta-run. Since it is mismatched, the actual word is
(1-eta), eta^(p-1), (1-eta)^q.
If p=1, this word is monochromatic (1-eta), so NOR is solved. Therefore p>=2, and the actual full word has exactly two changes with a singleton initial run:
(1-eta) | eta^(p-1) | (1-eta)^q.

So a minimum counterexample admits an endpoint-singleton two-change order. Equivalently, deleting its first coordinate yields a genuine one-change order, while reinserting that coordinate at the endpoint creates the unique extra return switch.

### Strategic consequence
The globally maximal threshold-band obstruction is not an arbitrary central band between two remote curvature barriers. In a minimum counterexample it is a codimension-one endpoint defect. All flat-sector barrier analysis can therefore be specialized to the first few windows next to this singleton endpoint defect. In the coboundary-flat sector, global B-maximality forces the tetrahedron at the unique unresolved boundary to be fully curved by subsection 153.

This should be combined with endpoint blocking / perfect-blocker scan structure rather than continuing a fully general two-barrier analysis.
