# Central block-faithful runs have length at most three, with a double-wrap equality form

## Statement

Under the hypotheses and notation of 10cf5889ee4a, no four consecutive central indices are block-faithful. Hence every four consecutive central positions contain an index for which every exact deletion cover splits or reorders an inherited path. Moreover, if three consecutive central indices i,i+1,i+2 are block-faithful, then after naming P,Q in {B,C} so that positions i and i+2 have support pairing {L,P}|{R,Q}, the middle cover at i+1 has the forced block order Q L_{i+1} | R_{i+1} P. Thus the only length-three block-faithful run has a double-wrap middle state.

## Body

We use the support-pairing alternation and distance-two orientation forcing proved in 10cf5889ee4a.

Suppose first that four consecutive central positions i,i+1,i+2,i+3 are block-faithful. Their support pairing types alternate. Name P,Q={B,C} so that positions i and i+2 pair L with P and R with Q. Then positions i+1 and i+3 pair L with Q and R with P.

Apply the distance-two forcing to positions i and i+2. It says that in the later state i+2 the left-paired component has block order L_{i+2} P. Apply the same forcing to positions i+1 and i+3. It says that in the earlier state i+1 the right-paired component has block order P R_{i+1}.

The two tight paths L_{i+2}P and P R_{i+1} overlap exactly in the path P. Since |P|>=2, their two certified joins concatenate without creating any new consecutive triple: the sequence
L_{i+2} P R_{i+1}
is tight. The A-intervals L_{i+2}=A[0,i+1] and R_{i+1}=A[i+2,a-1] partition V(A). Hence this is a Hamilton path on V(A) union V(P). The untouched path Q is disjoint from it, so together they form a spanning two-cover of H, contradiction. Therefore no four consecutive central positions are block-faithful.

Now suppose exactly three consecutive positions i,i+1,i+2 are block-faithful, and name P,Q so that the endpoint states i,i+2 pair L with P and R with Q. By distance-two forcing, the earlier endpoint state i has right component Q R_i, while the later endpoint state i+2 has left component L_{i+2} P. The middle state has the opposite support pairing: L_{i+1} with Q, and R_{i+1} with P.

If its left component had block order L_{i+1}Q, then L_{i+1}Q and Q R_i would concatenate through Q, whose order is at least two, to give the tight Hamilton path L_{i+1} Q R_i on A union Q; together with P this two-covers H. Hence the middle left component must be Q L_{i+1}.

If its right component had block order P R_{i+1}, then L_{i+2}P and P R_{i+1} would concatenate through P to give a Hamilton path on A union P; together with Q this again two-covers H. Hence the middle right component must be R_{i+1}P.

Thus the middle deletion cover is forced to have the double-wrap form Q L_{i+1} | R_{i+1} P. This proves both assertions.
