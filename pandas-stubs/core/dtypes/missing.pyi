from typing import overload

import numpy as np
from pandas import (
    DataFrame,
    Index,
    Series,
)

from pandas._typing import (
    ArrayLike,
    Scalar,
)

isposinf_scalar = ...
isneginf_scalar = ...

@overload
def isna(obj: DataFrame) -> DataFrame: ...
@overload
def isna(obj: Series) -> Series[bool]: ...
@overload
def isna(obj: Index | list | ArrayLike) -> np.ndarray: ...
@overload
def isna(obj: Scalar) -> bool: ...

isnull = isna

@overload
def notna(obj: DataFrame) -> DataFrame: ...
@overload
def notna(obj: Series) -> Series[bool]: ...
@overload
def notna(obj: Index | list | ArrayLike) -> np.ndarray: ...
@overload
def notna(obj: Scalar) -> bool: ...

notnull = notna
