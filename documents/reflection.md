# Reflection

**Author:** Gloria Kang  
**Date:** June 23, 2025

## Key Limitations

One core limitation is that the system has no access to real patient data like vitals, test results, or medical records. While the system reliably simulates empathy and structured reasoning, it is limited to typed input and lacks integration with real-world clinical data. It also does not retain memory between sessions unless state is passed manually, which limits continuity. Like any LLM, it can still produce confident but inaccurate responses, especially when inputs are vague or unexpected.

## How I Would Improve the System

I propose adding confidence scoring so the system can recognize uncertainty and adjust tone or escalate when needed. I would implement a separate guardrail agent to review high-risk responses in real time and review mild cases asynchronously. Audit logging would capture each step of the conversation for supervision, transparency, and model improvement. With more time, I would integrate a symptom checker API or structured triage logic to improve reliability when input is ambiguous.

## What Surprised Me

I was surprised by how much nuance could be coded into a single prompt. The model reliably followed empathy and safety rules with no special infrastructure. It also surprised me that GPT does not store memory between turns unless manually managed, which made me think more carefully about safe design in longer-term patient use.
