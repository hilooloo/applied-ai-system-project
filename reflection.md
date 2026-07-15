# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 50 (Secret: 85)| Should display "Go Higher" since 50 is less than 85. | Displayed "Go LOWER" | none |
| Guess of 90 (Secret: 85)| Should display "Go Lower" since 90 is less than 85. | Displayed "Go HIGHER" | none |
| Guess of 20 (Secret: 85)| Should display "Go Higher" since 20 is less than 85. | Displayed "Go LOWER" | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Answer: I used the VS Code AI coding assistant Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Answer: The AI pointed out the inverted hint bug in 'logic_utils.py' where "Too High" was paired with "Go HIGHER". It suggested swapping the messages to the correct directions, and I verified it by checking the code and running the game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Answer: When raw 'pytest' failed due to Windows environment path issues, the AI suggested modifying system PATH variables or reinstalling pytest. However, I found a much simpler workaround by running 'python -m pytest' directly in the terminal, which worked perfectly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Answer: I decided the bug was fixed only when the automated tests('pytest') passed completely and I manually verified that the Streamlit UI hints perfectly matched the secret numbers during actual gameplay.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
Answer: I ran 'python -m pytest' in the terminal, and all 3 test cases passed successfully in 0.04 seconds. This proved that our internal calculation logic was completely fixed and accurate.
- Did AI help you design or understand any tests? How?
Answer: Yes, the AI helped me understand how the test code uses mocking to simulate game states. It visually explained how the higher/lower conditions are validated, which made it easy to see how our code changes interacted with the tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
