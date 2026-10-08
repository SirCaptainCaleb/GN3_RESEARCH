# Audit: short-phase scan rises and the missing A2 suffix window

Audit repair. Blocking in the old 1-phase excludes a local 101 packet but does not force the entire insertion scan to be monotone; explicit globally flat blocked p=2 scans can rise later. Therefore the old p=2 s=110... classification and arguments depending on it are invalid. Separately, the former g=1 A2 splice omitted a new suffix boundary window. The g=0 boundary-safe surgery remains valid. Future local closure claims must track every changed boundary window and use the corrected arbitrary-scan replacement theorem.
