# Insertion scan band boundary classification

## Metadata

- ID: insertion_scan_band_boundary_classification
- Parent Section: monochromatic_connector_blocks
- Position: 6
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

A maximal scan-zero interval around xz has flat internal boundary tetrahedra. When it meets an endpoint, failed compatible insertion has explicit opposite dominance of the endpoint pair. These local data must be realized as full port-preserving exchanges before they define repair edges.

## Development

For a monochromatic connector C and an additional shore coordinate a, define s_i=alpha(a,c_i,c_{i+1}). Let the maximal constant-zero interval containing the xz edge be indexed from l through r. If l is internal, then the local scan values are 1 then 0. Together with the zero base status, tetrahedral parity determines the fourth face and shows that this boundary is a flat transition cell. The right boundary has the symmetric property. If the interval reaches the left end and endpoint absorption is unavailable, the first two connector coordinates both dominate a. If it reaches the right end, a dominates the final two connector coordinates. Hence every insertion obstruction is a constant-zero interval around xz with flat internal boundary cells and explicit endpoint dominance data.
