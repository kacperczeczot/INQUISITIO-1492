"""Type stub for inquisitio_native C++ extension module."""
from typing import Any, Dict, Optional

def run_batch(
    games: int = 1000,
    setup: str = "4p-core",
    seed: int = 42,
    threshold: int = 7,
    layer: str = "C",
    win_overrides: Optional[Dict[str, int]] = None,
    threads: int = 0,
) -> Dict[str, Any]: ...

def benchmark(games: int = 100000) -> Dict[str, float]: ...
