# Human Review Queue Bot

## Overview
This bot collects sessions flagged for human review. Admins can fetch pending reviews, approve them, or remove them from the queue.

## Endpoints
- `POST /submit_for_review`: Adds a review entry.
- `GET /get_pending_reviews`: Lists all pending reviews.
- `POST /approve_review/<index>`: Approves and removes review at the given index.

## Files
- `human_review_queue_bot.py`: Main app logic
- `pending_reviews.json`: Storage for pending reviews

## Usage
1. Run the Flask app.
2. Use endpoints to manage human review workflow.
