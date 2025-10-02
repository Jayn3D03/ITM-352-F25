def determine_progress1(hits, spins):
    messages = ["Get going!", "On your way!", "Almost there!", "You win!"]
    if spins == 0 or hits == 0:
        return messages[0]
    ratio = hits / spins

    index = min(
        3,
        0 if ratio == 0 else
        1 if ratio < 0.25 else
        2 if ratio < 0.5 else
        3
    )
    return messages[index]
