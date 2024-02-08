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

The choice of $\Delta > 0$ in the SVM loss function $L(\mat{W})$ is arbitrary because any change in its value can be compensated by a proportional adjustment in the weight matrix $\mat{W}$. If we multiply $\Delta$ by a positive constant, we can also multiply the weight matrix $\mat{W}$ by the same constant. This results in all margin losses being scaled by the same factor, leaving the maximum value unchanged. This is because the outcome is not affected by scaling the weight matrix with any positive scalar.

"""

part2_q2 = r"""
**Your answer:**

The linear model is learning to identify subspaces of pixels where the projection of vectors onto these subspaces yields a high value for the correct class. Some classification errors can be observed in instances where the samples have a high projection onto the subspace of an incorrect class.

"""

part2_q3 = r"""
**Your answer:**

1. The chosen learning rate appears to be optimal as the model exhibits good convergence. If the learning rate was too low, the model would either converge very slowly or not at all. Conversely, if the learning rate was too high, the model would either diverge or show fluctuations.

2. The model seems to be slightly overfitting, as evidenced by its high accuracy and low loss on the training set compared to a slightly lower accuracy and slightly higher loss on the test set.

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
