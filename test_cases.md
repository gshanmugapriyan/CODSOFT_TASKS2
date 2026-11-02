# Test Cases for Tic-Tac-Toe AI

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| Human wins | Human creates three X symbols in a row | Human wins (Note: Should be impossible against optimal AI) |
| AI wins | AI creates three O symbols in a row | AI wins |
| Draw | All cells are filled without a winner | Draw |
| Invalid move | Human selects an occupied cell | Invalid move message |
| Out of bounds | Human enters a number not in 1-9 | Invalid move message |
| Non-numeric input | Human enters a character | Prompt for valid number |
| Optimal AI | Human tries to force a loss | AI avoids losing |
| Both play optimally | Both players make the best moves | Draw |
