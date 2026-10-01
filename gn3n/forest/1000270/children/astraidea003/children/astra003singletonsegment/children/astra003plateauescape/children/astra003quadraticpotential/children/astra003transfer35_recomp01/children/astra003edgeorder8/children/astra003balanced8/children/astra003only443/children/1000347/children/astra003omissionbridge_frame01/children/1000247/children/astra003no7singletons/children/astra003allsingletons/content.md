# Every label occurs on the omission surface of a trapped order-eleven Astra component

## Statement

Let K be a trapped order-eleven Astra-003 component containing a 4|4|3 state, and let S be the set of labels occurring as singletons of reachable 5|5|1 states. Then S=V(H). Equivalently, all eleven vertex labels occur as singleton labels in the same Astra component.

## Body

By astra003no7singletons, |S|>=8. Put T=V(H)-S. We exclude |S|=8,9,10. Throughout, use the certified order-eleven omission theorem from 2ac31d8f3bb6: in every reachable 5|5|1 state P|Q|(x), each five-side supplies at least three reversible omission swaps. Since labels in T never occur as singletons, every T-label on a side is a bad deletion of the corresponding six-set side union {x}.

A basic connectivity observation will be used repeatedly.

For a fixed support A on one labeled side, the possible singleton labels form a finite graph whose edges are reversible omission swaps through the opposite side. If that graph has minimum degree at least d, then every connected component has at least d+1 vertices. Hence:
- minimum degree at least 3 on five vertices forces connectivity;
- minimum degree at least 3 on six vertices also forces connectivity, since two components would each have at least four vertices.

Likewise, when a fixed six-set consists of one side plus the singleton, swaps through that side give a graph on the possible singleton positions inside the fixed S-part.

## Case |S|=8

Now |T|=3. Every five-side contains at least three S-labels, so in every omission state the T-labels split 2+1 across the two sides. Fix a state and label the two-T side

P=A union U,

with |A|=3 and |U|=2; write the singleton as x in S.

The two labels of U are bad deletions of P union {x}. Four-of-six therefore forces all four S-labels A union {x} to be good. Thus every swap of x with a vertex of A is available, and the T-pair U remains fixed.

On the opposite side there is one T-label and four S-labels. That T-label is bad, so four-of-six gives at least three good swaps among the four side-S-labels. For fixed A, the graph on the five choices of singleton in S-A therefore has minimum degree at least three and is connected.

Hence, with U fixed, every three-subset A' of S can occur on the U-side: choose any desired y outside the current A as singleton using the connected opposite-side fiber, then swap y with any desired a in A on the U-side. Johnson connectivity finishes the claim.

Therefore for every four-subset W of S, the six-set U union W occurs as U plus a three-side support and a singleton. Both members of U are bad deletions. Consequently, for every u in U and every four-subset W of S, the five-set

W union {u}

is non-Hamiltonian.

Fix u in U and any five-subset Z of S. Then in the six-set Z union {u}, deleting any z in Z leaves a non-Hamiltonian five-set. Thus there are at least five bad deletions, contradicting four-of-six. Hence |S| is not eight.

## Case |S|=9

Now |T|=2.

If some reachable state places both T-labels on the same five-side, the preceding |S|=8 argument applies verbatim to that fixed T-pair. The opposite side now has five S-labels; its singleton-choice fiber has six vertices and minimum degree at least three, hence is connected. We again obtain that u plus every four-subset of S is non-Hamiltonian for u in T, contradicting four-of-six on u plus any five-subset of S.

Thus in every reachable state the two T-labels are split 1+1. Fix their assignment to the two labeled sides and write

P=A union {t},

where A is a four-subset of S and x is the singleton.

For the six-set P union {x}, the label t is bad. Hence among the five S-labels A union {x}, at least four are good. The swap graph on the five possible singleton positions inside the fixed five-set A union {x} therefore has minimum degree at least three and is connected.

For fixed A, the opposite side has four S-labels and one T-label. Its T-label is bad, so the graph on the five singleton choices in S-A again has minimum degree at least three and is connected.

These two connected fibers imply that every pair (A',x') with |A'|=4 and x' outside A' is reachable while preserving the assignment of t to this side: use the opposite-side fiber to choose a desired entering label, then the within-five-set fiber to move the singleton to the desired departing label. Equivalently, all four-subsets A' of S occur.

Now let W be any five-subset of S and choose x' in W, A'=W-{x'}. In the corresponding state, t is a bad deletion of the six-set {t} union W. Therefore W itself is non-Hamiltonian.

Hence every five-subset of S is non-Hamiltonian. Any six-subset of S then has six bad five-deletions, contradicting four-of-six. Thus |S| is not nine.

## Case |S|=10

Now T={t}. Fix a reachable state and label the side containing t as

P=A union {t},

with |A|=4 and singleton x in S. The opposite side consists of five S-labels.

In P union {x}, the excluded label t is bad, so at least four of the five S-labels A union {x} are good. Hence the swap graph on the five singleton positions inside A union {x} has minimum degree at least three and is connected.

For fixed A, the opposite six-set consists entirely of S-labels. Four-of-six gives at least four good deletions, one of which is the current singleton x, so at least three of the five opposite-side labels are available swaps. Thus the graph on the six choices of singleton in S-A has minimum degree at least three and is connected.

As in the previous case, these two connected fibers allow every pair (A',x') with |A'|=4 and x' outside A' while keeping t on the same side.

Given any five-subset W of S, choose x' in W and A'=W-{x'}. The corresponding six-set {t} union W has t as a bad deletion, so W is non-Hamiltonian. Hence every five-subset of S is non-Hamiltonian, again contradicting four-of-six on any six-subset of S.

Therefore |S| is not ten.

Since |S|>=8 and the cases 8,9,10 are impossible, |S|=11. Every vertex label of H occurs as the singleton of a reachable 5|5|1 state in the same trapped Astra-003 component.
