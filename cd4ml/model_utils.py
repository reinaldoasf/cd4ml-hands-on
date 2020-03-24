from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from cd4ml.ml_model_params import model_params


def get_model_class_and_params(model_name):
    model_classes = {
        'random_forest': RandomForestRegressor,
        'adaboost': AdaBoostRegressor,
        'gradient_boosting': GradientBoostingRegressor,
        'decision_tree': DecisionTreeRegressor
    }
    return model_classes[model_name], model_params[model_name]