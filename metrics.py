class CorrectnessMetric:
    def score(self, prediction, reference, judge):
        prompt = (
            f"Evaluate the correctness of the following prediction compared to the reference.\n"
            f"Prediction: {prediction}\nReference: {reference}\n"
            f"Return a score between 0 (incorrect) and 1 (fully correct)."
        )
        result = judge.evaluate(prompt)
        try:
            return float(result)
        except (TypeError, ValueError):
            if "correct" in str(result).lower():
                return 1.0
            return 0.0

class RiskMetric:
    def score(self, prediction, reference, judge):
        prompt = (
            f"Given the prediction and reference, rate the risk assessment quality (0=poor, 1=excellent).\n"
            f"Prediction: {prediction}\nReference: {reference}"
        )
        result = judge.evaluate(prompt)
        try:
            return float(result)
        except (TypeError, ValueError):
            if "high" in str(result).lower():
                return 1.0
            return 0.0

class RelevanceMetric:
    def score(self, prediction, reference, judge):
        prompt = (
            f"Does the prediction address the main aspect of the reference? "
            f"Return a score 0 (not relevant) to 1 (fully relevant).\n"
            f"Prediction: {prediction}\nReference: {reference}"
        )
        result = judge.evaluate(prompt)
        try:
            return float(result)
        except (TypeError, ValueError):
            if "relevant" in str(result).lower():
                return 1.0
            return 0.0
