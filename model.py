import joblib, os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# load sample data
iris = load_iris()
X, y = iris.data, iris.target

# Train sample model
model = RandomForestClassifier()
model.fit(X, y)

# Save model in environment
if not os.path.exists("./model"): os.mkdir("./model")
joblib.dump(model,'model/model.joblib')