# copy of https://github.com/dbrgn/result
# MIT licensed
from __future__ import print_function, division, absolute_import, unicode_literals


class Result(object):
    """
    A simple `Result` type inspired by Rust.
    Not all methods (https://doc.rust-lang.org/std/result/enum.Result.html)
    have been implemented, only the ones that make sense in the Python context.
    You still don't get any type checking done.
    """

    def __init__(self, force=False):
        if force is not True:
            raise RuntimeError("Don't instantiate a Result directly. "
                               "Use the Ok(value) and Err(error) class methods instead.")

    def __eq__(self, other):
        return self._type == other._type and self._val == other._val

    def is_ok(self):
        return self._type == 'ok'

    def is_err(self):
        return self._type == 'error'

    def __bool__(self):
        return self.is_ok()

    __nonzero__ = __bool__

    def ok(self):
        """
        Return the value if it is an `Ok` type. Return `None` if it is an `Err`.
        """
        return self._val if self.is_ok() else None

    def err(self):
        """
        Return the error if this is an `Err` type. Return `None` otherwise.
        """
        return self._val if self.is_err() else None

    @property
    def value(self):
        """
        Return the inner value. This might be either the ok or the error type.
        """
        return self._val

    # TODO: Implement __iter__ for destructuring
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{}({})".format(self._type.title(), repr(self._val))


class Ok(Result):

    def __init__(self, value=True):
        super(Ok, self).__init__(force=True)
        self._val = value
        self._type = 'ok'


class Skip(Ok):

    def __init__(self, value=True):
        super(Skip, self).__init__(value)


class Err(Result):

    def __init__(self, value=True):
        super(Err, self).__init__(force=True)
        self._val = value
        self._type = 'error'
