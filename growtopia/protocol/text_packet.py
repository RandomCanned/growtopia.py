__all__ = ("TextPacket",)

from typing import Optional, Union

import enet

from ..enums import EventID
from ..error_manager import ErrorManager
from ..exceptions import PacketTypeDoesNotMatchContent
from .packet import Packet, PacketType


class TextPacket(Packet):
    """
    Represents a text packet. A packet that contains text. Uses the Packet class as a base.

    Parameters
    ----------
    data: Optional[Union[bytes, Packet]]
        The raw data of the packet.

    Attributes
    ----------
    text: str
        The text of the packet.

    """

    def __init__(self, data: Optional[Union[bytes, enet.Packet]] = None) -> None:
        super().__init__(data)

        self.type: PacketType = PacketType.TEXT
        self.text: str = ""

        if len(self.data) >= 4:
            self.deserialise()

    def serialise(self) -> bytes:
        """
        Serialise the packet.

        Returns
        -------
        bytes
            The serialised packet.

        Raises
        ------
        NotImplementedError
            This method must be implemented in the child class.
        """

        self.data = bytearray(int.to_bytes(self.type, 4, "little"))
        self.data += self.text.encode("utf-8") + (
            b"\n" if not self.text.endswith(b"\n") else b""
        )

        return self.data

    def deserialise(self, data: Optional[bytes] = None) -> None:
        """
        Deserialise the packet.

        Parameters
        ----------
        data: Optional[bytes]
            The data to deserialise. If this isn't provided,
            the data attribute will be used instead.

        Raises
        ------
        NotImplementedError
            This method must be implemented in the child class.
        """

        if data is None:
            data = self.data

        if len(data) >= 4:
            self.type = PacketType(int.from_bytes(data[:4], "little"))

            if self.type != PacketType.TEXT:
                ErrorManager._raise_exception(PacketTypeDoesNotMatchContent(self))

            self.text = data[4:-1].decode("utf-8")

    def identify(self) -> EventID:
        """
        Identify the packet based on its contents.

        Returns
        -------
        EventID
            The event ID responsible for handling the packet.
        """
        if "requestedName" in self.text:
            return EventID.ON_REQUEST_LOGIN
