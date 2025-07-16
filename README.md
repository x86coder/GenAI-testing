# GenAI-testing
A few programs tested with the help of Copilot  
Each program has the prefix letter **g** e.g. **g**factorial

## gfactorial(x)
- Prompt: "Output: file containing the code, using PyTest framework style and using just integer numbers for the function. Input: Can you please generate a few test cases for my function gfactorial(x) ?"
- Copilot model: **GPT-4.1**
- Status: PASSED ✅

## gfibonacci(x)
- Prompt: "Output: file containing the resulting code and using PyTest's framework code style. Input: Can you please generate a few test cases (inside a Test Class) for my function gfibonacci(i) ? Context: fibonacci(i) is a function which returns the i-th member (or member number i) in the Fibonacci's sucession. The first member is 0, and the second is 1 in this case."
- Copilot model: **GPT-4.1**
- Status: PASSED ✅

## gbubblesort(csv_param)
- Prompt: "Output: file containing the resulting code and using PyTest's framework code style. Try to include different combinations of numbers (lists). Test edge cases too. Input: Can you please generate a few test cases (inside a Test Class) for my function gbubblesort(list) ?
"
- Copilot model: **GPT-4.1**
- Status: PASSED ✅

## ~~gfibonacci2(x)~~ (work in progres)
- IDE Input: gfibonacci_test.py
- Prompt: "Output: another test class or another generated file. Input: Thanks. aside from that. I feel the test cases in my TestGfibonacci class are brief. Can you wirte more test cases and consider extreme cases and/or edge cases? So I can be sure the function won't break."
- Copilot model: **GPT-4.1**
- Status: ~~(pending)~~

## Installation
- Install Python3
- Get a local working copy (clone)
- Create a virtual env (optional) with `python -m venv myvenv/`
- Switch to venv (optional) with `cd myvenv\scripts` then `activate`
- Run `pip install -r requirements`

## To run the tests
- Type `pytest` on your terminal and every test should be picked by **PyTest**
- Or you can specify test file to be run.