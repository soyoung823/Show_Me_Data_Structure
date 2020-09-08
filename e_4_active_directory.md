1. Problem explanations
The goal is to construct the hierarchy which consist of users and groups. Where user is represented by str representing their id.

2. Complexity explanations
Time Complexity:
group.get_name(): O(1) since the lookup and get the name takes constant time.
group.get_users(): O(1) since the lookup and get the name takes constant time.
group.get_groups(): O(1) since the lookup and get the name takes constant time.
recursive is_user_in_group(user, g): Assume that the depth of tree is m, the time complexiy if O(m)
Thus, total time complexity is O(m)

Space complexity: O(n) since the implementation uses arrays groups and users.
