# One-polarity two-vertex toggle has a canonical local two-cover

**Summary:** In the one-polarity 001/011/0101 witness scheme, the two-vertex toggle normal form decomposes its ten determining vertices into two tight paths; it is not a dual-polarity terminal case and does not by itself span H.

## Statement

For the one-polarity witness normal form with status segments (0,t,1,1,1,1,1-t,1) and (0,t,0,0,0,0,1-t,1), the ten determining vertices have path-cover number at most two. This lemma is not part of the nearest dual-polarity terminal chain.

## Body

This is the corrected convention-specific form of the local toggle calculation. Let the ten determining vertices be ordered as (a,b,c,d,x,y,e,f,g,h), with the two one-polarity toggle chambers having status segments (0,t,1,1,1,1,1-t,1) and (0,t,0,0,0,0,1-t,1). If t=0, (c,d,x,y,e,f,g,h) is a tight path and (a,b) is the second path. If t=1, boundary antisymmetry gives the tight path (g,f,e,x,y,d,c), while exactly one of (a,b,h) and (h,b,a) is tight, giving the second path. Thus the ten-vertex determining support is two-coverable. This normal form arises in the one-polarity witness analysis. Under the nearest dual-polarity convention it contains a strictly closer witness of the opposite polarity, so it must not be used as a dual-polarity terminal case.

## Metadata

- ID: terminal_two_vertex_toggle_forces_two_cover
- Kind: toolkit
- Version: 3
- Math version: 3
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
