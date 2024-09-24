# SUI wallets conveter

1. Install [Python 3+](https://www.python.org/downloads/)
2. Install [Sui CLI](https://docs.sui.io/guides/developer/getting-started/sui-install)
3. Choose format convert to (`SAVE` constant 1 or 2 or 3, default 1)
```
Examples:
╭──────────┬─────────────────┬──────────────────────────────────────────────────────────────────────────╮
│ SAVE = 1 │  bech32WithFlag │  suiprivkey1qqdc0fe87kyrpkd690lxanwgldy649h69g4mu967z29lacfldz2l766z9q2  │
│ SAVE = 2 │  base64WithFlag │  ABuHpyf1iDDZuiv+bs3I+0mqlvoqK74XXhKL/uE/aJX/                            │
│ SAVE = 3 │  hexWithoutFlag │  1b87a727f58830d9ba2bfe6ecdc8fb49aa96fa2a2bbe175e128bfee13f6895ff        │
╰──────────┴─────────────────┴──────────────────────────────────────────────────────────────────────────╯
```
5. Fill `wallets.txt` with your private keys
6. Run `convert.py`

After run will be generated output file with all converted private keys.

