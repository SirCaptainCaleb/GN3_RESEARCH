# Edge-orderable trapped minima with a three-side reduce to 4|4|3 at order eleven

## Statement

Let H be an edge-orderable minimum counterexample, and let A|B|C be a Phi-minimal spanning three-cover in a trapped Astra-003 component, with |A|>=|B|>=|C|. If |C|=3, then |V(H)|=11 and the component-order multiset is {4,4,3}. Consequently, for every edge-orderable minimum counterexample of order at least 12, every Phi-minimal trapped Astra-003 three-cover has all component orders at least four.

## Body

# Edge-orderable small-side reduction

Let H be an edge-orderable minimum counterexample and let A|B|C be Phi-minimal in a trapped Astra-003 component, with a=|A|>=b=|B|>=c=|C|=3.

By the certified three-side closure theorem astra003close3side, every component paired with a three-side has order at most five. Hence a,b<=5.

If a=5, then A union C is an induced eight-vertex edge-orderable boundary tournament. By astra003edgeorder8 it has an exact 4|4 two-cover. Replacing A|C by that cover lowers their quadratic contribution from 25+9=34 to 16+16=32, contradicting Phi-minimality. Therefore a<=4, and hence b<=4.

A minimum counterexample has order greater than ten. Since n=a+b+3 and a,b<=4, we have n<=11. Thus n=11 and necessarily a=b=4.

Therefore the only possible Phi-minimal trapped state with a three-vertex component in the edge-orderable subclass is 4|4|3 on eleven vertices. In particular, for n>=12 the minimum component order is at least four.
