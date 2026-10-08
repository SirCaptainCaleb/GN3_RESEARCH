# Exact simultaneous insertion calculus for triangle orientation and defects — preserved pre-item development

## Exact simultaneous insertion calculus for triangle orientation and defects

Use the ternary decomposition
[
h(a,b,c)=alpha(a,b,c)oplus [,b=d({a,b,c}),],
]
where (alpha) is alternating on each unordered triangle and (d) marks at most one vertex of each triangle.

Let
[
V_0=(v_1,ldots,v_m)
]
be a defect-free order, meaning that for every consecutive triple
[
(v_i,v_{i+1},v_{i+2}),
]
the marked defect vertex, if any, is not the middle vertex (v_{i+1}). Hence along (V_0), the actual NOR status equals the orientation status (alpha).

Fix a new vertex (x). For (1le i<m), define
[
s_i=alpha(x,v_i,v_{i+1}).
]

Consider inserting (x) in the interior gap between (v_i) and (v_{i+1}). The three new consecutive triples are
[
(v_{i-1},v_i,x),qquad
(v_i,x,v_{i+1}),qquad
(x,v_{i+1},v_{i+2}),
]
when the neighboring vertices exist.

By cyclic parity of an alternating triangle orientation,
[
alpha(v_{i-1},v_i,x)=alpha(x,v_{i-1},v_i)=s_{i-1},
]
[
alpha(v_i,x,v_{i+1})=1-alpha(x,v_i,v_{i+1})=1-s_i,
]
and
[
alpha(x,v_{i+1},v_{i+2})=s_{i+1}.
]

Therefore, whenever this insertion gap is defect-safe, the three new NOR statuses are exactly
[
(s_{i-1},,1-s_i,,s_{i+1}).
	ag{1}
]

Defect safety itself has an independent local description. For the unordered triangle
[
{x,v_j,v_{j+1}},
]
write its defect type as:
- (L) if the marked vertex is (v_j);
- (R) if the marked vertex is (v_{j+1});
- (X) if the marked vertex is (x);
- (N) if there is no mark.

Then the interior gap (i) is defect-safe precisely when
[
e_{i-1}
e R,qquad e_i
e X,qquad e_{i+1}
e L,
	ag{2}
]
with the evident omissions at the ends.

The defect-free Hamilton-order insertion lemma is recovered by scanning from the left: if prepending fails, then (e_1=L); if the next gap fails in the propagating way, then (e_2=L); and so on until the first non-(L) symbol, where a safe insertion occurs.

### Significance

Equations (1)--(2) isolate the exact simultaneous-ordering problem. The defect field determines which gaps are admissible; the alternating simplex orientation determines the three-bit replacement made at an admissible gap.

A full inductive proof of ternary NOR would follow from the following purely local insertion statement:

> For every defect-free one-change order and every new vertex (x), at least one defect-safe gap has orientation replacement ((s_{i-1},1-s_i,s_{i+1})) compatible with a one-change global word.

The statement is now finite and explicit. If it fails, the failure consists of a binary sign sequence (s) together with a defect-type sequence (e) for which every safe gap creates a second change. Classifying that obstruction is a concrete next closure target.
