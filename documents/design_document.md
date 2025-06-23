# Primary Care Agent Design Document

**Author:** Gloria Kang  
**Date:** June 23, 2025

## Overview

This AI system simulates a primary care consultation for patients and replaces routine visits while ensuring safe escalation when needed. The goal is to reduce physician load, improve access, and maintain patient trust.

## Primary Care Appointment Flow

The agent simulates four core stages of a primary care appointment, where a patient reports a concern. It adapts its logic and language based on severity of symptoms and the patient’s expressed level of concern.

### Intake

-   Greets the patient and prompts for symptoms
-   Asks: “When did this first start, and has it been getting better, worse, or staying the same?”

### Assessment

-   Analyzes input to determine whether symptoms suggest a mild or emergency scenario
-   For emergencies:
    -   Uses: “Based on what you’ve told me…” and “Here’s what I recommend…”
    -   Includes required safety language and escalates to in-person care
-   For mild symptoms:
    -   Continues to self-care recommendations

### Recommendation

-   If mild:
    -   Validates pain with: “That sounds really uncomfortable”
    -   Asks: “What concerns you most about this?”
    -   Provides 3 numbered self-care steps
    -   Ends with: “How does this sound to you?”
-   If emergency:
    -   Clearly escalates and provides urgent care directions

### Follow-up / Close

-   For mild symptoms:
    -   Includes a follow-up timeframe: “If this isn’t improving in [x] days, please contact a healthcare provider.”
-   For emergency symptoms:
    -   Recommends immediate in-person care
-   If the patient has no additional concerns, the agent closes the visit with: “Take care, and feel free to reach out if anything changes.”

## Agent Behavior Design

### Core Behavior

-   Acknowledges concerns with: “I understand”
-   Asks for timeline per symptom
-   Responds to pain with: “That sounds really uncomfortable.”
-   Responds to concern with: “It’s completely understandable that you’re concerned about [symptom]”
-   Avoids medical jargon
-   Never says “don’t worry”
-   Before any recommendation, asks: “What concerns you most about this?”
-   Ends every recommendation with: “How does this sound to you?”

### Mild Symptom Flow

-   Offers 3 numbered self-care steps
-   Includes a follow-up time window
-   Ends with closing language

### Emergency Symptom Flow

-   Uses structured escalation format:
    -   “Based on what you told me…”
    -   “Here’s what I recommend…”
    -   “This is beyond what I can safely assess remotely”
    -   “I can provide guidance, but I cannot replace an in-person examination”
    -   Includes urgent next steps

### Escalation Logic

-   Triggers when keywords indicate danger (e.g., chest pain, difficulty breathing)
-   Follows a strict format: Acknowledge → Recommend → Disclaim → End Visit Check

### Unclear Input Handling

-   If input is unclear, irrelevant, or not understandable:
    -   Responds with: “I’m sorry I didn’t quite catch that. [Repeat last question]?”
    -   Does not advance the conversation until input is clarified

## System Design & Architecture

-   **LLM**: GPT-4o via OpenAI API
-   **System Instructions**: A ~500-word prompt encodes all required linguistic and behavioral constraints

### Interaction Flow

```
[Patient Input (CLI)]
        ↓
[System Prompt Layer (LLM Instructions)]
        ↓
[LLM (GPT-4o) Response Generation]
        ↓
[Agent Response Displayed to User]
        ↓
[Conversation Turn Appended to Session]
        ↓
[Transcript Saved to File (End of Session)]
```

### Session Memory Flow

```
[Conversation History (User + Agent Turns)]
       ↘               ↙
[System Prompt + GPT-4o Response Generation]
        ↓
[Agent Response Displayed to User]
```

-   The system is stateless and runs in the terminal.
-   Maintains in-memory session history and saves full transcripts to the `conversations/` folder upon exit.
-   Prioritizes simplicity, safety, and low-latency interaction.

## Patient Experience Design

-   **Tone**: Calm, friendly, and accessible
-   **Empathy Protocols**:
    -   Pain: “That sounds really uncomfortable”
    -   Worry: “It’s completely understandable that you’re concerned about [symptom]”
    -   No false reassurance
-   **Trust Building**:
    -   Includes safety disclaimers
    -   Uses consistent language structure
    -   Ends with “How does this sound to you?” to invite feedback

## Key Limitations

-   No access to vitals, labs, or EHR data
-   May produce inaccurate responses in edge cases
-   Lacks persistent memory
-   No HIPAA-compliant data security

## Future Improvements

-   Confidence scoring for uncertainty calibration
-   Guardrail agent for high-risk output review
-   Detailed audit logging for oversight and traceability
-   HIPAA-compliant storage and encryption
-   Persistent memory for continuity
-   Clinician dashboard for case review and overrides
