from .ops import *
from mygrad.tensor_base import Tensor

__all__ = ["sum",
           "mean",
           "amax",
           "amin",
           "max",
           "min",
           "prod",
           "cumprod",
           "cumsum"]


def sum(x, axis=None, keepdims=False):
    """ Sum of tensor elements over a given axis.

        Parameters
        ----------
        x : Union[numpy.ndarray, mygrad.Tensor]

        axis : Optional[int, Tuple[ints, ...]
            Axis or axes along which a sum is performed.  The default,
            axis=None, will sum all of the elements of the input tensor.  If
            axis is negative it counts from the last to the first axis.
            If axis is a tuple of ints, a sum is performed on all of the axes
            specified in the tuple instead of a single axis or all the axes as
            before.

        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the input tensor.

        Returns
        -------
        sum_along_axis : Tensor
            A Tensor with the same shape as `self`, with the specified
            axis/axes removed. If `self` is a 0-d tensor, or if `axis` is None,
            a 0-dim Tensor is returned."""
    return Tensor._op(Sum, x, op_args=(axis, keepdims))


def mean(x, axis=None, keepdims=False):
    """ Mean of tensor elements over a given axis.

        Parameters
        ----------
        x : Union[numpy.ndarray, mygrad.Tensor]

        axis : Optional[int, Tuple[ints, ...]
            Axis or axes along which a mean is performed.  The default,
            axis=None, will mean all of the elements of the input tensor.  If
            axis is negative it counts from the last to the first axis.

            If axis is a tuple of ints, a mean is performed on all of the axes
            specified in the tuple instead of a single axis or all the axes as
            before.

        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the input tensor.

        Returns
        -------
        mean_along_axis : Tensor
            A Tensor with the same shape as `self`, with the specified
            axis/axes removed. If `self` is a 0-d tensor, or if `axis` is None,
            a 0-dim Tensor is returned."""
    return Tensor._op(Mean, x, op_args=(axis, keepdims))


def amax(x, axis=None, keepdims=False):
    """ Return the maximum of a tensor or maximum along its axes.

        Parameters
        ----------
        x : Union[numpy.ndarray, mygrad.Tensor]

        axis : Optional[int, Tuple[int, ...]]
            Axis or axes along which to operate. By default, flattened input is used.

        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the original `arr`.

        Returns
        -------
        max : Tensor
            Maximum of `a`. If `axis` is None, the result is a 0-D tensor."""
    return Tensor._op(MaxMin, x, op_kwargs=dict(axis=axis, keepdims=keepdims, maxmin='max'))


def amin(x, axis=None, keepdims=False):
    """ Return the minimum of a tensor or minimum along its axes.

        Parameters
        ----------
        axis : Optional[int, Tuple[int, ...]]
            Axis or axes along which to operate. By default, flattened input is used.

        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the original `arr`.

        Returns
        -------
        min : Tensor
            Minimum of `a`. If `axis` is None, the result is a 0-D tensor."""
    return Tensor._op(MaxMin, x, op_kwargs=dict(axis=axis, keepdims=keepdims, maxmin='min'))

# aliases
min = amin
max = amax


def prod(a, axis=None, keepdims=False):
    return Tensor._op(Prod, a, op_kwargs=dict(axis=axis, keepdims=keepdims))


def cumprod(a, axis=None):
    """
    Return the cumulative product of elements along a given axis.

    This docstring was adapted from the official numpy documentation

    Parameters
    ----------
    a : array_like
        Input array.

    axis : Optional[int]
        Axis along which the cumulative product is computed.  By default
        the input is flattened.

    Returns
    -------
    mygrad.Tensor

    Notes
    -----
    Arithmetic is modular when using integer types, and no error is
    raised on overflow.

    Examples
    --------
    >>> from mygrad import cumprod, Tensor
    >>> a = Tensor([1, 2, 3])
    >>> cumprod(a) # intermediate results 1, 1*2
    ...               # total product 1*2*3 = 6
    Tensor([1, 2, 6])

    The cumulative product for each column (i.e., over the rows) of `a`:

    >>> cumprod(a, axis=0)
    Tensor([[ 1,  2,  3],
           [ 4, 10, 18]])

    The cumulative product for each row (i.e. over the columns) of `a`:

    >>> cumprod(a,axis=1)
    Tensor([[  1,   2,   6],
           [  4,  20, 120]])"""

    return Tensor._op(CumProd, a, op_kwargs=dict(axis=axis))


def cumsum(a, axis=None):
    """
    Return the cumulative sum of the elements along a given axis.

    This docstring was adapted from the official numpy documentation

    Parameters
    ----------
    a : array_like
        Input array.

    axis : int, optional
        Axis along which the cumulative sum is computed. The default
        (None) is to compute the cumsum over the flattened array.

    Returns
    -------
    mygrad.Tensor


    Examples
    --------
    >>> from mygrad import cumsum, Tensor
    >>> a = Tensor([[1,2,3], [4,5,6]])
    >>> a
    Tensor([[1, 2, 3],
            [4, 5, 6]])
    >>> cumsum(a)
    Tensor([ 1,  3,  6, 10, 15, 21])

    >>> cumsum(a,axis=0)      # sum over rows for each of the 3 columns
    Tensor([[1, 2, 3],
            [5, 7, 9]])
    >>> cumsum(a,axis=1)      # sum over columns for each of the 2 rows
    Tensor([[ 1,  3,  6],
            [ 4,  9, 15]])
    """

    return Tensor._op(CumSum, a, op_kwargs=dict(axis=axis))