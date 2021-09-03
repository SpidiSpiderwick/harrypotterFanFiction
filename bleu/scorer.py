from nltk.translate.bleu_score import sentence_bleu, corpus_bleu, SmoothingFunction
from nltk import word_tokenize


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    lines = [word_tokenize(x) for x in lines]

    indices = [i for i, x in enumerate(lines) if x == []]
    prev_index = 0
    result = []
    for index in indices:
        result.append(lines[prev_index:index])
        prev_index = index + 1
    result.append(lines[prev_index:])
    result = [x for x in result if x != []]

    return result


def absatzweise(references, candidate):
    for ref in references:
        if len(ref) != len(candidate):
            raise Exception("references-candidate-mismatch")
    return [corpus_bleu(list(map(list, zip(*[ref[index] for ref in references]))),
                        can_absatz,
                        smoothing_function=SmoothingFunction().method4)
            for index, can_absatz in enumerate(candidate)]


def gesamt(references, candidate):
    for ref in references:
        if len(ref) != len(candidate):
            raise Exception("references-candidate-mismatch")
    new_refs = [[[token for line in ref[index] for token in line] for ref in references] for index, _ in enumerate(references[0])]
    new_cands = [[token for line in can_absatz for token in line] for can_absatz in candidate]
    return new_refs, new_cands, corpus_bleu(new_refs, new_cands)


if __name__ == '__main__':
    references = [read_file(path) for path in ("ina.txt", "ina.txt")]
    candidate = read_file("mTurk.txt")

    scores = absatzweise(references, candidate)

    token_anzahl = [sum(len(line) for line in absatz) for index, absatz in enumerate(candidate)]
    token_gesamt = sum(token_anzahl)

    weighted_scores = [score * tok_a / token_gesamt for score, tok_a in zip(scores, token_anzahl)]
    avg_score = sum(weighted_scores)

    ges_refs, ges_cands, ges_score = gesamt(references, candidate)

    print(f"scores:\t\t\t{scores}\nweighted scores:{weighted_scores}\n\n weighted_score_sum: {avg_score}\n\n"
          f"gesamtcorpusscore: {ges_score}")

