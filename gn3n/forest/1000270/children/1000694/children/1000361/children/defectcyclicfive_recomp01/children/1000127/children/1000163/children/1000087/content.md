# Every three-cover with long components has barriers in both cyclic orientations whenever path-cover number exceeds two

## Statement

Let H be any boundary tournament with pc(H)>2 and let A|B|C be a three-cover with |A|,|B|,|C|>=3. For an ordered interface X|Y, call it a barrier when both join triples needed to concatenate X followed by Y are non-tight. Each of the two cyclic orientations A->B->C->A and A->C->B->A contains a barrier. Consequently there are two directed barrier interfaces, one from each orientation cycle; after relabeling they are opposite orientations of one unordered pair, share a source, or share a target.

## Body

Consider the cyclic orientation A->B->C->A. At any interface, the two join triples cannot both be tight, because then the two adjacent displayed paths concatenate and, together with the third path, give a two-cover of H. Suppose this cyclic orientation had no barrier. Then every one of its three interfaces has exactly one non-tight join triple. Since all three displayed paths have order at least three, these three defects are separated around the cyclic order by tight internal triples. The cyclic defect graph therefore has run type {1,1,1}. Cutting the cyclic order at an internal tight location gives a spanning ordering of defect span three with the same three isolated cyclic defects, contradicting 33b80d34aad4. Hence this orientation contains a barrier.

The same argument applied to A->C->B->A gives a barrier in the reverse orientation cycle. The two directed edge sets are disjoint; any choice of one directed edge from each has, after relabeling, one of the three stated incidence types.
