# rotate_cli.py
import random
from spoof_call import spoof_call

CLI_LIST = [
    "18005551212",
    "12125551212",
    "13105551212",
    # add hundreds from your sip24.cc allowed list
]

async def campaign(destinations):
    for dest in destinations:
        cli = random.choice(CLI_LIST)
        await spoof_call(dest, caller_id=cli)
        await asyncio.sleep(1.5)  # pace control
