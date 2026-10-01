# A globally longest unique large side forces orders eleven, twelve, or fifteen

## Statement

Let H be a minimum counterexample and let P|Q|X be a globally Phi-minimal spanning three-cover in the non-endpoint-square unique-large branch of global_sizegap_maximin_bypass01, so with c=|X| one has either component profile (c+2,c,c) or (c+3,c,c). Assume the largest displayed component P is globally longest. Then exactly the following ambient possibilities remain: (5,3,3) at order 11, (6,3,3) at order 12, or (7,4,4) at order 15. In particular, every such globally-longest size-gap branch of order at least sixteen is impossible.

## Body

# Proof

By global_sizegap_maximin_bypass01, exclusion of the endpoint-square branch together with a largest-second size gap at least two forces q=c and p in {c+2,c+3}. By hypothesis the displayed p-vertex path P is globally longest, so the maximum tight-path order is lambda=p.

Use the certified universal longest-path lower bound from bcfa72bc175f:

lambda >= ceil((n-1)/2).

First suppose p=c+2. Then n=3c+2 and lambda=c+2. Hence

c+2 >= ceil((3c+1)/2),

so in particular 2c+4 >= 3c+1 and therefore c<=3. Since every minimum counterexample has order greater than ten, c cannot be at most two here; thus c=3, giving profile (5,3,3) and n=11.

Now suppose p=c+3. Then n=3c+3 and lambda=c+3. Hence

c+3 >= ceil((3c+2)/2),

so 2c+6 >= 3c+2 and c<=4. If c<=2 then n<=9, impossible for a minimum counterexample. Thus c is 3 or 4, giving respectively profiles (6,3,3) at n=12 and (7,4,4) at n=15.

Therefore no globally-longest unique-large branch of the stated type exists above order fifteen. ∎
