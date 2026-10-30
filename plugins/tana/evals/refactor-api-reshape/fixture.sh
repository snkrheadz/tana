#!/bin/bash
set -euo pipefail
mkdir -p docs
cat > users.py <<'EOF'
USERS = {1: {"name": "Ann", "email": "ann@example.com", "orders": [10, 11]},
         2: {"name": "Bo", "email": "bo@example.com", "orders": []}}


def get_user(uid, with_email=False, with_orders=False):
    u = USERS[uid]
    out = {"name": u["name"]}
    if with_email:
        out["email"] = u["email"]
    if with_orders:
        out["orders"] = list(u["orders"])
    return out
EOF
cat > api.py <<'EOF'
from users import get_user


def profile(uid):
    return get_user(uid, True)
EOF
cat > report.py <<'EOF'
from users import get_user


def order_counts():
    return {uid: len(get_user(uid, with_orders=True)["orders"]) for uid in (1, 2)}
EOF
cat > admin.py <<'EOF'
from users import get_user


def full_record(uid):
    return get_user(uid, True, True)
EOF
cat > docs/usage.md <<'EOF'
# Using the users module

Call `get_user(uid, with_email=True)` to include the email address, and pass
`with_orders=True` to include order ids.
EOF
git add -A >/dev/null 2>&1 && git -c user.email=e@x -c user.name=e commit -qm "users module" >/dev/null 2>&1 || true
