class Chart:

    chart_types = {
        'bar', 'line', 'pie', 'scatter'
    }

    def __init__(self, chart_id: int, title: str, chart_type: str, data: dict) -> None:
        self.chart_id: int = chart_id
        self.title: str = title
        self.chart_type: str = chart_type
        self.data: dict = data

    @property
    def chart_type(self):
        return self._chart_type

    @chart_type.setter
    def chart_type(self, value):
        if value not in self.chart_types:
            raise ValueError(f'Недопустимый статус: {value}')
        self._chart_type = value