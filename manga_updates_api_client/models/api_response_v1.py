from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_response_v1_context import ApiResponseV1Context
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiResponseV1")


@attr.s(auto_attribs=True)
class ApiResponseV1:
    """
    Attributes:
        status (str):
        reason (str):
        context (Union[Unset, ApiResponseV1Context]):
    """

    status: str
    reason: str
    context: Union[Unset, ApiResponseV1Context] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        reason = self.reason
        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "reason": reason,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        reason = d.pop("reason")

        _context = d.pop("context", UNSET)
        context: Union[Unset, ApiResponseV1Context]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = ApiResponseV1Context.from_dict(_context)

        api_response_v1 = cls(
            status=status,
            reason=reason,
            context=context,
        )

        api_response_v1.additional_properties = d
        return api_response_v1

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
