# Protected A3 reversal pairs project to Johnson geodesics of length at most two

## Composition

If both orientations of a ternary A3 endpoint root genuinely carry minimum-p protected provenance, canonical switch geometry forces the four-block to start at p or p-1. Under block reversal the corresponding protected cuts are therefore Johnson distance one or two. Explicit reduced chamber paths realize the reversal with exactly that many cut-changing walls and all remaining walls inside fixed-cut fibers. Thus, after collapsing cooriented fibers, a genuine protected A3 two-cycle reduces to at most two actual cut exchanges.

## Development

## Protected A3 reversal pairs project to Johnson geodesics of length at most two

Assume ternary arity and a genuine protected A3 two-cycle: a canonical minimum-first-phase root rho and its opposite -rho are both realized in the same four-coordinate Coxeter block by protected states normalized to the same first-phase length p.

For a canonical switch insertion, the inserted coordinate occupies position p+1. If the internal 10 slide starts at rank i, the ternary root block occupies positions i,i+1,i+2,i+3. The condition that both consecutive ternary windows contain the inserted coordinate gives i in {p-1,p}. Thus the protected cut after position p meets the four-block in only two possible sizes:

1. i=p: exactly the first block coordinate lies on the left of the cut;
2. i=p-1: exactly the first two block coordinates lie on the left of the cut.

Write the first protected chamber on the block as (a,b,c,d), so rho=e_a-e_d, and the opposite reversal chamber as (d,c,b,a).

### One-left-coordinate case

If i=p, the cut traces are {a} and {d}. Hence the two protected cuts differ by the single exchange a -> d and have Johnson distance one.

Moreover the reversal can be realized by
(a,b,c,d)
-> (a,b,d,c)
-> (a,d,b,c)
-> (d,a,b,c)
-> (d,a,c,b)
-> (d,c,a,b)
-> (d,c,b,a).
Only the third wall swaps the first and second block positions, hence only that wall crosses the protected cut. All other walls remain in a single cut fiber.

### Two-left-coordinate case

If i=p-1, the cut traces are {a,b} and {d,c}. Their Johnson distance is two.

Use the reduced path
(a,b,c,d)
-> (b,a,c,d)
-> (b,c,a,d)
-> (b,c,d,a)
-> (c,b,d,a)
-> (c,d,b,a)
-> (d,c,b,a).
Only the second and fifth walls swap positions two and three, the protected cut boundary. The cut traces follow the Johnson geodesic
{a,b} -> {b,c} -> {c,d}.
Every other wall remains inside a cut fiber.

### Consequence

After collapsing same-cut chamber motion, every genuine protected A3 reversal two-cycle is represented by a path of length one or two in the Johnson graph of physical p-cuts. Thus the two-cycle extraction problem is not a six-wall A3 problem after quotienting by cooriented fibers. It reduces to at most two actual cut exchanges, while the intervening chamber motion is root-cooriented.

This does not show that either cut exchange is itself a threshold surgery. It does sharpen the missing theorem: in the protected two-cycle case, it is enough to analyze one Johnson edge, or two consecutive Johnson edges with one intermediate cut, rather than an arbitrary A3 carrier.
