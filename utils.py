def normalize_score(score):
    try:
        score = float(score)
        if score < 0:
            return 0.0
        if score > 1:
            return 1.0
        return score
    except Exception:
        return 0.0
