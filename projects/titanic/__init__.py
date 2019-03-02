from sklearn.ensemble import VotingClassifier, BaggingClassifier, GradientBoostingClassifier, AdaBoostClassifier

gb = GradientBoostingClassifier(n_estimators=500,random_state=0)

ada = AdaBoostClassifier(n_estimators=200,learning_rate=0.1,random_state=0)
