"""Runtime import helpers for Cython-accelerated modules."""

try:
    from app.cython_modules.scoring import score_sum as score_sum
    CYTHON_ENABLED = True
except Exception:  # pragma: no cover
    from app.cython_modules.scoring_fallback import score_sum as score_sum
    CYTHON_ENABLED = False
