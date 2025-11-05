def format_number_with_suffix(num):
    if not isinstance(num, (int, float)) or num < 0:
        raise ValueError("Input must be a non-negative number")

    if num >= 1e12:  # Trillion
        return f"{num / 1e12:.1f}T"
    elif num >= 1e9:  # Billion
        return f"{num / 1e9:.1f}B"
    elif num >= 1e6:  # Million
        return f"{num / 1e6:.1f}M"
    elif num >= 1e3:  # Thousand
        return f"{num / 1e3:.1f}K"
    else:
        return str(int(num))