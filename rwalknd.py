from random import choice
dim=3
trials=100
steps=10000
gothome=0
for i in range(trials):
    point=[0]*dim
    for step in range(steps):
        for j in range(dim):
            point[j]+=choice((-1,1))
        if point.count(0)==dim:
            gothome+=1
            break
print("Fraction that got home=%f in %d dims" % (gothome/trials,dim))

# In dim=2, the fraction that got home was 0.78.  In dim=3, the fraction that got home was 0.31.  Thus, the walker does not get home in all dimensions.