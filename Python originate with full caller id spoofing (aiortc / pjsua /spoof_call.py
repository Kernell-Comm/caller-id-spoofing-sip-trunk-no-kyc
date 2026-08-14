# spoof_call.py
import asyncio
from asterisk.ami import AMIClient, SimpleAction
import os

AMI_HOST = "127.0.0.1"
AMI_USER = "admin"
AMI_PASS = "amp111"
SIP24_TRUNK = "sip24"
DEFAULT_CLI = "18005551212"

async def spoof_call(destination: str, caller_id: str = None, caller_name: str = "Private"):
    cli = caller_id or DEFAULT_CLI
    client = AMIClient(address=AMI_HOST, port=5038)
    client.login(username=AMI_USER, secret=AMI_PASS)

    action = SimpleAction(
        "Originate",
        Channel=f"SIP/{SIP24_TRUNK}/{destination}",
        Context="spoof-out",
        Exten=destination,
        Priority=1,
        CallerID=f"{caller_name} <{cli}>",
        Variable=f"CLI={cli}|CLI_NAME={caller_name}",
        Async="true",
        Timeout="60000"
    )
    client.send_action(action)
    print(f"Spoofed call launched: From {cli} → To {destination}")
    client.logoff()

# Example: change caller id and spoof a call
asyncio.run(spoof_call("15551234567", caller_id="12125551212", caller_name="John Smith"))
