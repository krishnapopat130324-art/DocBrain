from storage import add_document, load_documents
from checker import check_status
from plyer import notification


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )


def add_new_document():
    print("\nAdd New Document")
    name = input("Document Name: ").strip()
    number = input("Document Number: ").strip()
    expiry = input("Expiry Date (YYYY-MM-DD or DD-MM-YYYY): ").strip()
    notes = input("Notes (optional): ").strip()

    add_document(name, number, expiry, notes)
    print("✅ Document added successfully!\n")


def view_documents():
    documents = load_documents()

    if not documents:
        print("\nNo documents found.\n")
        return

    print("\n📄 DOCUMENT STATUS\n")

    for doc in documents:
        status, days_left = check_status(doc["expiry"])

        if status == "INVALID":
            print(f"❌ {doc['name']} - Invalid date saved")

        elif status == "OVERDUE":
            msg = f"{doc['name']} expired {-days_left} days ago"
            print(f"❌ {msg}")
            send_notification("Document Expired ❌", msg)

        elif status == "EXPIRING SOON":
            msg = f"{doc['name']} expires in {days_left} days"
            print(f"⚠ {msg}")
            send_notification("Document Expiry Alert ⚠", msg)

        else:
            print(f"✅ {doc['name']} - Safe ({days_left} days left)")

    print()


def main():
    while True:
        print("===== IMPORTANT DOCUMENT EXPIRY MONITOR =====")
        print("1. Add new document")
        print("2. View document status")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_new_document()
        elif choice == "2":
            view_documents()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
