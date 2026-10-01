# Flat gap-one terminal cycles have length at most p minus one

## Statement

A flat terminal cycle of rank-(p-1) ascending edges with terminal potential p and private entrances of potential p-2 has length at most p-1. Indeed deleting the cycle edge immediately after e_i leaves a (c-1)-edge path ending physically at the private entrance x_i, so c-1<=phi(x_i)=p-2.

## Body


Let
  C=(e_0,...,e_{c-1})
be a linear terminal cycle of flat gap-one top edges:
  e_i={x_i,t_i,t_{i+1}},
with indices modulo c, where x_i is the private entrance of e_i,
  phi(e_i)=p-1,
  phi(x_i)=p-2,
and the terminal vertices have potential p.

Then
  c<=p-1.

Fix i and omit the next cycle edge e_{i+1}. The remaining c-1 cycle edges can be ordered
  e_{i+2},e_{i+3},...,e_{i-1},e_i
around the cycle. This is a linear path of length c-1: all consecutive intersections are inherited terminal joints of the cycle, and omitting e_{i+1} breaks the closing intersection.

The final edge is e_i. Its intersection with the preceding edge e_{i-1} is t_i. The other terminal t_{i+1} lies only on the omitted edge e_{i+1} among the cycle edges, while x_i is private to e_i. Hence x_i can be chosen as the physical last vertex of the displayed path.

Therefore
  phi(x_i)>=c-1.
But phi(x_i)=p-2 by ascendingness of the rank-(p-1) edge e_i. Hence
  c-1<=p-2,
so
  c<=p-1.

Thus any flat gap-one terminal cycle has circumference strictly smaller than the common terminal potential p.
