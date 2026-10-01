# An all-clean two-regular shell either has a three-step repeated label or is a canonical decagon

## Statement

Assume the five-label shell conclusion of astra004fiveactiveshell. Write r_i for the active 2-subset of support S_i and x_i for the label of edge S_iS_{i+1}. Then either x_i=x_{i+3} for some i, giving a clean four-edge corridor with three-step repeated label, or the support cycle has length exactly 10. In the latter case the edge-label word has period five, every five consecutive labels are the five active labels in some order, and r_i={x_{i-2},x_{i+1}}. Thus the non-repeated-label branch is the bipartite double cover of a five-cycle on five active pair types.

## Body

Cleanliness of S_i-S_{i+1}-S_{i+2} gives S_{i+2}=(S_i-{x_{i+1}})+{x_i}; hence x_{i+1} belongs to r_i and x_i belongs to r_{i+2}. Applying this two steps earlier also gives x_{i-2} in r_i. Consecutive labels are distinct, and labels at distance two are distinct because x_i lies in r_{i+2} whereas x_{i+2} is omitted from S_{i+2}. If some x_{i-2}=x_{i+1}, this is exactly a label repetition at distance three. Otherwise r_i, which has order two, equals {x_{i-2},x_{i+1}}. Then adjacent active pairs r_i and r_{i+1} are disjoint and x_i is the unique fifth active label outside their union, so x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2} are all distinct. Sliding the five-term window by one position forces x_{i+3}=x_{i-2}; hence x has period five. The shell cycle is even, so its length is a multiple of ten. But r_i is five-periodic and the core parity is two-periodic, so S_{i+10}=S_i. Simplicity of the support cycle therefore forces length exactly ten.
