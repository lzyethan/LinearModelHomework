import test as p

"""
Created on Sun Feb 19 18:38:39 2017
@author: Christine lee and Wadood Chaudhary
"""

def test_rent():
    if (p.score_rent() > 0.05):
        return 1
    else:
        return 0

if __name__ == "__main__":
    if test_rent()==1:
        print("The model is good, and return me a good result!")
    else:
        print("The result is not good as I expected")