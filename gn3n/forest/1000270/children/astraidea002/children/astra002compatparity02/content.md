# Compatible balanced deletion covers glue to a balanced cover in odd order

## Statement

Let H be a minimum-order counterexample to the balanced two-cover conjecture, and for labels d in D choose balanced two-covers F_d of H-d that are pairwise fully compatible, with |D|>=4. The certified compatibility gluing theorem produces a global two-cover A|B whose restriction to H-d is F_d for every d in D. If |V(H)|=2k+1 is odd, this is impossible: every F_d has sizes k|k, forcing A|B to have sizes k+1 and k, hence balanced. If |V(H)|=2k is even, the only possible unbalanced glued size vector is (k+1,k-1), and then every deletion label in D must lie in the (k+1)-vertex component. In particular, for odd order the compatibility graph of any chosen balanced deletion covers is K4-free.

## Body

# Proof

Let the pairwise compatible deletion covers be F_d for d in D, with |D|>=4. By the certified compatibility gluing theorem, there is a global two-cover A|B of H whose restriction to H-d agrees with F_d for every d in D.

Write a=|A|, b=|B|, with a+b=n.

For a label d in A, the restriction has component-size multiset {a-1,b}; for d in B it has multiset {a,b-1}.

Because every F_d is balanced for H-d, these multisets are prescribed by parity.

## Odd order

Let n=2k+1. Then n-1=2k, so every balanced deletion cover has sizes k|k.

If d lies in A, then

{a-1,b}={k,k},

hence a=k+1 and b=k. If d lies in B, symmetrically {a,b-1}={k,k}, again giving the global size multiset {k+1,k}.

Thus the glued global cover is balanced, contradicting that H is a counterexample to the balanced two-cover conjecture.

Therefore no four balanced deletion covers can be pairwise compatible. Equivalently, any compatibility graph formed from one chosen balanced deletion cover per label is K4-free.

## Even order

Let n=2k. Then n-1=2k-1, so every balanced deletion cover has sizes k and k-1.

Suppose d lies in A. The equation

{a-1,b}={k,k-1}

has two possibilities:

(a,b)=(k+1,k-1)

or

(a,b)=(k,k).

The second is already a balanced global cover and is impossible in a counterexample. Hence if d lies in A, the only surviving global size vector is (k+1,k-1) with A the larger side.

If instead some deletion label e in D lies in B, then its restriction has sizes {k+1,k-2}, which is not balanced. Therefore in the unbalanced surviving case every label of D lies in the same larger (k+1)-vertex component.

So even-order compatible families are not forbidden outright, but they are globally localized: every label in the family must belong to the larger side of one fixed (k+1)|(k-1) two-cover.

This gives a parity-sensitive compatibility interface for Astra-002.
