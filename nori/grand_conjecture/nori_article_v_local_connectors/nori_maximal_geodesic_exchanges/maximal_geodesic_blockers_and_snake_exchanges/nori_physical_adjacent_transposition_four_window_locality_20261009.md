# Adjacent direction exchange preserves all but four physical three-face windows

# Physical adjacent-transposition localization

**Lemma.** In a physical k-edge direction-distinct cube geodesic P rooted at x, interchange consecutive directions p_i and p_(i+1) to obtain P'. Both paths have the same root, endpoint, and direction support. Their genuine ordered-three-face windows W_j are *identical as physical ordered faces* for all j outside [i-2,i+1] intersect [1,k-2]. Consequently their color words differ in at most four consecutive positions under an arbitrary active NORI coloring.

**Proof.** Both direction words flip the same coordinates. Their prefix vertices are identical up through step i-1 and again from step i+1 onward, because coordinate flips commute. Every triple window whose indices avoid i and i+1 has the same ordered directions and the same preceding prefix vertex, hence determines the same physical ordered face. The only potentially modified starts j obey j<=i+1 and j+2>=i. QED.

**Exchange application and scope.** An adjacent direction swap therefore preserves the entire certified color word outside one four-window interval; only that interval and its boundary color comparisons need rechecking. This provides an exact root- and support-preserving operation for studying globally maximal one-switch geodesics. It does not force an improving exchange, missing-coordinate extension, or grand closure.
