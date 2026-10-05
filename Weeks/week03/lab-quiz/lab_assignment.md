# Week 3 Lab: Order Approval Policy

## Task

Create `lab03_order_approval.py`. Ask for order amount, available stock, requested quantity and whether the customer is a member. Reject invalid quantities or insufficient stock. Give members a 10% discount on approved orders of at least 500 TRY.

## Acceptance Checks

1. Test just below, exactly at and above 500 TRY.
2. A rejected order shows no final price.
3. A valid order displays the reason for approval and its final price.
4. Use `if`, `elif` or `else` and at least one logical operator.

## Stretch Task

Write a small test table in your README with the inputs and expected result for three boundary cases.

## GitHub Submission

1. Create `week03/lab-quiz/` in your own course repository and save `lab03_order_approval.py` there. Keep weekly homework in `week03/` outside this folder.
2. Add a short README note with one test you ran and one thing you changed after testing.
3. Commit with a specific message, such as `week03: complete order approval policy`.
4. Show the running program and your commit history to the instructor.

## Assessment (10 Points)

- Working behavior and required rules: 5
- Meaningful tests, including a boundary or error case: 2
- Readable names and clear output: 2
- GitHub commit and README note: 1
