# Endpoint deletion yields a boundary hole exchange

## Composition

In the relaxed monochromatic state space, deleting a shore endpoint and absorbing the omitted shore vertex is a support-size-preserving omission exchange exactly when its two remaining endpoint incidences agree, provided those two coordinates exist. Deleting a required special vertex is outside that state space. Final endpoint compatibility remains a boundary target.

## Development

Let C=(c_1,...,c_m) be a monochromatic-zero connector in path-normalized square-path gauge and let a be a missing shore vertex. Write r_i for the incidence bit of c_i against a.

Deleting c_1 preserves monochromaticity. In the shortened order (c_2,...,c_m), prepending a is possible after choosing the switching state of a exactly when r_2=r_3: then a can be oriented consistently against the first two vertices, and no other window changes. Thus there is a support-preserving omission exchange from missing a to missing c_1 whenever r_2=r_3.

Symmetrically, deleting c_m and appending a gives a support-preserving omission exchange whenever r_{m-2}=r_{m-1}.

Therefore any blocker word trapped against both endpoint hole exchanges satisfies r_2 != r_3 and r_{m-2} != r_{m-1}. This is a statement in the relaxed monochromatic repair complex; final endpoint compatibility is only a boundary target.

Elevation audit: an exchange that retains the required special vertices assumes the deleted endpoint is a shore vertex, and the shortened path has the two endpoint coordinates used by the incidence test. Removing x or z leaves the specified connector state space. Final port compatibility remains a separate boundary target.
