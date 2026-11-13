import math


def parse_booking(text):
    if not isinstance(text, str):
        return None

    parts = text.split(":")
    if len(parts) != 2:
        return None

    pet, days_text = parts
    pet = pet.strip()

    if not pet:
        return None

    try:
        days = float(days_text)
    except (ValueError, OverflowError):
        return None

    if not math.isfinite(days) or days < 0:
        return None

    return pet.title(), days


def stay_average(days_csv):
    if not isinstance(days_csv, str):
        return None

    parts = days_csv.split(",")

    try:
        values = [int(part.strip()) for part in parts]
    except ValueError:
        return None

    if any(value < 0 for value in values):
        return None

    try:
        average = sum(values) / len(values)
    except OverflowError:
        return None

    if not math.isfinite(average):
        return None

    return average


def payable_fee(text):
    if not isinstance(text, str):
        return None

    parts = text.split("|")
    if len(parts) != 2:
        return None

    try:
        fee, discount = [float(part) for part in parts]
    except (ValueError, OverflowError):
        return None

    if not math.isfinite(fee) or not math.isfinite(discount):
        return None

    if fee < 0 or discount < 0:
        return None

    total = fee * 1.18 - discount

    if not math.isfinite(total):
        return None

    return max(total, 0.0)


def show_result(label, result):
    if result is None:
        print("Invalid input. Please check the required format and values.")
    else:
        print(label, result)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter pet:days (e.g. dog:5): ")
    show_result("Pet and Days:", parse_booking(user_input))

    print("\n==== Running stay_average ====")
    user_input = input(
        "Enter stay lengths in days as CSV (e.g. 2,5,7): "
    )
    show_result("Average Stay:", stay_average(user_input))

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 1500|100): ")
    show_result("Payable Fee:", payable_fee(user_input))


if __name__ == "__main__":
    main()