from datetime import datetime

class Report:
    
    chart_types = {
        'bar', 'line', 'pie', 'scatter',
        'histogram', 'area', 'bubble',
        'heatmap', 'radar', 'boxplot'
    }

    def __init__(self, summary: str = None,
                 result_summary: str = None,
                 reviewer_comments: list[str] = None,
                 reviewer_rating: str = None,
                 reviewer_text: str = None,
                 review_date: datetime = None,
                 chart_type: str = None,
                 chart_date: dict = None,
                 insight_summary: str = None
                 ):
        
        self.summary = summary
        self.result_summary = result_summary
        self.reviewer_comments = reviewer_comments
        self.reviewer_comments = reviewer_rating
        self.reviewer_text = reviewer_text
        self.review_date = review_date
        self.chart_type = chart_type
        self.chart_date = chart_date
        self.insight_summary = insight_summary


    @property
    def chart_type(self):
        return self._chart_type

    @chart_type.setter
    def chart_type(self, value):
        if value not in self.chart_types:
            raise ValueError(f'Недопустимый статус: {value}')
        self._chart_type = value