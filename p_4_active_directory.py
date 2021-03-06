'''
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
'''

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def print(self, indent=0):
        print('{}Group [{}]'.format(' '*indent, self.name))
        print('{} Users: {}'.format(' '*indent, ', '.join(self.users)))
        for group in self.groups:
            group.print(indent=indent+1)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(Group("child2"))

parent.print()

# Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name() or user in group.get_users():
        return True
    for g in group.get_groups():
        return is_user_in_group(user, g)
    return False

print(is_user_in_group('sub_child_user', parent)) 
print(is_user_in_group('', parent)) 
print(is_user_in_group('child', parent)) 
print(is_user_in_group('sub_child_user', sub_child)) 
print(is_user_in_group('child', child)) 