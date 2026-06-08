import json
import os
import struct
import sys

COLOR_MODES = {
    0: "Bitmap",
    1: "Grayscale",
    2: "Indexed",
    3: "RGB",
    4: "CMYK",
    7: "Multichannel",
    8: "Duotone",
    9: "Lab",
}


def read_payload():
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    return json.loads(raw)


def resolve_path(value):
    if not value or not isinstance(value, str):
        raise ValueError("path is required")
    expanded = os.path.expanduser(value)
    if os.path.isabs(expanded):
        return expanded
    working_dir = os.environ.get("LOCUS_WORKING_DIR") or os.getcwd()
    return os.path.abspath(os.path.join(working_dir, expanded))


def parse_header(file_path):
    with open(file_path, "rb") as handle:
        header = handle.read(26)
    if len(header) < 26:
        raise ValueError("file is too small to contain a PSD header")
    signature = header[0:4].decode("ascii", errors="replace")
    if signature != "8BPS":
        raise ValueError("not a PSD/PSB file: missing 8BPS signature")
    version, channels, height, width, depth, color_mode = struct.unpack(">H6xHIIHH", header[4:26])
    if version not in (1, 2):
        raise ValueError(f"unsupported PSD version: {version}")
    return {
        "path": file_path,
        "signature": signature,
        "version": version,
        "format": "PSB" if version == 2 else "PSD",
        "channels": channels,
        "height": height,
        "width": width,
        "depth": depth,
        "colorMode": color_mode,
        "colorModeName": COLOR_MODES.get(color_mode, "Unknown"),
        "fileSizeBytes": os.path.getsize(file_path),
    }


def main():
    try:
        payload = read_payload()
        file_path = resolve_path(payload.get("path") or payload.get("filePath"))
        result = parse_header(file_path)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False, indent=2), file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
