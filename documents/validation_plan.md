# Validation Plan

**Author:** Gloria Kang  
**Date:** June 23, 2025

## Objective

To ensure this GPT-powered primary care agent safely, empathetically, and consistently handles mild and emergency concerns across varied inputs. The goal is to validate language behavior, escalation logic, and patient experience. This assumes unlimited testing resources but remains grounded in the current implementation.

## Validation Strategy

We apply a layered framework to evaluate safety, reliability, and interaction quality.

### Prompt unit tests

Test that outputs follow instruction constraints:

-   Mild cases return exactly 3 numbered recommendations
-   Emergency responses include all required safety disclaimers
-   Disallowed phrases like “don’t worry” do not appear

### Scenario simulation

Run synthetic cases (100+) including:

-   Mild symptoms like headache or fatigue
-   Emergency symptoms like chest pain or shortness of breath
-   Ambiguous, emotional, or edge-case inputs

Evaluate whether the agent classifies correctly, responds appropriately, and maintains empathy

### Robustness testing

Input gibberish, slang, or irrelevant text:

-   Confirm the agent prompts for clarification and repeats the last question
-   Ensure the conversation does not progress until the input is clear

### Human evaluation

Have licensed physicians review agent responses for:

-   Safety and clinical appropriateness
-   Accuracy of escalation
-   Risk of harm or misinformation

Simulated users assess tone, flow, and comfort with the experience

## Success Criteria

-   100% of emergency inputs escalate correctly with all required disclaimers
-   90% or more responses rated clear and empathetic
-   95% of mild cases follow the required numbered recommendation format
-   100% of unclear inputs are flagged and clarified before proceeding

## Future-State Testing

-   Shadow testing alongside physicians in real clinics
-   Fact-checking agent for hallucination detection
-   Latency-tuned triage for safety-critical inputs
