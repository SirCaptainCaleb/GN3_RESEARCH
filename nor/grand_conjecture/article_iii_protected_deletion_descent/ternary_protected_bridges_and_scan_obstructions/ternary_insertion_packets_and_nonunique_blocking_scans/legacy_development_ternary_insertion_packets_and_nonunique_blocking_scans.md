# Ternary insertion packets and nonunique blocking scans — preserved pre-item development

## Development

Sources: Article II §117 and the audit 'Insertion blocking does not force the special blocker scan'. This consolidates the valid insertion calculation and a parametric obstruction.

Let alpha be alternating: cyclic rotations preserve its value, and odd permutations complement it. Let O=(v_1,...,v_m) have word 0^p1^q and let s_i=alpha(x,v_i,v_{i+1}). Inserting x after v_i replaces the relevant old windows by
(s_{i-1},1-s_i,s_{i+1}),
with the first or last entry omitted at an endpoint-adjacent gap. Earlier and later windows are unchanged.

For a vertex blocking every insertion, both phases have length at least two. If p=1, failure of prepend forces s_1=1; insertion after v_1 then gives 0,s_2 followed by an all-one suffix, a good word. The q=1 case follows by reversal. This conclusion does not require the special scan used by earlier closure attempts.

However blocking every insertion does NOT imply s=1^(p+1)0^q. For every p,q>=2, the different scan
s=11 0^(p+q-1)
blocks all gaps. Prepend and append create a return switch. The first three interior gaps give respectively
0,1,0^(p-1),1^q;
1,0^p,1^q;
and, for p>=3, 0,11,0^(p-2),1^q.
For p=2 the third word is 0,11,0,1^(q-1).
Every remaining nonterminal interior gap contains 010. At the last interior gap, the inherited final one together with its new 01 gives 101.

These data are globally coboundary-flat realizable. Use alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a). Prescribe adjacent carrier edges forward and distance-two edges equal to the desired carrier statuses. Set q_i=t(x,v_i) recursively by q_{i+1}=1 xor q_i xor s_i. This realizes every desired scan because alpha(x,v_i,v_{i+1})=1 xor q_i xor q_{i+1}. All remaining tournament edges are free, and the resulting alternating orientation has zero tetrahedral coboundary.

This disproves scan uniqueness from insertion failure; it does not give a NOR counterexample. Global counterexamplehood might impose further restrictions, but they need a separate proof. The flat closure and its two audits assumed the special scan rather than establishing it.
