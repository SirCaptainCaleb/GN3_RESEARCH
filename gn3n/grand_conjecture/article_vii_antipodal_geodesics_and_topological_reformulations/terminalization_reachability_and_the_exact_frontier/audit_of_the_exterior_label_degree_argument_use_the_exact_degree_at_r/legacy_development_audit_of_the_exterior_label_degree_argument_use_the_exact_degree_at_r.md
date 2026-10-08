# Audit of the exterior-label degree argument: use the exact degree at R — preserved pre-item development

## Development

The conclusion of 271, that the saturated Johnson block is spanning, is correct by 269. Its displayed degree argument at K=R+y does not by itself prove that conclusion.

The known incoming edges at K give deg_in(K) >= |U|-d+1. Antipodality and minimum positive source degree give d <= deg_in(K). These two lower bounds on the SAME degree do not imply d <= |U|-d+1. Additional incoming edges from exterior labels have not been excluded there.

The valid repair is the exact-degree calculation at R, as in 269. Every u in U-R gives the edge R+u -> R. Every y outside U has Type I polarity and makes R+y a sink, so R+y -> R is absent by purity. Therefore
deg_in(R)=|U|-d+1
exactly. Antipodality then gives a source with precisely this degree, and minimality of d yields |U|>=2d-1. Proper-induced two-coverability gives |U|<=2d-2 if U is proper, the required contradiction.

No change to the spanning-block or odd-middle-layer conclusions is required. Only the inference from the lower-bound degree at K must be replaced by the exact degree at R.
