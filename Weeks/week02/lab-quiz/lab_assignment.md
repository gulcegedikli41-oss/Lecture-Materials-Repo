# Week 2 Lab: Two-Item Purchase Quote

## Task

Create `lab02_purchase_quote.py`. Ask for two item names, quantities, unit prices, a delivery fee and a tax percentage. Calculate each line, subtotal, tax and final total. Apply tax to the item subtotal, then add the delivery fee.

## Acceptance Checks

1. Use `int()` for quantities and `float()` for money input.
2. Print money with two decimal places.
3. Test with 2 × 50 and 1 × 80, delivery 20, tax 10%. Expected total: 218.00 TRY.
4. Explain why `input()` must be converted before arithmetic.

## Stretch Task

Try typing letters for a quantity. Note the error message and describe how a later version could handle it.

## GitHub Submission

1. Create `week02/lab-quiz/` in your own course repository and save `lab02_purchase_quote.py` there. Keep weekly homework in `week02/` outside this folder.
2. Add a short README note with one test you ran and one thing you changed after testing.
3. Commit with a specific message, such as `week02: complete two-item purchase quote`.
4. Show the running program and your commit history to the instructor.

## Assessment (10 Points)

- Working behavior and required rules: 5
- Meaningful tests, including a boundary or error case: 2
- Readable names and clear output: 2
- GitHub commit and README note: 1
