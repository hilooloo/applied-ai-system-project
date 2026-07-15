# Model Card: Game Glitch Investigator

## 1. AI Collaboration
- I collaborated with AI by using it to refactor my Python code, implement the logging module, and design the RAG (Retrieval-Augmented Generation) retrieval function. AI helped me structure the error handling (guardrails) to ensure the system is user-friendly.

## 2. AI Suggestions: Helpful vs. Flawed
- **Helpful**: The AI provided a clean way to implement the `logging` module and suggested a robust `try-except` structure to manage empty inputs.
- **Flawed**: The AI occasionally suggested library versions that were incompatible with my local environment or recommended file paths that I had to manually correct to match my actual folder structure.

## 3. System Limitations
- **Limited Scope**: The system currently relies on keyword matching. It cannot understand complex, natural language questions that deviate from the keyword list.
- **Data Dependency**: The knowledge base ('glitch_knowledge.txt') is small and requires manual updates. It does not learn automatically from new user inputs.
- **Ethics**: The system does not collect personal user data, only functional logs, ensuring user privacy.
