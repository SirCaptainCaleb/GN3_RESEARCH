# Three nonrigid width-two types close at a three-window exterior, with exact interior collar transport

## Composition

In the flat alternating sector, a full/full width-two band with a trailing three-window zero phase closes whenever its chord type is nonrigid. The easy chord branches reduce to the established singleton or width-two terminal constructions. For the three exact nonrigid six-set types, explicit eight-coordinate replacements repair the formerly forced 01 splice while preserving the left ordered pair. They yield either 000110 or 0000kl, each admitting a spanning closure. The same replacements preserve the final coordinate and therefore leave only one changed right crossing bit in an interior occurrence; that interior export remains an extraction obligation. The rigid six-set type is not closed by this theorem.

## Development

## Three nonrigid width-two types close at a three-window exterior, with exact interior collar transport

Work in the coboundary-flat alternating ternary sector. Suppose a full order has word 0^A 1^2 0^3, A>=1, and its two band boundaries are full. Write its final eight coordinates (a,b,c,d,e,f,g,h), so their six window labels are 011000. Put t=bce, u=abe. We give actual spanning orders, without maximizing over a restricted short-tail family.

If t=0, the replacement (a,b,c,e,d,f) has internal word 0001. If t=1,u=0, the replacement (a,b,e,d,c,f) has internal word 0001. Both preserve the first pair (a,b) and the final coordinate f. Thus, after appending g,h, the full word is 0^(A+2),1,x,0: the last bit fgh is untouched. If x=0, use the singleton spanning theorem §253 (trailing length two); if x=1, use the width-two terminal spanning theorem §259. These two chord branches therefore close.

Now t=u=1. Use the exact §264 table, r=abf and s=bcf. Suppose (r,s)!=(1,1).

For s=0, replace the first six coordinates by (a,b,c,f,e,d), whose internal word is 0001. For s=1,r=0, replace them by (a,b,f,e,c,d), also with internal word 0001. Both preserve (a,b). Denote the two right crossing labels by x,y.

If xy=11, the spanning word is already good. If xy=00, it is a singleton with trailing length two and §253 closes it. If xy=10, it is a width-two band with trailing length one and §259 closes it. It remains to treat xy=01; no extremality argument is needed.

### Type s=0: repair the forced 01 splice

Here x=edg=0 and y=dgh=1. Alternation gives deg=1. Flatness on defg, using def=efg=0, gives dfg=1.

Use the eight-coordinate order
(a,b,c,f,e,g,d,h).
Its six labels, in order, are
abc=0, bcf=0, cfe=0, feg=1, egd=1, gdh=0.
The values feg=1 and gdh=0 follow by transposition from efg=0 and dgh=1; egd=deg=1 follows by cyclic invariance. Its word is therefore 000110. The ordered first pair (a,b) is preserved, so the complete spanning word is 0^(A+2)1^2 0. Apply §259.

### Type s=1,r=0: absorb the forced 01 splice

Here x=cdg=0 and y=dgh=1. Use
(a,b,f,c,d,g,e,h).
The first four labels are
abf=0, bfc=0, fcd=cdf=0, cdg=0.
Write the final two labels k=dge and l=geh. The full spanning word is 0^(A+3),k,l. Every pair kl gives a good word except 10. In that case it is a singleton with trailing length one, closed by §253. Thus this type also closes.

### Exact theorem and scope

Every full/full width-two band 0^A1^2 0^3 with either t=0, or t=1,u=0, or t=u=1 and (r,s)!=(1,1), has a spanning NOR-good order. Reversal and one global color complement give the corresponding leading-three-window result. A may be arbitrarily large. The exceptional rigid type t=u=r=s=1 is expressly unresolved.

### Interior extension of the same surgery

The two eight-coordinate replacements preserve the ordered first pair and the final coordinate h. In an interior occurrence, all left exterior windows and the second right crossing window are fixed. Only the first right crossing bit can change.

For s=0, the repaired local word is 000110. If the remaining right crossing bit is 0, the global word remains in the two-change class with a strictly longer leading zero run, or is good. An extremal survivor therefore forces that one bit to be 1, giving a specified isolated 01 reconnection beyond the repaired width-two band.

For s=1,r=0, the repaired local word is 0000kl. If a right exterior coordinate is present, let its sole changed crossing label be z. After k,l,z, the old zero suffix resumes. The only pattern with two separated nonempty 1-bands is klz=101. Every other pattern yields a good order or a member of the two-change class with a longer leading zero run. Hence an interior extremal survivor forces exactly klz=101.

This is a collar-compatible witness construction. The one-bit interior survivor still requires a further realized surgery; the spanning conclusion above uses the actual right endpoint, and does not claim general interior closure.
