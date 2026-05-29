from datetime import datetime, timezone


def send_draft_via_mcp(email_address: str, email_body: str):
    print("=== MCP DRAFT LOG ===")
    print(f"Recipient: {email_address}")
    print(f"Timestamp (UTC): {datetime.now(timezone.utc).isoformat()}")
    print("Body:")
    print(email_body)
    print("=====================")