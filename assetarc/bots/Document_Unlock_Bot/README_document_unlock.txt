
Document Unlock Bot

This bot handles the secure unlocking of structured documents based on token and session validation.

Setup Instructions:
1. Place this bot in its own folder (e.g., Document_Unlock_Bot).
2. Ensure Flask is installed (`pip install flask`).
3. The `unlocked/` directory must contain approved PDFs named as {session_id}_document.pdf.
4. Run the bot with: python document_unlock.py
5. Send a POST request to /unlock-document with JSON:
   {
     "token": "client-access-token",
     "session_id": "generated-session-id"
   }

Returns: The unlocked PDF document or error.
