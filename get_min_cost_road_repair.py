def getMinCost(crew_id, job_id):
    # Write your code here
    crew_id.sort()
    job_id.sort()
    s=0
    for i in range(len(crew_id)):
        x=job_id[i]-crew_id[i]
        s+=abs(x)
    return s
crew_id=[5,3,1,4,6]
job_id=[9,3,1,15,8]
print(getMinCost(crew_id, job_id))