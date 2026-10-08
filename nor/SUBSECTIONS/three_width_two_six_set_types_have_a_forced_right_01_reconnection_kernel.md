# Three width-two six-set types have a forced right 01 reconnection kernel

## Metadata

- ID: three_width_two_six_set_types_have_a_forced_right_01_reconnection_kernel
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 265
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For the exact two-bit width-two table, all types except (r,s)=(1,1) have an explicit left-pair-preserving six-set order with internal word 0001: use (a,b,c,f,e,d) when s=0 and (a,b,f,e,c,d) when s=1,r=0. The only two changed right reconnection bits must then equal 01 in any lexicographic extremum; every other pair keeps one contiguous 1-band while strictly increasing the leading zero run. Thus the width-two frontier is the exceptional (1,1) rigid type or one forced exported 01 kernel.

## Development

## Three width-two six-set types have a forced right 01 reconnection kernel

Continue with §264 for a lexicographically extremal width-two full/full band 0^A 1^2 0^C on six consecutive coordinates (a,b,c,d,e,f). Put r=alpha(a,b,f) and s=alpha(b,c,f). Terminal short-tail cases are already covered by §259.

If s=0, use the order (a,b,c,f,e,d). Its statuses are
abc=0,
bcf=0,
cfe=1-cef=0,
fed=1-def=1.
Thus its local word is 0001.

If s=1 and r=0, use (a,b,f,e,c,d). Its statuses are
abf=0,
bfe=1-bef=0,
fec=1-cef=0,
ecd=cde=1.
Again its local word is 0001.

Both replacements preserve the ordered left pair (a,b), hence every left exterior window is unchanged. Therefore every two-bit six-set type except (r,s)=(1,1) has a left-compatible 0001 replacement.

Only two windows crossing the right edge of the reordered six-set can change. Call them x,y. The next window, when present, is an untouched old trailing-zero window and equals 0. Hence the new global word consists of the unchanged zero prefix, the packet 0001, then x,y,0, then the old zero suffix.

For (x,y)=00,10, or 11, all 1s remain in one contiguous band. The leading zero run has strictly increased, so the resulting order closes NOR or contradicts lexicographic maximality. Consequently any extremal survivor must have

(x,y)=(0,1).

Thus the width-two lexicographic frontier reduces to two species:

1. the exceptional six-set type (r,s)=(1,1);
2. the exact exported right reconnection kernel 01 arising from each of the other three six-set types.

This argument remains entirely within the global two-change comparison class until the forced 01 kernel appears and uses no maximal-threshold-band rotation hypothesis.
