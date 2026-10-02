# Endpoint hook forcing

## Statement

Every component P=(p_0,...,p_m), m>=2, of every exact deletion two-cover H-x=P|Q in a minimum counterexample forces all four tight triples (p_1,p_0,x), (p_2,x,p_0), (x,p_m,p_{m-1}), and (p_m,x,p_{m-2}); likewise for Q.

## Body

# Endpoint hook forcing

Let H be a minimum counterexample, fix x in V(H), and let

H-x = P | Q

be any exact two-path cover. Write

P=(p_0,...,p_m),

where m>=2.

Then the four endpoint-hook triples

(p_1,p_0,x),
(p_2,x,p_0),
(x,p_m,p_{m-1}),
(p_m,x,p_{m-2})

are all tight.

Thus every component of every deletion two-cover carries, at each end, a bounded four-vertex orientation pattern involving the omitted vertex x. No auxiliary comparison cover is needed to produce these hooks.

## Proof

If (x,p_0,p_1) were tight, then

(x,p_0,...,p_m) | Q

would be a spanning two-cover of H. Hence (x,p_0,p_1) is non-tight, so boundary antisymmetry gives

(p_1,p_0,x)

tight.

Suppose (p_0,x,p_2) were tight. Then

(p_0,x,p_2,...,p_m)

is tight, since its only new consecutive triple is (p_0,x,p_2). Prepending p_1 gives

(p_1,p_0,x,p_2,...,p_m),

whose first triple is the already proved (p_1,p_0,x), whose second is (p_0,x,p_2), and whose remaining triples are inherited from P. Together with Q this would two-cover H, contradiction. Therefore (p_0,x,p_2) is non-tight and

(p_2,x,p_0)

is tight.

The right end is symmetric. If (p_{m-1},p_m,x) were tight, appending x to P would two-cover H, so

(x,p_m,p_{m-1})

is tight.

If (p_{m-2},x,p_m) were tight, then

(p_0,...,p_{m-2},x,p_m)

would be tight. Appending p_{m-1} gives

(p_0,...,p_{m-2},x,p_m,p_{m-1}),

using the already proved tight triple (x,p_m,p_{m-1}); together with Q this would two-cover H. Hence (p_{m-2},x,p_m) is non-tight and

(p_m,x,p_{m-2})

is tight. ∎

The same four triples hold with Q in place of P. Therefore every deletion two-cover supplies two synchronized endpoint hooks on each component, all sharing the omitted vertex x.