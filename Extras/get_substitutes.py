l1 = ["a","b","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c","a","b","c"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
l1 = le.fit_transform(l1)
print(l1)