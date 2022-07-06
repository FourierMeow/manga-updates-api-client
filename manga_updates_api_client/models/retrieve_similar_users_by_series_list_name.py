from enum import Enum


class RetrieveSimilarUsersBySeriesListName(str, Enum):
    READ = "read"
    WISH = "wish"
    COMPLETE = "complete"
    UNFINISHED = "unfinished"
    HOLD = "hold"

    def __str__(self) -> str:
        return str(self.value)
