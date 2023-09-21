from thefuzz import fuzz


def fix(
    subtitle: list[str], reference: str | list[str], max_neighbours=5, match_region=500
) -> list[str]:
    """Match words in subtitle to reference text."""

    if isinstance(reference, str):
        reference = reference.split()

    result = []
    actual_index = 0

    for i, _ in enumerate(subtitle):
        best_ratio = 0
        word = ""
        for actual_word in reference[actual_index : actual_index + max_neighbours]:
            if actual_word == subtitle[i]:
                word = actual_word
                actual_index += 1
                break

            new_word = word + " " + actual_word
            remaining_sub = " ".join(subtitle[i + 1 : match_region])
            remaining_ref = " ".join(reference[actual_index + 1 : match_region])
            ratio = fuzz.ratio(remaining_sub, remaining_ref)
            if ratio > best_ratio:
                best_ratio = ratio
                word = new_word
                actual_index += 1
            else:
                break

        result.append(word.strip())

    return result
