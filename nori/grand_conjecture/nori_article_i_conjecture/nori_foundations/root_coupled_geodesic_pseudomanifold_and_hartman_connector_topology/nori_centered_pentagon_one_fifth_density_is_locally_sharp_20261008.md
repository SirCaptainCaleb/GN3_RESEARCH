# The centered five-cycle 1/5 monochromatic connector bound is sharp even inside active NORI

SHARPNESS OF THE UNIVERSAL CENTERED-PENTAGON DENSITY. Fix an arbitrary cube vertex z and five distinct directions W={0,1,2,3,4}. Assign binary labels to the 60 ordered 3-tuples (a,b,c) of distinct elements of W in lexicographic order (a increasing, then b increasing excluding a, then c increasing excluding a,b) via the five 12-bit rows, one per first coordinate a:
  a=0: 111000000000
  a=1: 111000001001
  a=2: 011000111001
  a=3: 011011111000
  a=4: 111111111010
For each ordered triple use this bit as the color of the actual physical three-face through z whose free directions are exactly {a,b,c}, in order (a,b,c). A direct count over the 5*4*3*2=120 ordered distinct 4-tuples (a,b,c,d) gives EXACTLY 24 with f(a,b,c)=f(b,c,d). Thus precisely 1/5 of centered four-edge geodesics using W have their two successive ordered-three-face windows equal. Each of the 24 directed pentagon classes must contain an odd number of good shifts, at least one, so equality of total count 24 moreover implies EXACTLY ONE marked monochromatic shift in every one of these pentagons.
The local table is realizable in a GLOBAL coloring satisfying active NORI antipodal-reversal oddness: these 60 ordered faces all contain z, while their antipodal ordered-reversal mates have the same free triples but exterior bits complemented (the two exterior bits differ for a five-face). Therefore no selected face equals the antipodal-reversal mate of another selected face. Assign each mate its complementary color, and assign every remaining involution orbit arbitrarily. This preserves all specified hub colors and defines an honest full NORI coloring in every n>=5, extending to any ambient extra exterior bits.
Hence the >=1/5 centered seed density theorem is OPTIMAL when only the vertex-centered five-cycle constraints are used. A better NORI global switch bound or grand closure must exploit correlations between DIFFERENT hub vertices, different five-sets, and/or the antipodal-reversed terminal-memory reachability basins. Verifier: enumerate permutations(a,b,c,d) in W and count f(a,b,c)==f(b,c,d); the count is 24.
