def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"

    hits_spins_ratio = hits / spins

    if hits_spins_ratio == 0:
        return "Get going!"
    elif hits_spins_ratio < 0.25:
        return "On your way!"
    elif hits_spins_ratio < 0.5:
        return "Almost there!"
    elif hits < spins:
        return "You win!"


def test_determine_progress(progress_function):
    assert progress_function(10, 0) == "Get going!" , "test case 1 failed"
    assert progress_function(2, 5) == "Almost there!" , "test case 2 failed"
    assert progress_function(1, 4) == "Almost there!" , "test case 3 failed"
    assert progress_function (1, 7) == "On your way!", "test case 4 failed"
    assert progress_function(5, 8) == "You win!", "test case 5 failed"
    assert progress_function(4, 7) == "You win!", "test case 6 failed"

test_determine_progress(determine_progress3)


    