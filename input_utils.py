def normalize_remainder_input(user_input):
    user_input = user_input.replace(" ", "").lower()
    if 'r' in user_input:
        parts = user_input.split('r')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return f"{int(parts[0])} r{int(parts[1])}"
    return user_input