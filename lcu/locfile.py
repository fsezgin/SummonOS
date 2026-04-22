from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LockFile:
    name: str
    pid: int
    port: int
    password: str
    protocol: str

    @classmethod
    def parse(cls, path: Path) -> "LockFile":
        content = path.read_text(encoding="utf-8")
        name, pid, port, password, protocol = content.split(":")
        return cls(
            name=name,
            pid=int(pid),
            port=int(port),
            password=password,
            protocol=protocol,
        )

    @property
    def base_url(self) -> str:
        return f"{self.protocol}://0.0.0.0:{self.port}"