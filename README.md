# LLMTestBench: Custom LLM/ML Evaluation Framework

A starter framework for automated evaluation of AI/ML model outputs using LLMs (e.g., GPT-4) as judge models.  
Supports pluggable metrics, judge endpoints (OpenAI/AWS), pytest integration, and reporting.

## Features

- Judge abstraction: OpenAI GPT-4 or custom endpoints (AWS, etc.)
- Pluggable metrics (correctness, risk, relevance, etc.)
- Automated test integration (`pytest`)
- Simple reporting (JSON)

## Quickstart

1. `pip install openai pytest requests`
2. Add your OpenAI API key or endpoint in `tests/test_claim_eval.py`
3. Run sample tests:
    ```
    pytest tests/
    ```

## Extending

- Add more metrics in `llmtestbench/metrics.py`
- Add judge endpoints in `llmtestbench/judge.py`
- Customize reporting in `llmtestbench/report.py`
- Use pytest for workflow automation

## Example

See `tests/test_claim_eval.py` for a sample test that uses GPT-4 to evaluate claim risk prediction correctness, risk, and relevance.

---

Feel free to extend with more metrics (Risk, Relevance, etc.), richer reporting, or workflow integrations.  
PRs and suggestions welcome!
