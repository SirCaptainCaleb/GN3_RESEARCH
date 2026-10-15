# Rank-three convex obstruction in ordinary boundary tournaments

### Rank-three convex obstruction for unrestricted boundary tournaments

**Theorem.** For every integer n>=6, there is a reversal-odd binary coloring b of all ordered distinct triples, and a three-dimensional dual type-A Coxeter cell D, such that every Hamilton order in D has at least two triple-color switches, yet the convex hull of their first/last-switch bivectors contains zero. Two nonzero labels are negatives.

*Construction and proof.* For n=6 take D to be the 24 permutations (a,b,c,d,4,5), with (a,b,c,d) ranging over the four-element set {0,1,2,3}. This is the rank-three residue corresponding to the ordered partition {0,1,2,3}|{4}|{5}. Specify b(a,h,c) with a<c using these rows, indexed by h; the ten entries in each row follow lexicographic order on pairs {a,c} excluding h:
[
egin{array}{c|c}
h&	ext{ten bits}\hline
0&1000000000\
1&0010010100\
2&0000100000\
3&0110110100\
4&0001000010\
5&0000000000
end{array}
]
Define b(c,h,a)=1-b(a,h,c). The full four-bit words of these 24 complete Hamilton paths are:
[
egin{array}{c|c@{quad}c|c@{quad}c|c@{quad}c|c}
abcd&w&abcd&w&abcd&w&abcd&w\hline
0123&0110&0132&0101&0213&0010&0231&0010\
0312&0101&0321&1010&1023&1010&1032&0101\
1203&1010&1230&1001&1302&1101&1320&1101\
2013&0010&2031&0010&2103&1010&2130&0101\
2301&0110&2310&0101&3012&1001&3021&1010\
3102&1101&3120&1101&3201&1010&3210&0101
end{array}
]
Every word is among {0010,0101,0110,1001,1010,1101}, all having two or three switches. The orders pi=(0,1,2,3,4,5) and pi'=(2,3,0,1,4,5) both have word 0110; their first/last switch positions are 1 and 3. Define centered prefixes Z_j(pi)=sum_{h<=j}e_{pi_h}-(j/n)1. Their extreme-switch bivectors are E(pi)=Z_2(pi) wedge Z_4(pi) and E(pi')=Z_2(pi') wedge Z_4(pi'). As the first four symbols agree as a set, and the first two symbols are complementary within that set, Z_4(pi')=Z_4(pi) and Z_2(pi')=Z_4(pi)-Z_2(pi). Therefore
[
oxed{E(pi')=-E(pi)
e0,quad (E(pi)+E(pi'))/2=0.}
]
The bivectors are nonzero because centered prefix vectors of distinct ranks are linearly independent.

For n>6 append the fixed suffix 6,7,...,n-1. Keep the six-symbol coloring above, set b(j,j+1,j+2)=0 for all j>=4, and extend remaining triples arbitrarily under reversal oddness. Every four-bit word acquires a zero tail, so it retains at least its existing two switches. The two special words are 011 followed by n-5 zeros, retaining switches at 1 and 3 and the same centered-prefix wedge identity. This proves the theorem for all n>=6.

**Consequences.** The theorem shows that convex hull avoidance on every rank-two residue, established previously for unrestricted reversal-odd boundary tournaments, cannot be extended to rank-three residues using only reversal oddness and the absence of a favorable flag. Barycentric affine filling of the switch-wedge labels fails on D. The construction concerns only one residue; favorable full Hamilton orders can exist elsewhere. It does not refute the original conjecture. It does not rule out a nonconvex continuous filling: the target of nonzero bivectors has the homotopy type of S^{binomial(n-1,2)-1}, whose second homotopy group is zero for n>=6.
