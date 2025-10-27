class CloudStorage:
    def __init__(self, provider: str, bucket_name: str, access_key: str) -> None:
        self.provider: str = provider
        self.bucket_name: str = bucket_name
        self.access_key: str = access_key
