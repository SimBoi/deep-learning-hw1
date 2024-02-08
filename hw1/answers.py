r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$


"""

part1_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

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


The ideal residual pattern plot would have all the predicted values matching the actual ones, meaning the plot would have all its points at the line $y - \hat{y} = 0$, and the closer and more clustered the points are around the line, the better the model.

The final set of features is better than the top 5 features used before, residual graphs show that margins for the top 
5 features are higher than the margin for the final set of features on average, and also when looking at the maximum margin or farthest prediction from the actual.

"""

part3_q2 = r"""
**Your answer:**


1. Despite incorporating nonlinear features, the model remains linear in its behavior. We're still seeking a weight $W$ to linearly divide the data. The key difference lies in how we engineer the features to better suit a linear separator, but this doesn't fundamentally change the model itself.

2. Yes, technically speaking, we could do that. Imagine $f$ as a function mapping features to real numbers. We could create a new feature by transforming our current features using $f$, then learn a weight $W$ based on this new feature to perfectly fit the data. However, the challenge is that we don't know $f$ beforehand; that's precisely what we're trying to learn. Nonetheless, from a technical perspective, predicting $f$ is possible regardless of the non-linear features.

3. Applying this transformation approach to the previous model would still result in a linear classifier, producing a hyperplane that separates the data. The only difference now is that by incorporating transformations and creating new features, the dimension of the feature space increases. Consequently, the size of the weight matrix ($W$) and the hyperplane it represents also increase. While it's still termed a hyperplane, it exists in a different dimensional space due to the additional features.

"""

part3_q3 = r"""
**Your answer:**


1. Since lambda is directly involved in the computation of $W$, it is expected to have massive effect on it. Therefore we need to take small steps when examining which lamda to use: each step up might lead to big difference in accuracy, so we take small ones in hope of not missing a lambda value that leads to increased accuracy.

2. $3^{degrees}*20^{lambdas}*3^{folds} = 180^{times}$

"""

# ==============

# ==============