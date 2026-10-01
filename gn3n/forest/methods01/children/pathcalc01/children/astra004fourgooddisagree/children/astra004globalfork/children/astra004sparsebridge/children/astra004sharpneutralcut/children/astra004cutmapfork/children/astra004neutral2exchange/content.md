# A disturbance-free sparse shell forces exactly two good deletions and one two-ended longest-support exchange

## Statement

Keep the sharp-shell longest-path setup A,U,D. Assume no direct mixed-support crossing or relative-order disagreement occurs in the Astra-004 endpoint/deletion probes, and assume every bad deletion state lies in the neutral equality-two-crossing cut form of astra004sharpneutralcut. Then |D|=2, the cut map k:U-D->{1,...,lambda-1} is a bijection, and the extreme cuts produce distinct w_L,w_R such that B=(w_L,a_1,...,a_{lambda-2},w_R) is a globally longest tight path. Thus the entire disturbance-free deletion-sparse branch reduces to a genuine two-ended replacement of A.

## Body

Certified astra004threegoodmixed says |D|>=3 already forces direct mixed-support crossing or relative-order disagreement, excluded here. Hence |D|<=2. By astra004repeatcutdisturb, two distinct bad labels cannot share a neutral cut without producing explicit disturbance, so k is injective on U-D. Since |U|=lambda+1, the number of bad labels is lambda+1-|D|, while there are only lambda-1 possible cuts. Injectivity gives lambda+1-|D|<=lambda-1, hence |D|>=2. Therefore |D|=2 and the two finite sets have equal size lambda-1, so k is bijective. Apply the injective branch of astra004cutmapfork. The extreme cuts 1 and lambda-1 yield endpoint replacements by w_L,w_R. If w_L=w_R, insert01 forces relative-order disagreement, excluded. Hence w_L!=w_R and astra004cutmapfork gives the tight path B=(w_L,a_1,...,a_{lambda-2},w_R) of order lambda.
