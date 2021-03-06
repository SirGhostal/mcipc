"""Stuff, common to Query and RCON."""

from socket import SOCK_STREAM, socket, SocketKind  # pylint: disable=E0611


__all__ = ['BaseClient']


class BaseClient:
    """A basic client."""

    def __init__(self, host: str, port: int, typ: SocketKind = SOCK_STREAM):
        """Sets host an port."""
        self._socket = socket(type=typ)
        self.host = host
        self.port = port

    def __enter__(self):
        """Conntects the socket."""
        self._socket.__enter__()
        self.connect()
        return self

    def __exit__(self, typ, value, traceback):
        """Delegates to the underlying socket's exit method."""
        self.close()
        return self._socket.__exit__(typ, value, traceback)

    @property
    def socket(self) -> tuple:
        """Returns a tuple of host and port."""
        return (self.host, self.port)

    def connect(self):
        """Conntects to the RCON server."""
        return self._socket.connect(self.socket)

    def close(self):
        """Disconnects from the RCON server."""
        return self._socket.close()
