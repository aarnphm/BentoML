from typing import Any

logger: Any

def is_s3_url(url): ...
def create_s3_bucket_if_not_exists(bucket_name, region) -> None: ...