# Short-loss boundary sinks: loss two always escapes and loss one has exactly two exceptional forms

## Statement


In the boundary case q=delta, suppose a lossy double-blocker splice from a canonical entrance path produces an x-ending path avoiding y,z and the new opposite endpoint has no safe clean extension and no safe single-blocker rotation. Loss two is impossible. For loss one, exactly one of two forms remains: (A) two clean edges, one through y and one through z, with at most one single blocker, necessarily x-type; or (B) one clean edge through one terminal and exactly two single blockers, one x-type and one through the other terminal.


## Body


Let r be the loss and let C,S,D count clean, single-blocking and double-blocking edges at the new opposite endpoint. Endpoint deficiency gives
  2C+S >= 2(r+1).
No safe clean edge means every clean edge contains y or z, so C<=2. No safe single blocker means every single blocker is exceptional: x-type, y-type, or z-type, at most one of each.

For r=2, the deficiency inequality gives 2C+S>=6. Since C<=2 and S<=3, necessarily C=2 and S>=2; the two clean edges are exactly the y-edge and z-edge. But then linearity forbids any y- or z-type single blocker, leaving only x-type, of which there can be at most one. Contradiction. Thus every loss-two state has a safe continuation.

For r=1, 2C+S>=4 and C>=1. If C=2, the two clean edges are y- and z-edges, again excluding y- and z-type single blockers, so S<=1 and any such blocker is x-type: case (A). If C=1, say the unique clean edge contains y, then y-type single blockers are excluded. The only possible singleton types are x and z, at most one each; the inequality forces S=2, giving exactly one of each. This is case (B), with the symmetric version when the unique clean edge contains z.
