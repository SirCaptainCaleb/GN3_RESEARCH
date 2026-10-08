# Audit refinement: the universal connector leaves a shore phase-alignment problem — preserved pre-item development

## Composition

(none yet)

## Development


Section 330 gives an exact universal central connector, but its immediate gluing consequence must be stated carefully.

If A=(a_1,...,a_r) and B=(b_1,...,b_s), then the full order
A,x,z,B
contains the forced central windows
alpha(a_r,x,z)=0,
alpha(x,z,b_1)=1.

These already consume the unique allowed global status change. Therefore every earlier window, including all internal A windows and the remaining left crossing window alpha(a_{r-1},a_r,x), must be 0; likewise every later window, including alpha(z,b_1,b_2) and all internal B windows, must be 1.

Thus ordinary NOR-good shore orders with merely matching endpoint phases are not sufficient. The direct connector closes only from a monochromatic-0 left extension and a monochromatic-1 right extension (or the reversed 1-to-0 version).

The valid remaining target is therefore a phase-alignment theorem:

Given the signature split A|B induced by a protected-shortcut-free pair x,z, construct shore orders whose entire exposed phases are compatible with the universal connector, or recursively refine the shores until their internal switches are absorbed into the same global switch.

This is exactly where a Hartman-style reversible reachability/least-unreachable argument could enter: the connector itself is solved, and the unresolved datum is which boundary phase each proper shore can expose without introducing an additional switch.
