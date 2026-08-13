from datetime import datetime

def message(message, force_uppercase_full, force_uppercase_partial):
    if force_uppercase_full:
        message = message.upper()
    elif force_uppercase_partial:
        message = message.title()
    else:
        message = message.lower()
    return message

message_original = input("What is your message? ")
message_partial = message(message_original, False, True)
message_upper = message(message_original, True, False)
message_lower = message(message_original, False, False)

print()
print(f"{message_partial}\n")
print(f"{message_upper}\n")
print(f"{message_lower}\n")
