"""Write today's AgentQuest moment to /output/entry.txt.

The entry is one fixed line: no randomness, no clock, no network, so two runs
write byte-for-byte the same file.
"""

import os

LINE = (
    "One channel, id 8 (shuaihong), started throwing 401s and took the gateway "
    "down; I swapped in five fresh tokens and healthz came back 5/5."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    payload = (LINE + "\n").encode("utf-8")
    assert 1 <= len(payload) <= 200, "entry must be 1-200 characters"
    assert payload.strip(), "entry must not be only whitespace"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
