# A one-band-per-face Sperner carrier yields a witnessed macro-root closing path

## Metadata

- ID: a_one_band_per_face_sperner_carrier_yields_a_witnessed_macro_root_closing_path
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 156
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A one-band-per-face Sperner carrier yields a witnessed macro-root closing path

Continue with the consecutive-change defect of root §155.

For every proper ordered-partition face

F=B_1|...|B_s,

choose one block-good witness order pi_F by concatenating arbitrary NOR-good orders on the proper blocks B_j.

Because the ambient instance is bad, pi_F has at least two changes. Root §155 proves that EVERY consecutive-change macro root of pi_F strictly crosses F-blocks.

Choose ONE consecutive pair of changes in pi_F, say p<q, and label the face by the single macro root

r_F=e_{v_p}-e_{v_{q+3}}.

The status interval from p through q+1 is an isolated band

0 1...1 0

or

1 0...0 1.

Choose these labels antipodally: for one face from each reversal pair choose arbitrarily, and on the reversed face choose the reversed band/root. Then

r_{-F}=-r_F.

### 1. Zero-free nonzero-degree boundary carrier

Label the barycenter of every proper face F by r_F and extend affinely over the barycentric subdivision of the permutahedron boundary.

On a boundary flag

F_0<...<F_k=G,

every witness order pi_{F_i} refines G. Therefore every selected macro root is weakly forward in the G-block order:

beta_G(r_{F_i})<=0.

The largest-face label r_G strictly crosses G-blocks, hence

beta_G(r_G)<0.

At every point whose minimal supporting flag ends in G, the G-barycenter coefficient is positive, so the affine carrier has strict beta_G<0 and cannot vanish.

The same face-normal sign gives the standard zero-free homotopy to the radial normal map. Hence the normalized boundary carrier has nonzero degree.

This repairs the orientation flaw of the actual-10-root boundary carrier without averaging labels.

### 2. Replace the center by one witnessed isolated band

Choose any bad full order pi_0 and any pair of consecutive changes p<q in its word. Let

r_0=e_s-e_t

be the corresponding isolated-band macro root.

Label the top-face barycenter by r_0 and cone the witnessed boundary carrier to that apex.

The boundary degree is nonzero, while neither boundary labels nor r_0 vanish. Therefore some cone simplex has a zero:

lambda_0 r_0 + sum_{i=1}^k lambda_i r_{F_i}=0,

with all displayed coefficients positive and

F_1<...<F_k=G

a proper face flag.

### 3. The largest-face isolated band lies on a closing path

Every boundary macro root is weakly forward in the G-block order, and r_G is strictly forward.

The zero equation makes the positive boundary-root flow have net divergence opposite r_0. Thus r_0 must be backward across G.

Decompose the boundary macro-edge flow into directed source-to-sink paths plus directed cycles.

No directed cycle of weakly G-forward edges can contain a strict G-crossing edge. Hence r_G cannot lie in a circulation component.

Therefore some closing path from the target of r_0 back to its source contains r_G.

### 4. Two-shore reduction

Choose a G-block boundary crossed by r_G and coarsen to a facet

H=L|R.

The chosen closing path is weakly forward and contains r_G, so after taking the corresponding boundary between its source and target blocks, the path crosses H exactly once at r_G.

Thus the topological extraction is:

- one backward isolated-band macro root r_0;
- one forward isolated-band macro root r_G crossing L|R;
- internal macro-root paths in L and R;
- every macro root is witnessed by a concrete full coordinate order and a pair of CONSECUTIVE changes, hence by one isolated monochromatic band.

Moreover the unique transverse edge r_G comes from the block-good witness pi_G: every constituent G-block is already ordered NOR-good.

### Significance

This reinstates the center-replacement / two-shore topology in a form immune to the orientation audit of §150.

The extracted edges are not actual adjacent-window 10 roots. They are isolated-band macro roots. But that is now an advantage: their witness states lie exactly in the threshold-band repair class.

The remaining gluing theorem can be stated entirely in Article III language:

> Given a positive closing path of witnessed isolated-band macro roots with one block-good transverse band, use flat band transport / realized repair cells to concatenate or eliminate the path, or force a terminal fully-curved exchange that strictly improves the protected witness state.

This is a more faithful Sperner interface than endpoint-only coordinate labels: the topological label remembers the complete two-change obstruction interval.

## Frontier

- Development version when composed: None
- Development version now: 1
