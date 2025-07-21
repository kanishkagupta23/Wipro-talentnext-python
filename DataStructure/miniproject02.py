#Given a list of participant scores for your University Sports Day, determine the score of the runner-up (the second highest unique score)

# List of scores
scores = [2, 3, 6, 6, 5]

# Remove duplicates and sort in descending order
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

# The runner-up score is the second element
runner_up = unique_scores[1]

print(runner_up)