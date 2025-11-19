def generate_profile(age):
    """Определяет жизненный этап на основе возраста"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"