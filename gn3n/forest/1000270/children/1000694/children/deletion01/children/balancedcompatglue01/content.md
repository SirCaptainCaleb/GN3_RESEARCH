# Compatible balanced deletion covers have a parity-determined global size profile

## Statement

Let H have n vertices and let D be a set of at least four deletion labels. For each d in D choose a balanced two-cover F_d of H-d, and suppose these covers are pairwise compatible. Then they glue to a global two-cover A|B. If n=2k+1, the global component orders are k+1 and k. If n=2k, then either the global component orders are k and k, or they are k+1 and k-1; in the latter case every label in D lies in the (k+1)-vertex component.

## Body

By the certified four-cover compatibility gluing theorem, the pairwise compatible family has a global two-cover A|B whose restriction to H-d is F_d for every d in D. Write a=|A| and b=|B|.

If d lies in A, the restricted component-order multiset is {a-1,b}; if d lies in B, it is {a,b-1}.

For n=2k+1, every balanced cover of H-d has sizes k|k. Hence either restriction equation forces the global sizes to be k+1 and k.

For n=2k, every balanced cover of H-d has sizes k and k-1. If d lies in A, {a-1,b}={k,k-1}, so either {a,b}={k,k} or, after naming A as the larger side, (a,b)=(k+1,k-1). In the unbalanced case a label e in B would restrict the global cover to sizes k+1 and k-2, not balanced. Hence every d in D lies in the larger component.

This strips the minimum balanced-counterexample hypothesis from astra002compatparity02. The contradiction and K4-free consequences in that route arise only after adding the line-specific assumption that H itself has no balanced two-cover.
