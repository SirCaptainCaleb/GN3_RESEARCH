# The reciprocal all-equal residue is multiply crossed or a clean three-edge exchange

## Statement

In the reciprocal-crossing branch of the all-equal endpoint-probe theorem 7ae7f3c03f16, fix the endpoint deletion cover T and the inherited three-path cover J of H-d. Let t count T-edges crossing the three inherited classes and let s count inherited J-edges crossing the two support classes of T. Then, absent relative-order disagreement, either t>=3, or s>=2, or t=2 and s=1 and T differs from J by the clean three-edge exchange of dual_clean_exchange. Thus the only doubly sparse reciprocal residue is one inherited edge deleted and two cross-class edges inserted.

## Body

The reciprocal-crossing hypothesis gives s>=1. Since one inherited class meets both T-components, cutting T at its t cross-class edges yields at least four nonempty inherited-class blocks: at least two from the split class and at least one from each other class. Because T has two components, the crossing/block identity gives t=(number of blocks)-2>=2. Hence if t is not at least three and s is not at least two, necessarily t=2 and s=1. The hypotheses of dual_clean_exchange then hold and give the stated clean forest exchange.