# Exact six-direction hub coloring blocks every monochromatic three-window continuation

FINITE OBSTRUCTION TO OVERSTRENGTHENING THE CENTERED FIVE-CYCLE. The guaranteed centered four-edge mono two-window connector CANNOT in general be strengthened to a centered five-edge mono THREE-window connector using only the binary labels of ordered triples at one prescribed hub z on a fixed six-direction set. This is already false for an arbitrary vertex-local table of ordered-triple colors, and such a table is locally compatible with the global NORI antipodal-reversal axiom (the axiom constrains the antipodal physical face at bar z, not the reversed triple at the same z).
EXPLICIT CERTIFICATE. Index six directions as 0,1,2,3,4,5. For a in ascending order, b runs ascending through [0..5] except a, and for each (a,b), c runs ascending through [0..5] except a,b. Assign the 120 ordered-triple colors from six successive 20-bit rows:
  a=0: 11001110110011111111
  a=1: 00000000110011111111
  a=2: 11011100110011111111
  a=3: 00001100000011111111
  a=4: 00001100000010100000
  a=5: 00001100000010100000
There are exactly 6*5*4=120 ordered triples and 6*5*4*3*2=720 ordered five-tuples of distinct directions. Direct exhaustive substitution in the table shows for every distinct (a,b,c,d,e), the three bits f(a,b,c), f(b,c,d), f(c,d,e) are NEVER all equal. Thus a monochromatic center-z five-edge ordered-three-face geodesic cannot be forced by an arbitrary six-direction hub labeling.
SELF-CONTAINED VERIFIER (Python syntax):
B=['11001110110011111111','00000000110011111111','11011100110011111111','00001100000011111111','00001100000010100000','00001100000010100000']
def f(a,b,c):
    bs=[x for x in range(6) if x!=a]
    cs=[x for x in range(6) if x not in (a,b)]
    return int(B[a][4*bs.index(b)+cs.index(c)])
from itertools import permutations
assert all(len({f(a,b,c),f(b,c,d),f(c,d,e)})==2 for a,b,c,d,e in permutations(range(6),5))
The certificate demonstrates a precise limitation of purely hub-local extension from length four to five. It does not refute NORI, because globally a full six-edge one-switch path might exist through a different alignment or an external root exchange. It strengthens the motivation for root-coupled five-cycle overlap, antipodal compatibility, and the two-window seam extraction rather than an automatic greedy hub-local absorption.
