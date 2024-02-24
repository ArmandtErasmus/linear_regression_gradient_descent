# Linear Regression with Gradient Descent

Implementation of a gradient descent algorithm to minimize a cost-function $J(w,b)$ in order to find the optimal weight (w) and bias (b) fitting parameters for a linear fit.

# Introduction

Linear regression is a supervised machine learning model that is used to produce an estimate value based on input features. The linear regression model used is given by

$$f_{w,b}(x)=wx+b$$

where $w$ and $b$ respectfully are the weight and bias parameters. The associated cost-function is given by

$$J(w,b)=\frac{1}{2n}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^{2}$$

# The Gradient Descent Algorithm

The aim is to find values of $w,b$ such that $J(w,b)$ is minimized. This is achieved by repeating the following algorithm until convergence

$$w = w - \alpha\frac{\partial}{\partial w}J(w,b)$$
$$b = b - \alpha\frac{\partial}{\partial b}J(w,b)$$

where $\alpha$ is the learning rate. 


