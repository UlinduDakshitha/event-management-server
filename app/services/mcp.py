from datetime import datetime, timezone

def send_draft_via_mcp(email_address: str, email_body: str):
    utc_time = datetime.now(timezone.utc).isoformat()

    print("----- MCP DRAFT SENT -----")
    print(f"Recipient: {email_address}")
    print("Body:")
    print(email_body)
    print(f"UTC Timestamp: {utc_time}")
    print("--------------------------")