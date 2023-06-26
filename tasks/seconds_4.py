"""
Написать функцию, которая выводит словесное описание длительности, выраженной в секундах,
используя слова ‘year(s)’, ‘day(s)’, ‘hour(s)’, ‘minute(s)’ и ‘second(s)’.
"""

def get_seconds_to_text_representation(seconds: int) -> str:
    """
    Convert timespan representation in seconds to text
    Examples:
         f(3665) => "1 hour, 1 minute, 5 seconds"
    """
    years = seconds // (365 * 24 * 60 * 60)
    days = (seconds // (24 * 60 * 60)) % 365
    hours = (seconds // (60 * 60)) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    representation = []
    if years > 0:
        representation.append(f"{years} {'year' if years == 1 else 'years'}")
    if days > 0:
        representation.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours > 0:
        representation.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes > 0:
        representation.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds > 0:
        representation.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    if len(representation) == 0:
        return "0 seconds"
    elif len(representation) == 1:
        return representation[0]
    else:
        return ", ".join(representation)


if __name__ == '__main__':
    print(get_seconds_to_text_representation(3665))
    print(get_seconds_to_text_representation(223443665))
