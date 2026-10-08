# Audit: one-vertex insertion can fail even in the coboundary-flat sector

## Composition

(none yet)

## Development


## Audit: one-vertex insertion can fail even in the coboundary-flat sector

Assume delta f=0, so alpha has the tournament representation

alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a),

with t(b,a)=1-t(a,b).

Let O=(v_1,...,v_m), put

e_i=t(v_i,v_{i+1}),
p_i=t(x,v_i),

and define the insertion scan

s_i=alpha(x,v_i,v_{i+1}).

Then

s_i
=1 xor p_i xor e_i xor t(v_{i+1},x)
=p_i xor e_i xor p_{i+1}.

Thus the scan obeys a derivative formula.

However this imposes no effective restriction along one fixed order. Given arbitrary adjacent-edge bits e_i, arbitrary desired scan bits s_i, and one initial bit p_1, define recursively

p_{i+1}=p_i xor e_i xor s_i.

These are legitimate independent tournament edges between x and the v_i. Hence every binary scan word can occur in a coboundary-flat orientation.

Likewise, for the old alpha-word c_i, writing

r_i=t(v_i,v_{i+2})

gives

c_i=e_i xor e_{i+1} xor r_i.

After choosing the adjacent bits e_i, the distance-two tournament edges r_i are independent and can realize any prescribed old alpha-word.

Consequently the previously exhibited failure of one-vertex insertion for a pure orientation -- for example an old one-change word 000111 together with scan 1111000 -- can already be realized with delta f=0.

### Consequence

The coboundary-flat sector is not amenable to a naive one-vertex induction either. Its advantage is not a restriction on a single insertion scan; it is the existence of one global tournament whose edge variables couple many different orders simultaneously.

Therefore a successful flat-sector argument must compare multiple orders, use block exchanges, or exploit a global tournament potential. Local scan constraints alone cannot close it.
