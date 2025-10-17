from datetime import datetime

class ExperimentLog:

    def __init__(self, experiment_id: int,
                 start_time: datetime,
                 end_time: datetime,
                 duration: int,
                 raw_data_file: list[str],
                 lab_room: int = None,
                 data_points: list[str] = None,
                 analysis_method: str = None,
                 error_margin: int = None
                 ):
        
        self.experimnet_id = experiment_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.raw_data_file = raw_data_file
        self.lab_room = lab_room
        self.data_points = data_points
        self.analysis_method = analysis_method
        self.error_margin = error_margin
