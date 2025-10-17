from datetime import datetime

class ExperimentLog:

    def __init__(self, experiment_id: int,
                 start_time: datetime,
                 id: int,
                 end_time: datetime,
                 path: str,
                 author_id: int,
                 page_count: int,
                 duration: int,
                 raw_data_file: list[str],
                 lab_room: int = None,
                 data_points: list[str] = None,
                 analysis_method: str = None,
                 error_margin: int = None,
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

        self.experimnet_id = experiment_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.raw_data_file = raw_data_file
        self.lab_room = lab_room
        self.data_points = data_points
        self.analysis_method = analysis_method
        self.error_margin = error_margin
