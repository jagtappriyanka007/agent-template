from app.cython_modules.runtime import score_sum as runtime_score
from app.cython_modules.scoring_fallback import score_sum as py_score

try:
    from app.cython_modules.scoring import score_sum as cy_score
except Exception:  # pragma: no cover
    cy_score = None


def test_score_sum_parity() -> None:
    if cy_score is None:
        return

    values = [1.0, 2.5, 3.5]
    assert abs(py_score(values) - cy_score(values)) < 1e-9


def test_runtime_loader_matches_fallback() -> None:
    values = [1.0, 2.0, 3.0]
    assert abs(py_score(values) - runtime_score(values)) < 1e-9
