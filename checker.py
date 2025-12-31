from datetime import datetime, date


def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def check_status(expiry_date_str):
    expiry_date = parse_date(expiry_date_str)

    if expiry_date is None:
        return "INVALID", None

    today = date.today()
    days_left = (expiry_date - today).days

    if days_left < 0:
        return "OVERDUE", days_left
    elif days_left <= 30:
        return "EXPIRING SOON", days_left
    else:
        return "SAFE", days_left
