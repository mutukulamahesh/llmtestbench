class Evaluator:
    def __init__(self, metrics, judge):
        self.metrics = metrics
        self.judge = judge

    def evaluate(self, predictions, references):
        results = []
        for pred, ref in zip(predictions, references):
            scores = {
                metric.__class__.__name__: metric.score(pred, ref, self.judge)
                for metric in self.metrics
            }
            results.append(scores)
        return results
