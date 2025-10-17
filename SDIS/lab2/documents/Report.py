from datetime import datetime

class Report:
    
    chart_types = {
        'bar', 'line', 'pie', 'scatter',
        'histogram', 'area', 'bubble',
        'heatmap', 'radar', 'boxplot'
    }

    def __init__(self, path: str,
                 id: int,
                 author_id: int,
                 page_count: int,
                 summary: str = None,
                 result_summary: str = None,
                 reviewer_comments: list[str] = None,
                 reviewer_rating: str = None,
                 reviewer_text: str = None,
                 review_date: datetime = None,
                 chart_type: str = None,
                 chart_date: dict = None,
                 insight_summary: str = None,
                 title: str = None,
                 desc: str = None,
                 created_at: datetime = None, 
                 updated_at: datetime = None,
                 tags :str = None,
                 keywords: str = None,
                 language: str = None,
                 word_count: int = None,
                 confidentiality_level: str = 'public',
                 status: str = 'draft'
                 ):
        
        super().__init__(
                 id=id,
                 author_id=author_id,
                 page_count=page_count,
                 path=path,
                 title=title,
                 desc=desc,
                 created_at=created_at, 
                 updated_at=updated_at,
                 tags=tags,
                 keywords=keywords,
                 language=language,
                 word_count=word_count,
                 confidentiality_level=confidentiality_level,
                 status=status
                 )
        
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