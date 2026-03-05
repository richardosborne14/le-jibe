# Task [X.X]: [Task Name]

**Status:** Complete / In Progress / Blocked  
**Confidence:** X/10  
**Date:** YYYY-MM-DD

---

## What Was Built

[2–4 sentences describing what now exists that didn't before. Be concrete — name files, endpoints, components.]

---

## Key Decisions

| Decision | Why |
|---|---|
| [What was chosen] | [Reason — especially if alternatives were considered] |

---

## Files Created / Modified

```
backend/app/api/signups.py        — created
backend/app/models/signup.py      — created
backend/app/schemas/signup.py     — created
alembic/versions/xxxx_signups.py  — created (migration)
```

---

## How to Test

```bash
# [Command to verify this works]
# Example:
curl -X POST http://localhost:8000/api/signups \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "first_name": "Test", "profile_type": "user"}'

# Expected: 201 Created with {"id": 1, "email": "test@example.com", ...}
```

---

## Known Limitations / Follow-ups

- [Anything deliberately left simple for now]
- [Edge cases not handled — and why that's acceptable at this stage]
- [Anything to revisit in Phase 2]

---

## Blockers / Notes for Human

[Leave blank if none. Otherwise describe what needs a human decision before proceeding.]
