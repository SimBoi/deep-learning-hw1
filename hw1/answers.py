r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. false -> The in-sample error is calculated using the same dataset that was used to train the classifier, not the test set. This estimation tends to be more optimistic compared to the error rate derived from the test set.

2. false -> The error rate estimation from the holdout method can be deceptive if we end up with a split that is not representative or "unlucky".

3. true -> Otherwise, the error will be more optimistic than the actual error, as the classifier is partially built on the test samples themselves.

4. true -> Each validation set in every fold is separate from the training set within the same fold. This ensures that the error from each fold is generalized. Consequently, the average error across all folds, which is also generalized, is obtained.

"""

part1_q2 = r"""
**Your answer:**

No, it's not justified. The test set was utilized during the training of the classifier to approximate the best hyperparameter value. This makes the error appear more optimistic than the actual error. Even if it's not overfitting, the model is still not generalized.

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**


"""

part2_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
