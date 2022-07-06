from enum import Enum


class SearchMemberChangeRequestsOrderby(str, Enum):
    SCORE = "score"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
