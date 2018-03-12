from name_function import get_formatted_name

print("********Press Q to Quit!!!!!********")
while True:
    first = input("Enter the first Name:")
    if first == "q":
        break
    last = input("Enter the last Name:")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly Formatted Name: " + formatted_name + ".")