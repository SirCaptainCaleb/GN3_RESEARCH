
STANDARDIZATION DICTIONARY

Each research project owns a project-local standardization dictionary. It is normative for durable mathematical prose in that project and is never shared across projects.

Read it with:
  gn3n.standardization_dictionary()

Entries have status canonical | alias | prohibited.
- canonical: preferred project terminology;
- alias: recognized noncanonical wording that should be replaced by preferred_term in durable mathematics;
- prohibited: wording that should not appear in durable mathematical prose; preferred_term may name the replacement.

An empty dictionary imposes no additional project-local vocabulary beyond the general requirement to use standard mathematical language.

Dictionary mutation is ordinary worker maintenance and is available under every scheduler mode:
  gn3n.upsert_standardization_term(...)
  gn3n.remove_standardization_term(...)

The dictionary is project-local state. New-project creation initializes the dictionary schema but MUST NOT copy dictionary entries between projects.
