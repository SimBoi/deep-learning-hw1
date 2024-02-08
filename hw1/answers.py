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