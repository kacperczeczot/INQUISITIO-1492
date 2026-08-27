#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DIR/../.." && pwd)"

# Include paths for Apple Clang and Python3
PYTHON_INCLUDE="$(python3 -c "import sysconfig; print(sysconfig.get_paths()['include'])" 2>/dev/null || echo "")"
SDK_HEADERS="/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Headers"

INCLUDES=""
if [ -d "$PYTHON_INCLUDE" ]; then
    INCLUDES="$INCLUDES -I$PYTHON_INCLUDE"
fi
if [ -d "$SDK_HEADERS" ]; then
    INCLUDES="$INCLUDES -I$SDK_HEADERS"
fi

echo "🔨 Kompilacja inquisitio_native (C++20, -O3)..."
clang++ -std=c++20 -O3 -fPIC -shared -undefined dynamic_lookup \
    $INCLUDES \
    "$DIR/inquisitio_native.cpp" \
    -o "$ROOT_DIR/sim/inquisitio_native.so"

echo "✅ Zbudowano pomyślnie: $ROOT_DIR/sim/inquisitio_native.so"
