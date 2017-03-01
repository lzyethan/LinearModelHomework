1. Explain how you validated your model and why    
   I use R^2 to validate my model, which compare the predicated value and the true value of testing data.
   If the R^2 value is high, it means the predicated value and true value have big difference
   If the R^2 value is low, it means the predicated value and true value have small difference. Which means the prediction mdoel is good.
   To validate the model, I set 0.2 as the threshold to determine the model is good or not.

2. The model is based on linear regression for the prediction

3. There are two files:
	1) homework2_rent.py with two functions: score_test and predict_rent
	2) test_rent.py with a function test_rent to call the score_test in homework2_rent.py
