from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Union,
    overload,
)

import numpy as np
from pandas import Series
from pandas.core.accessor import PandasDelegate as PandasDelegate
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.base import (
    NoNewAttributesMixin as NoNewAttributesMixin,
    PandasObject as PandasObject,
)
from pandas.core.indexes.base import Index

from pandas._typing import (
    ArrayLike,
    Dtype,
    ListLike,
    Ordered,
    Scalar,
    np_ndarray_bool,
    np_ndarray_int,
)

from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype

def contains(cat, key, container): ...

class Categorical(ExtensionArray, PandasObject):
    __array_priority__: int = ...
    def __init__(
        self,
        values: ListLike,
        categories=...,
        ordered: Optional[bool] = ...,
        dtype: Optional[CategoricalDtype] = ...,
        fastpath: bool = ...,
    ) -> None: ...
    @property
    def categories(self): ...
    @categories.setter
    def categories(self, categories) -> None: ...
    @property
    def ordered(self) -> Ordered: ...
    @property
    def dtype(self) -> CategoricalDtype: ...
    def astype(self, dtype: Dtype, copy: bool = ...) -> ArrayLike: ...
    def size(self) -> int: ...
    def itemsize(self) -> int: ...
    def tolist(self) -> List[Scalar]: ...
    to_list = ...
    @classmethod
    def from_codes(
        cls,
        codes: Sequence[int],
        categories: Optional[Index] = ...,
        ordered: Optional[bool] = ...,
        dtype: Optional[CategoricalDtype] = ...,
        fastpath: bool = ...,
    ) -> Categorical: ...
    @property
    def codes(self) -> np_ndarray_int: ...
    @overload
    def set_ordered(self, value, inplace: Literal[True]) -> None: ...
    @overload
    def set_ordered(self, value, inplace: Literal[False]) -> Categorical: ...
    @overload
    def set_ordered(self, value, inplace: bool) -> Union[None, Categorical]: ...
    @overload
    def as_ordered(self, inplace: Literal[True]) -> None: ...
    @overload
    def as_ordered(self, inplace: Literal[False]) -> Categorical: ...
    @overload
    def as_ordered(self, inplace: bool) -> Union[None, Categorical]: ...
    @overload
    def as_unordered(self, inplace: Literal[True]) -> None: ...
    @overload
    def as_unordered(self, inplace: Literal[False] = ...) -> Categorical: ...
    @overload
    def set_categories(
        self, new_categories, ordered=..., rename: bool = ..., *, inplace: Literal[True]
    ) -> None: ...
    @overload
    def set_categories(
        self,
        new_categories,
        ordered=...,
        rename: bool = ...,
        inplace: Literal[False] = ...,
    ) -> Categorical: ...
    @overload
    def set_categories(
        self, new_categories, ordered=..., rename: bool = ..., inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    @overload
    def rename_categories(self, new_categories, inplace: Literal[True]) -> None: ...
    @overload
    def rename_categories(
        self, new_categories, inplace: Literal[False] = ...
    ) -> Categorical: ...
    @overload
    def rename_categories(
        self, new_categories, inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    @overload
    def reorder_categories(
        self, new_categories, ordered=..., *, inplace: Literal[True]
    ) -> None: ...
    @overload
    def reorder_categories(
        self, new_categories, ordered=..., inplace: Literal[False] = ...
    ) -> Categorical: ...
    @overload
    def reorder_categories(
        self, new_categories, ordered=..., inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    @overload
    def add_categories(self, new_categories, inplace: Literal[True]) -> None: ...
    @overload
    def add_categories(
        self, new_categories, inplace: Literal[False] = ...
    ) -> Categorical: ...
    @overload
    def add_categories(
        self, new_categories, inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    @overload
    def remove_categories(self, removals, inplace: Literal[True]) -> None: ...
    @overload
    def remove_categories(
        self, removals, inplace: Literal[False] = ...
    ) -> Categorical: ...
    @overload
    def remove_categories(
        self, removals, inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    @overload
    def remove_unused_categories(self, inplace: Literal[True]) -> None: ...
    @overload
    def remove_unused_categories(
        self, inplace: Literal[False] = ...
    ) -> Categorical: ...
    @overload
    def remove_unused_categories(
        self, inplace: bool = ...
    ) -> Union[None, Categorical]: ...
    def map(self, mapper): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    @property
    def shape(self): ...
    def shift(self, periods, fill_value=...): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs): ...
    @property
    def T(self): ...
    @property
    def nbytes(self) -> int: ...
    def memory_usage(self, deep: bool = ...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    def isna(self) -> np_ndarray_bool: ...
    def isnull(self) -> np_ndarray_bool: ...
    def notna(self) -> np_ndarray_bool: ...
    def notnull(self) -> np_ndarray_bool: ...
    def put(self, *args, **kwargs) -> None: ...
    def dropna(self): ...
    def value_counts(self, dropna: bool = ...): ...
    def check_for_ordered(self, op) -> None: ...
    def argsort(self, ascending: bool = ..., kind: str = ..., *args, **kwargs): ...
    def sort_values(
        self, inplace: bool = ..., ascending: bool = ..., na_position: str = ...
    ): ...
    def view(self, dtype=...): ...
    def to_dense(self): ...
    def fillna(self, value=..., method=..., limit=...): ...
    def take(self, indexer, allow_fill: bool = ..., fill_value=...): ...
    def take_nd(self, indexer, allow_fill: bool = ..., fill_value=...): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def min(self, skipna: bool = ...): ...
    def max(self, skipna: bool = ...): ...
    def mode(self, dropna: bool = ...): ...
    def unique(self): ...
    def equals(self, other): ...
    def is_dtype_equal(self, other): ...
    def describe(self): ...
    def repeat(self, repeats, axis=...): ...
    def isin(self, values): ...
    @overload
    def replace(self, to_replace, value, inplace: Literal[True]) -> None: ...
    @overload
    def replace(self, to_replace, value, inplace: Literal[False]) -> Categorical: ...
    @overload
    def replace(
        self, to_replace, value, inplace: bool = ...
    ) -> Union[None, Categorical]: ...

class CategoricalAccessor(PandasDelegate, PandasObject, NoNewAttributesMixin):
    def __init__(self, data) -> None: ...
    @property
    def codes(self) -> Series[int]: ...
    @property
    def categories(self) -> Index: ...
    @property
    def ordered(self) -> Optional[bool]: ...
    def rename_categories(
        self, new_categories: Union[ListLike, Dict[Any, Any], Callable[[Any], Any]]
    ) -> Series: ...
    def reorder_categories(
        self,
        new_categories: ListLike,
        ordered: bool = ...,
    ) -> Series: ...
    def add_categories(self, new_categories: Union[Scalar, ListLike]) -> Series: ...
    def remove_categories(self, removals: Union[Scalar, ListLike]) -> Series: ...
    def remove_unused_categories(self) -> Series: ...
    def set_categories(
        self,
        new_categories: ListLike,
        ordered: Optional[bool] = ...,
        rename: bool = ...,
    ) -> Series: ...
    def as_ordered(self) -> Series: ...
    def as_unordered(self) -> Series: ...

def factorize_from_iterable(values): ...
def factorize_from_iterables(iterables): ...
