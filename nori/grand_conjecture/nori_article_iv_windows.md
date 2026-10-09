# Article IV - Window methods

# Physical window transport and cyclic parity

Let W_z(a,b,c) denote an actual ordered physical three-face of Q_n, with directions a,b,c free and other bits fixed as in z. Antipodal reversal sends W_z(a,b,c) to W_(bar z)(c,b,a) and complements its color. A consecutive pair of windows from a genuine four-edge geodesic is a physical window-shift edge; if their colors agree, the four-edge path is monochromatic.

## Exact physical two-step shuttles

Fix a direction i and restrict to the window-shift graph H_i in which i belongs to the common middle directions of every shift. For pairwise distinct a,b,d,i,k, the sequence

W_z(a,i,b), W_z(i,b,k), W_(z xor e_k)(d,i,b)

is a genuine two-edge path in H_i. The shared middle face has free directions i,b,k, so replacing its representative by one differing only in k does not change the physical face. The shuttle exchanges an outer free direction and flips a chosen exterior coordinate. Variants perform the same outer exchange without that flip.

By iterating these moves, each actual window can be connected to its antipodal reversed window through an even-length H_i path linear in n. In the optimal transport theorem, the minimum length is max(6,2 ceil((n-1)/2)), for n>=5. The construction accounts separately for the exterior bits to be complemented and the exchange of outer ordered directions.

## Forced monochromatic connectors

An even-length path from v to its antipodal reverse has oppositely colored endpoints. If every shift changed color, even parity would force equal endpoint colors, a contradiction. Hence at least one edge along each such antipodal transport path is monochromatic, meaning its two ordered three-face windows agree.

Let E_0=2^(n-2)(n-1)(n-2)(n-3), the number of edges in each middle-orientation orbit under root translations and permutations fixing i. Averaging translates of an optimal antipodal path of length L gives a lower bound of 2 ceil(E_0/L) for the total monochromatic H_i connector edges, with the two orientation classes equally represented by antipodal reversal. This forces exponentially many actual local connectors, yet their roots and direction supports may differ.

## Cyclic seams and the global limitation

Cyclic window-shift structures have odd cycles and associated parity/monodromy constraints. They provide complementary routes to short monochromatic seeds and average bounds on the switch defects of full geodesics. The physical shuttles also exhibit literal square cycles whose diagonals are not genuine four-edge window shifts. A topological filling using those diagonals would therefore misrepresent path incidence. Adjacent permutation exchanges can move a unique equality seam across the midpoint while both full paths remain bad, so the seam side alone is not a locally constant Tucker label.

The physical transport theory supplies connected root-moving carriers and numerous certified local monochromatic windows. The global missing statement is a compatibility or gluing theorem choosing those connectors along one direction-distinct full antipodal path with at most one switch.
