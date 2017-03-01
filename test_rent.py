import homework2_rent as h


def test_rent():
    if (h.score_rent() < 0.2):
        return 1
    else:
        return 0

if __name__ == "__main__":
    if test_rent()==1:
        print("The model is good, and return me a good prediction result!")
    else:
        print("The result is not good as I expected")