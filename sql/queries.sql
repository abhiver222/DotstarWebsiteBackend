# Login
Select Count(*) From Users 
Where NetId=netid And UIN=uin;

# Selecting all tasks for a user
Select * From Task
Where AssignedUser = netid Or CompletedUser = netid
Order By EndTime;

# Selecting all tasks for a team
Select * From Task
Where AssignedUser In (
    Select NetId From TeamMembers
    Where Company = company And Team = team)
Or CompletedUser In (
    Select NetId From TeamMembers
    Where Company = company And Team = team)
)
Order By EndTime;

# Selecting all tasks for a company
Select * From Task
Where AssignedUser In (
    Select NetId From TeamMembers
    Where Company = company)
Or CompletedUser In (
    Select NetId From TeamMembers
    Where Company = company)
)
Order By EndTime;

# Selecting netids of all users on team
Select NetId From TeamMembers
Where Company = company And Team = team;

# Selecting netids of all users on company
Select NetId From TeamMembers
Where Company = company;

