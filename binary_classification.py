from math import exp
def classifyBinary(feature_vector, weight_vector, classes):
    wx = 0
    for i in range(len(feature_vector)):
        wx += feature_vector[i] * weight_vector[i]

    p = 1/(1+exp(-wx))
    if p < 0.5:
        y = 0
    else:
        y = 1

    return classes[y]