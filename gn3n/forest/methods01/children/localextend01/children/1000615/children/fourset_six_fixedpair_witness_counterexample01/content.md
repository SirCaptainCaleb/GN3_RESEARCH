# A four-set can have all six same-class fixed-pair witnesses

## Statement

There exists a boundary tournament on four vertices in which, for every one of the six unordered vertex pairs, the complementary two vertices lie in the same fixed-pair orientation class. Thus the universal upper bound of four asserted in fourset_fixedpair_witness_bound01 is false; the trivial upper bound six is sharp.

## Body

Let V={1,2,3,4}. For each unordered endpoint pair {i,j}, write i<j and let {k,l}=V-{i,j}. Declare both ordered triples (i,k,j) and (i,l,j) tight. Their boundary flips (j,k,i) and (j,l,i) are therefore non-tight. These declarations concern twelve distinct boundary-flip pairs: a boundary-flip pair is determined by its middle vertex together with its unordered endpoint pair, and there are 4*C(3,2)=12 such pairs on four vertices. Hence the declarations specify exactly one member of every boundary-flip pair and define a boundary tournament.

Now fix any unordered pair {i,j}, with i<j. Its complementary vertices k and l both satisfy (i,k,j) and (i,l,j) tight, so both belong to the same fixed-pair orientation class C_+ relative to the ordered endpoints (i,j). Therefore {i,j} is a same-class fixed-pair witness. This holds for all six unordered pairs, so the four-set has six witnesses.
