# GenAI-testing
A few programs tested with the help of Copilot
Each program has the prefix letter **g** e.g. **g**factorial

## gfactorial(x)
- Definition: [Wikipedia](https://en.wikipedia.org/wiki/Factorial)
- PROMPT: **Output: file containing the code, using PyTest framework style and using just integer numbers for the function. Input: Can you please generate a few test cases for my function gfactorial(x) ?**
- Copilot model: **GPT-4.1**
- Status: PASSED ✅

## Installation
- Install Python3
- Get a local working copy (clone)
- Create a virtual env (optional) with `python -m venv myvenv/`
- Switch to venv (optional) with `cd myvenv\scripts` then `activate`
- Run `pip install -r requirements`

## To run the tests
- Type `pytest` on your terminal and every test should be picked by **PyTest**