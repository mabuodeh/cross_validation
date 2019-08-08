import pytest

from sklearn.utils.estimator_checks import check_estimator

from cyber_deception import TemplateEstimator
from cyber_deception import TemplateClassifier
from cyber_deception import TemplateTransformer


@pytest.mark.parametrize(
    "Estimator", [TemplateEstimator, TemplateTransformer, TemplateClassifier]
)
def test_all_estimators(Estimator):
    return check_estimator(Estimator)
