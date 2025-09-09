import pytest
from llmtestbench.judge import GPTJudge
from llmtestbench.metrics import CorrectnessMetric, RiskMetric, RelevanceMetric
from llmtestbench.evaluator import Evaluator

def test_claim_risk():
    # Use your OpenAI key or AWS endpoint here
    judge = GPTJudge(api_key="YOUR_OPENAI_KEY", endpoint=None)
    metrics = [CorrectnessMetric(), RiskMetric(), RelevanceMetric()]
    evaluator = Evaluator(metrics, judge)
    predictions = ["High risk due to missing docs."]
    references = ["Incorrect, docs are complete."]
    results = evaluator.evaluate(predictions, references)
    assert results[0]['CorrectnessMetric'] >= 0.5
    assert results[0]['RiskMetric'] >= 0.5
    assert results[0]['RelevanceMetric'] >= 0.5
