# Consecutive terminal-only singleton ranks sum to at least the host potential plus four

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let e,f be distinct ascending nonspecial edges terminal at v, each having exactly one off-v contact with P, and suppose in both cases that contact is the opposite terminal while the unique entrance is absent from P. If the contact of e occurs before the contact of f along P, and r_e=phi(e), r_f=phi(f), then r_e+r_f>=p+4. Consequently, among terminal-only singleton edges of rank at most q, at most one can occur whenever p>=2q-3.

## Body

Let j_e be the first path-edge index containing the contact of e. The corrected single-contact window 028c2c3f7167 gives j_e>=p-r_e+1. The earlier-contact inequality df8ad4c65be0, applied to e before f, gives j_e<=r_f-3. Combining yields p-r_e+1<=r_f-3, hence r_e+r_f>=p+4. If both ranks are at most q, two such contacts require 2q>=p+4. Therefore p>=2q-3 excludes a pair.