# Q9 certified obstruction: opposite Tucker median signs, same middle cut, and all four splice paths have three changes

# An explicit actual Q9 obstruction to automatic one-switch extraction from a near-middle Tucker pair

Fix Q9 directions indexed 0,1,...,8 and full path root x=0. Consider these two full geodesic direction words
  P=(0,1,2,3 | 4,5,6,7,8),
  Q=(1,2,3,0 | 5,7,6,8,4),
with a common used-coordinate support S={0,1,2,3} at rank FOUR, and the two hybrid full direction orders P_left Q_right and Q_left P_right. Thus all four real geodesics pass through the same PHYSICAL cube vertex y=e0+e1+e2+e3 after four edges. The cut has four edges before it and five after it, exactly in the near-midpoint interval k=floor((9-2)/2)=3 of the new Tucker theorem.

There is a globally valid active NORI ordered-three-face coloring c satisfying c(bar F, reverse pi)=1-c(F,pi) for which the genuine 7-window words along the four actual full geodesics are, respectively:
  P:              0010001 (3 switches: positions 2,3,6; median 3 LEFT of center 3.5),
  Q:              0011011 (3 switches: positions 2,4,5; median 4 RIGHT of center 3.5),
  P_left Q_right: 0010011 (3 switches: positions 2,3,5),
  Q_left P_right: 0001001 (3 switches: positions 3,4,6).
Every word has OPPOSED endpoint colors (first0,last1). In particular P and Q have OPPOSITE binary signed Tucker median-side labels, BOTH already have the MINIMAL possible BAD number of changes (three), and neither of the TWO prefix/suffix hybrid exchanges improves on that minimal bad defect. Thus mere actual common near-middle cube vertex plus opposite Tucker median labels, EVEN TOGETHER WITH MINIMAL BAD DEFECT ON BOTH ORIGINAL PATHS, does NOT imply grand one-switch closure by choosing among these four paths.

EXPLICIT PHYSICAL FACE CERTIFICATE: The table below assigns a binary color to each ordered physical 3-face occurring among the four paths. Represent a physical 3-face by (ordered free direction triple; exterior-one-bit mask in decimal). Coordinates and masks are 0-based, the physical face has all remaining free-coordinate bits unconstrained.
(0,1,2;0)=0; (1,2,3;1)=0; (2,3,4;3)=1; (3,4,5;7)=0; (4,5,6;15)=0; (5,6,7;31)=0; (6,7,8;63)=1;
(1,2,3;0)=0; (2,3,0;2)=0; (3,0,5;6)=1; (0,5,7;14)=1; (5,7,6;15)=0; (7,6,8;47)=1; (6,8,4;175)=1;
(2,3,5;3)=1; (3,5,7;7)=0; (3,0,4;6)=0; (0,4,5;14)=1.
These 18 ordered-face objects are distinct, and none is the active NORI involutive partner of another in the list. An involutive partner of (a,b,c;mask) is (c,b,a;mask XOR ([9] minus {a,b,c})) where the complement is on all six FIXED exterior coordinates. Hence these independent assignments extend to a TOTAL active NORI coloring of all ordered physical three-faces by arbitrarily assigning one bit per remaining involution orbit and assigning the complementary bit to its antipodal-reversal partner. Direct evaluation of the four words against the listed physical face data gives precisely the four 7-bit words above. Thus the example involves honest physical ordered faces and globally extendible NORI oddness, not a formal sign sequence unrooted in the cube.

SCOPE. The completed global active NORI coloring may possess OTHER one-switch antipodal geodesics. This is NOT a counterexample to the NORI grand conjecture. It is an exact counterexample to the LOCAL inference that the genuine binary-median Tucker complementary pair plus a near-middle shared prefix support and even both paths having 3 switches necessarily makes one of its four prefix-suffix exchanges good. To complete unrestricted NORI, topology must impose ADDED information from a whole cell, root-square packet, or extra simultaneous path witnesses that goes beyond the mere existence of this pair.
