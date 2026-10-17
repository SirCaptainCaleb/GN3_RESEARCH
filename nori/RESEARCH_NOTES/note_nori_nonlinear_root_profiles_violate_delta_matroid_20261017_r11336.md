# Nonlinear rooted full profiles violate delta-matroid exchange under balance and full affine span

- Stable ID: note_nori_nonlinear_root_profiles_violate_delta_matroid_20261017_r11336
- Author: session_nori_r11336_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, root-profiles, delta-matroid, symmetric-exchange, balanced, dimension-uniform, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11336_1
- Updated session: session_nori_r11336_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (non-delta rooted profiles with balance and full affine span).** On Q4 write E(a,b,d)=1 if a=b=d and zero otherwise, equivalently E=(1+a+b)(1+a+d) over F2. Define c_0=1+x_2, c_1=x_3, c_2=x_3+E(x_0,x_1,x_3), c_3=x_2. All rules ignore their own bits and are complement-odd, hence legal. Exhausting the 24 orders at root 0 gives the indexed profile words, as integer masks, W_0={1,3,4,6,7,8,9,11,12,14}. Take u=3, v=8 and a direction i=0 in u xor v={0,1,3}. The symmetric exchanges u xor {0}, u xor {0,1}, u xor {0,3} are masks 2,0,10; none belongs to W_0. Therefore W_0 violates the delta-matroid symmetric-exchange axiom.

Every rooted profile family nevertheless has full affine span F2^4. Indeed the profile changes from adjacent square swaps are delta_02=e_0+(1+x_1+x_3)e_2, delta_13=e_1, and delta_23=(x_0+x_1)e_2+e_3. At each prescribed root the unused prefix directions permit both values of x_1+x_3 at a 02 square, giving e_0 and e_2; the other two families then yield e_1,e_3. Enumeration verifies that each of the sixteen roots supports ten profiles; hence every two roots share a profile by the pigeonhole principle, so the complete root-profile incidence graph is connected. Enumeration also confirms symmetric exchange fails at each root.

For any N>=4 append direction reader rules c_j=x_0 for j>=4. Rooted profile families factor as W_(x,y)=W_x times F2^(N-4), because each appended direction may be traversed independently before or after all original steps. The four-dimensional exchange failure survives by choosing witnesses with the same appended bits, and rooted affine spans remain full. For each even N>=8, append first four rules 1+c_i in new directions, then optional pairs x_0,1+x_0; these rules are complement-odd and pair all incident colors pointwise, giving vertex balance. Factorization continues to hold, preserving full affine profile span, connected incidence, and failure of the delta-matroid axiom.

This refutes a universal rooted delta-matroid model even for balanced colorings with full rooted affine span and connected incidence; the construction satisfies NORI1. The finite certificate and proof are preserved in non_delta_root_profiles_balanced_20261017.md and non_delta_profile_verify.py. As an unproved contrast, exhaustive checking of the 4096 four-direction zero-diagonal affine matrices and 32768 legal five-direction affine matrices found no exchange violation.
