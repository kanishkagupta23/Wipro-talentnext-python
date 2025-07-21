#Given a list of participant scores for your University Sports Day, determine the score of the runner-up (the second highest unique score)

scores = [1, 3, 4, 4, 9]

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)


runner_up = unique_scores[1]

print(runner_up)
