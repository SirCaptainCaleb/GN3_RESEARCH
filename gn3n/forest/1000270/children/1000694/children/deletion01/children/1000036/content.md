# End-adjacent clean replacement is impossible

## Statement

In every exact deletion two-cover of a minimum counterexample, the internal vertex adjacent to either endpoint of either component cannot admit the clean same-slot replacement by the omitted vertex. Thus the internal-deletion trichotomy forces explicit support crossing or relative-order disagreement at a canonical end-adjacent location.

## Body

# End-adjacent clean replacement is impossible

Let H be a minimum counterexample to the grand two-cover conjecture. Fix any vertex x and any exact two-path cover

H-x = P | Q,

where P=(p_0,...,p_m). By the minimum-counterexample calculus, |P|>=3, so m>=2.

## Theorem

For either internal vertex adjacent to an endpoint of P, the clean same-slot replacement branch of the internal-deletion trichotomy is impossible.

More explicitly, no exact two-cover of H-p_1 can be

(p_0,x,p_2,...,p_m) | Q,

and no exact two-cover of H-p_{m-1} can be

(p_0,...,p_{m-2},x,p_m) | Q.

Therefore, for every exact two-cover F of H-p_1, the internal-deletion trichotomy exposes either

- an ordinary edge of F crossing two inherited classes among (p_0), (p_2,...,p_m), and Q; or
- a relative-order disagreement with the inherited order on P or Q.

The symmetric statement holds at p_{m-1}.

## Proof

Since H is a counterexample, x cannot be prepended to P: if (x,p_0,p_1) were tight, then

(x,p_0,...,p_m) | Q

would be a spanning two-cover of H. Hence (x,p_0,p_1) is non-tight. Boundary antisymmetry gives

(p_1,p_0,x)

tight.

Suppose an exact cover of H-p_1 had the clean form

(p_0,x,p_2,...,p_m) | Q.

Then

(p_1,p_0,x,p_2,...,p_m)

is a tight path: its first consecutive triple is (p_1,p_0,x), its second is (p_0,x,p_2) from the clean replacement path, and every later consecutive triple is inherited from that same path. Together with Q this spans H by two tight paths, contradiction.

The right endpoint is symmetric. If (p_{m-1},p_m,x) were tight, appending x to P would two-cover H, so boundary antisymmetry gives

(x,p_m,p_{m-1})

tight. A clean cover

(p_0,...,p_{m-2},x,p_m) | Q

of H-p_{m-1} would then make

(p_0,...,p_{m-2},x,p_m,p_{m-1})

tight, again yielding a spanning two-cover with Q.

Thus neither end-adjacent internal deletion can be clean. Applying the internal-deletion trichotomy proves the asserted crossing/order-disagreement alternatives. ∎

## Consequence for the current frontier

Every exact one-vertex deletion two-cover in a minimum counterexample already has a canonical place where explicit support/order disagreement is forced: the internal vertex adjacent to either endpoint of either component.

Hence the current endpoint-transport frontier does not need a preliminary argument to prove that disagreement exists. The remaining unsupported task is strictly the consumer problem: turn one of these forced crossing/order-disagreement witnesses into endpoint absorption, a direct spanning two-cover, or a spanning ordering of defect span at most two.