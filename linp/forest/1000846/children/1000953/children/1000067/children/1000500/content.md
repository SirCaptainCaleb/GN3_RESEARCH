# Almost-spanning hypertrees give a 1/3 ceiling for Steiner-system lower constructions

## Statement

Im, Kim, Lee and Methuku proved that for every fixed mu>0 and all sufficiently large v, every Steiner triple system on v vertices contains every hypertree on at most (1-mu)v vertices. In particular it contains a linear path with at least ((1-mu)v-1)/2 edges. Consequently a sequence of Steiner triple systems, used as P_ell-free components at their first forbidden path lengths, has normalized density (|E|/|V|)/ell at most 1/3+o(1). Thus full Steiner triple systems cannot yield an asymptotic lower-bound coefficient strictly larger than 1/3.

## Body

Source: Seonghyuk Im, Jaehoon Kim, Joonkyung Lee, Abhishek Methuku, "A proof of the Elliott-Rodl conjecture on hypertrees in Steiner triple systems", Forum of Mathematics, Sigma 12 (2024), e75, DOI 10.1017/fms.2024.34.

Their theorem states that for every mu>0 there is v_0 such that every v-vertex Steiner triple system with v>=v_0 contains every hypertree on at most (1-mu)v vertices. A linear path is a hypertree. Therefore the maximum linear-path length L in such an STS satisfies
  2L+1 >= (1-mu)v - O(1),
so L >= (1-mu)v/2 - O(1).

An STS(v) has v(v-1)/6 edges and hence edge/vertex ratio (v-1)/6. If ell=L+1 is the first forbidden path length, then
 ((|E|/|V|)/ell)
 <= ((v-1)/6)/((1-mu)v/2-O(1))
 = 1/[3(1-mu)] + o(1).
Letting mu tend to zero gives limsup at most 1/3.

This does not rule out fixed-length additive improvements such as the PG(3,2) P7 construction, nor partial triple systems that are far from Steiner. It does rule out any strategy whose asymptotic components are themselves Steiner triple systems.
