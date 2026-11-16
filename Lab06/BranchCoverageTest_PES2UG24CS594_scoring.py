from spam_scoring import score_message


def test_known_sender_with_positive_score():
    assert score_message("free winner prize", True, 0) == 3