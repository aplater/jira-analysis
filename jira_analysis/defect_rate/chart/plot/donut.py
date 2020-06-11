import attr

from bokeh.models.sources import DataSource
from math import pi
from typing import List, Type

from jira_analysis.defect_rate.issue import Issue


@attr.s
class DefectRateDonut:
    issues: List[Issue] = attr.ib()
    data_source: Type[DataSource] = attr.ib()

    def to_data_source(self):
        num_issues = len(self.issues)
        issues_with_defects = len([i for i in self.issues if i.defects])
        defect_rate = issues_with_defects / num_issues
        no_defect_rate = 1 - defect_rate
        return self.data_source(
            {
                "issues": [num_issues, issues_with_defects],
                "defect_rate": [no_defect_rate, defect_rate],
                "value": ["Issues", "Defect Rate"],
                "angle": [_get_angle(no_defect_rate), _get_angle(defect_rate)],
                "color": ["green", "red"],
            }
        )


def _get_angle(percentage: float) -> float:
    return percentage * pi
