import uuid
from typing import final
from syft.proto import ProtoUID
from syft.decorators.syft_decorator_impl import syft_decorator
uuid_type = type(uuid.uuid4())

@final
class AbstractUID(object):
    """This exists to allow us to typecheck on the UID object

    |

    """


@final
class UID(AbstractUID):
    """This object creates a unique ID for every object in the Syft
    ecosystem. This ID is guaranteed to be unique for the node on
    which it is initialized and is very likely to be unique across
    the whole ecosystem (because it is long and randomly generated).

    Nearly all objects within Syft subclass from this object because
    nearly all objects need to have a unique ID. The only major
    exception a the time of writing is the Client object because it
    just points to another object which itself has an id.

    There is no other way in Syft to create an ID for any object.

        - **parameters**, **types**, **return** and **return types**::

            :param arg1: description
            :param arg2: description
            :type arg1: type description
            :type arg1: type description
            :return: return description
            :rtype: the return type description

        - and to provide sections such as **Example** using the double commas syntax::

              :Example:

              followed by a blank line !

        which appears as follow:

        :Example:

        followed by a blank line

        - Finally special sections such as **See Also**, **Warnings**, **Notes**
          use the sphinx syntax (*paragraph directives*)::

              .. seealso:: blabla
              .. warnings also:: blabla
              .. note:: blabla
              .. todo:: blabla

        .. note::
            There are many other Info fields but they may be redundant:
                * param, parameter, arg, argument, key, keyword: Description of a
                  parameter.
                * type: Type of a parameter.
                * raises, raise, except, exception: That (and when) a specific
                  exception is raised.
                * var, ivar, cvar: Description of a variable.
                * returns, return: Description of the return value.
                * rtype: Return type.

        .. note::
            There are many other directives such as versionadded, versionchanged,
            rubric, centered, ... See the sphinx documentation for more details.

        Here below is the results of the :func:`function1` docstring.


    |


    """

    @syft_decorator(typechecking=True)
    def __init__(self, value: uuid_type = None):
        """This initializes the object. Normal use for this object is
        to initialize the constructor with value==None because you
        want to initialize with a novel ID. The only major exception
        is deserialization, wherein a UID object is created with a
        specific id value.

        :param value: if you want to initialize an object with a specific UID, pass it in here. This is normally only used during deserialization.
        :type value: uuid.uuid4(), optional
        :return: returns the initialized object
        :rtype: UID

        .. code-block:: python

            from syft.core.common.uid import UID
            my_id = UID()
            print(my_id.value)

        .. code-block:: bash

            >>> 8d744978-327b-4126-a644-cb90bcadd35e

        |

        """

        # if value is not set - create a novel and unique ID.
        if value is None:

            # for more info on how this UUID is generated:
            # https://docs.python.org/2/library/uuid.html
            value = uuid.uuid4()

        # save the ID's value. Note that this saves the uuid value
        # itself instead of saving the
        self.value = value

    @syft_decorator(typechecking=True)
    def __hash__(self) -> int:
        """A very common use of UID objects is as a key in a dictionary
        or database. The object must be able to be hashed in order to
        be used in this way. We take the 128-bit int representation of the
        value.

        :param value (uuid): if you want to initialize an object with a specific UID, pass it in here. This is normally only used during deserialization.
        :param arg2: description
        :type arg1: type description
        :type arg1: type description
        :return: return description
        :rtype: the return type description

        .. note::
            Note that this probably gets further hashed into a shorter
            representation for most python data-structures.

        .. note::
            Note that we assume that any collisions will be very rare and
            detected by the ObjectStore class in Syft.

    |

    """


        return self.value.int

    @syft_decorator(typechecking=True)
    def __eq__(self, other: AbstractUID) -> bool:
        """This checks to see whether this UID is equal to another UID by
        comparing whether they have the same .value objects. These objects
        come with their own __eq__ function which we assume to be correct.

    |

    """

        if isinstance(other, UID):
            return self.value == other.value

        return False

    def __repr__(self):
        return f"<UID:{self.value}>"

    def serialize(self):
        return ProtoUID(value=self.value.bytes)

    @staticmethod
    def deserialize(proto_uid: ProtoUID) -> AbstractUID:
        return UID(value=uuid.UUID(bytes=proto_uid.value))