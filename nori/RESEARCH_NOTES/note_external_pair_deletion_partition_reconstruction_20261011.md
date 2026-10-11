# Archive: two-deletion reconstruction of ordered-block partitions

- Stable ID: note_external_pair_deletion_partition_reconstruction_20261011
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: historical_scope, archive
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r5005_1
- Updated session: session_nori_r5005_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Self-contained combinatorial lemma inherited from an earlier project. No transfer to the present unrestricted NORI1 or all-boundary-tournament goals is known. Pending export to a general combinatorial toolkit; the original versioned Toolkit record remains archived.

## Original Toolkit source: pairdeletionreconstruct01

Because R and S are distinct, some unordered pair {u,v} has different pair state in the two structures.

If x is any vertex outside {u,v}, then the pair {u,v} survives in W-{x} with its pair state unchanged in each restriction. Hence the two restrictions to W-{x} still disagree. Therefore every x in Z belongs to {u,v}, proving |Z|<=2.

Now suppose Z contains two distinct vertices x,y. Let {a,b} be any unordered pair different from {x,y}. At least one of x,y is not in {a,b}; call that vertex z. Since z belongs to Z, the restrictions of R and S to W-{z} have identical pair states. The pair {a,b} survives that restriction, so R and S give it the same pair state.

Thus every pair except possibly {x,y} has the same state in R and S. Since R and S are distinct, {x,y} must indeed be their unique disagreeing pair. ∎
