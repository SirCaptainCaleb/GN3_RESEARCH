# Two fully curved predecessor choices fail only under consecutive defect marks

## Metadata

- ID: two_fully_curved_predecessor_choices_fail_only_under_consecutive_defect_marks
- Parent Section: directed_nor_union_closed_bridge
- Position: 78
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Retain the setting of Subsection 76: Q={a,b,c,d} is fully curved for the alternating orientation alpha, but now the actual label h may have defects, with h(p,q,r)=alpha(p,q,r) xor 1_{d({p,q,r})=q}. Fix a suffix beginning (c,d,v,...) that is monochromatic for h, with color z=h(c,d,v). Consider the two possible orders obtained by prepending (a,b) or (b,a). Put s=alpha(b,c,d). Full curvature gives alpha(a,b,c)=1-s, alpha(b,a,c)=s, and alpha(a,c,d)=1-s.

Each prepending operation adds two statuses before the constant z suffix. It fails NOR precisely when those two added statuses are (z,1-z). Consequently both operations fail if and only if one of the following mutually exclusive configurations holds:

(1) z=s, the defect of {a,b,c} is b, the defect of {b,c,d} is c, and the defect of {a,c,d} is not c.

(2) z=1-s, the defect of {a,b,c} is a, the defect of {a,c,d} is c, and the defect of {b,c,d} is not c.

Proof. Write A=1_{d(abc)=b}, A'=1_{d(abc)=a}, B=1_{d(bcd)=c}, B'=1_{d(acd)=c}. The two added words are (1-s xor A, s xor B) and (s xor A',1-s xor B'). To make both equal (z,1-z), solve the four displayed binary equalities. If z=s they give A=1,A'=0,B=1,B'=0. If z=1-s they give A=0,A'=1,B=0,B'=1. The shared triangle abc has at most one marked vertex, so these solutions are precisely the two configurations stated.

In particular, if the shared triangle abc is coherent or marked at c, the first added statuses of the two orders are opposite. One is therefore different from z, and that entire three-status entry word has at most one change regardless of its middle status. Thus at least one prepending choice succeeds. The pure-orientation extension in Subsection 76 is a special case.

Labeling interpretation. For a prescribed suffix state (c,d,z), the two predecessor choices a and b can be labeled by actual extension success. A fully curved packet never blocks both labels unless the defect field marks consecutive centers along one of the two prefix orders, with the additional stated condition on the other triangle. This identifies the precise defect data that must accompany the curvature predecessor label. It is an actual local extension theorem and complete description of its failure, not a claim that a connector prevents these configurations globally.

## Development

Retain the setting of Subsection 76: Q={a,b,c,d} is fully curved for the alternating orientation alpha, but now the actual label h may have defects, with h(p,q,r)=alpha(p,q,r) xor 1_{d({p,q,r})=q}. Fix a suffix beginning (c,d,v,...) that is monochromatic for h, with color z=h(c,d,v). Consider the two possible orders obtained by prepending (a,b) or (b,a). Put s=alpha(b,c,d). Full curvature gives alpha(a,b,c)=1-s, alpha(b,a,c)=s, and alpha(a,c,d)=1-s.

Each prepending operation adds two statuses before the constant z suffix. It fails NOR precisely when those two added statuses are (z,1-z). Consequently both operations fail if and only if one of the following mutually exclusive configurations holds:

(1) z=s, the defect of {a,b,c} is b, the defect of {b,c,d} is c, and the defect of {a,c,d} is not c.

(2) z=1-s, the defect of {a,b,c} is a, the defect of {a,c,d} is c, and the defect of {b,c,d} is not c.

Proof. Write A=1_{d(abc)=b}, A'=1_{d(abc)=a}, B=1_{d(bcd)=c}, B'=1_{d(acd)=c}. The two added words are (1-s xor A, s xor B) and (s xor A',1-s xor B'). To make both equal (z,1-z), solve the four displayed binary equalities. If z=s they give A=1,A'=0,B=1,B'=0. If z=1-s they give A=0,A'=1,B=0,B'=1. The shared triangle abc has at most one marked vertex, so these solutions are precisely the two configurations stated.

In particular, if the shared triangle abc is coherent or marked at c, the first added statuses of the two orders are opposite. One is therefore different from z, and that entire three-status entry word has at most one change regardless of its middle status. Thus at least one prepending choice succeeds. The pure-orientation extension in Subsection 76 is a special case.

Labeling interpretation. For a prescribed suffix state (c,d,z), the two predecessor choices a and b can be labeled by actual extension success. A fully curved packet never blocks both labels unless the defect field marks consecutive centers along one of the two prefix orders, with the additional stated condition on the other triangle. This identifies the precise defect data that must accompany the curvature predecessor label. It is an actual local extension theorem and complete description of its failure, not a claim that a connector prevents these configurations globally.
