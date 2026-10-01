# Aharoni--Haxell hypergraph Hall toolkit

## Statement

A family of hypergraphs has disjoint representatives if every subfamily has matching width at least its cardinality. A deficiency form gives a large partial system of disjoint representatives when the inequality is allowed a fixed deficit.

## Body


Source: Ron Aharoni and Penny Haxell, "Hall''s theorem for hypergraphs", Journal of Graph Theory 35 (2000), 83--88.
Publisher: https://onlinelibrary.wiley.com/doi/10.1002/1097-0118(200010)35:2%3C83::AID-JGT2%3E3.0.CO;2-V

Definitions. A set K of edges pins a set F if every edge of F intersects some edge of K. For a hypergraph G and a matching M in G, let pi_G(M) be the minimum size of an edge set of G that pins M. The matching width is
  mw(G)=max{pi_G(M): M is a matching in G}.

Aharoni--Haxell theorem. Let (H_i)_{i in I} be a finite family of hypergraphs on a common ground set. If for every J subset I,
  mw(union_{i in J} H_i) >= |J|,
then there are pairwise disjoint edges e_i in H_i for all i in I.

Proof architecture. The original proof is topological and uses a Sperner-type argument. A triangulated simplex has one vertex/color for each member of the family. Local choices of hyperedges are arranged so that a fully colored simplex supplies pairwise disjoint representatives; failure of disjointness would produce a small pinning set contradicting the matching-width hypothesis. Because the detailed topological construction is specialized, the canonical proof remains linked rather than recopied verbatim.

Deficiency corollary (full proof). Suppose instead that
  mw(union_{i in J}H_i) >= |J|-d
for every J subset I. Introduce d new vertices z_1,...,z_d disjoint from the old ground set, and enlarge every H_i by the d singleton edges {z_1},...,{z_d}. For any J, choose a matching M in the old union requiring at least |J|-d pinning edges, and add all d dummy singleton edges. Pinning the old part and pinning the d fresh singletons are independent tasks, so the enlarged union has matching width at least |J|. Apply Aharoni--Haxell. A full disjoint representative system in the enlarged family uses at most d dummy singletons, hence at least |I|-d representatives are genuine old edges. Thus there is a partial system of disjoint representatives of size at least |I|-d.

LINP relevance. This is a robust "many local option families => globally compatible disjoint choices" engine. Its contrapositive is equally useful: failure to choose many disjoint path-extension gadgets certifies a subfamily with small matching width, hence a small set of edges that pins a large obstruction family.
 