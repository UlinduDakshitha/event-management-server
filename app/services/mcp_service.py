from datetime import (
    datetime,
    timezone
)

from app.core.logger import logger

def send_draft_via_mcp(
    email,
    body
):

    timestamp = (
        datetime.now(
            timezone.utc
        ).isoformat()
    )

    logger.info(
        f"""
Recipient:
{email}

Timestamp:
{timestamp}

Body:
{body}
"""
    )