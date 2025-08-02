
import json
import datetime

def generate_newsletter(content, audience_segment, tone='professional'):
    subject = f"Asset Protection Insights – {datetime.date.today().strftime('%B %d, %Y')}"
    header = f"Hi {audience_segment}, here’s your weekly dose of strategic structuring."
    footer = "To your legacy,

The AssetArc Team"
    body = f"Subject: {subject}\n\n{header}\n\n{content}\n\n{footer}"
    return body

def log_campaign_result(campaign_name, open_rate, click_through_rate, conversion_rate):
    result = {
        "campaign": campaign_name,
        "open_rate": open_rate,
        "click_through_rate": click_through_rate,
        "conversion_rate": conversion_rate,
        "date": str(datetime.date.today())
    }
    with open("newsletter_metrics.json", "a") as f:
        f.write(json.dumps(result) + "\n")

if __name__ == "__main__":
    sample = generate_newsletter("Today's topic: Tax Efficiency via Holding Structures.", "Founders")
    print(sample)
    log_campaign_result("Week_31_Tax_Efficiency", 0.42, 0.12, 0.05)
