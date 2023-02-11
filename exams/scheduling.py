jobs = [[int(n), i] for i, n in enumerate(input().split(', '))]
target_job_index = int(input())

target_job = jobs[target_job_index]

jobs = sorted(jobs)

target_job_index = jobs.index(target_job)

cycles = jobs[:target_job_index + 1]

print(sum([n[0] for n in cycles]))
