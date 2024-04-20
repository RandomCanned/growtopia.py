import pytest
import growtopia

from os import chdir, path

chdir(path.abspath(path.dirname(__file__)))

    
def test_protocol() -> None:
    packet = growtopia.Packet(growtopia.PacketType.HELLO)
    assert packet.pack() == bytearray([1,0,0,0])

if __name__ == "__main__":
    test_protocol()
