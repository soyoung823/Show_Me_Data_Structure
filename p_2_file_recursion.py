'''
Finding Files
For this problem, the goal is to write code for finding all files under a directory 
(and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. 
However, for this problem you are not allowed to use os.walk().

Here is some code for the function to get you started:
'''
import os

def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

  Returns:
      a list of paths
  """
  # Recursion
  result = []

  if not bool(path):
    return []

  if not bool(suffix):
    suffix = None

  if os.path.isdir(path): # if the current path is a file
    if path.endswith(suffix): # if the file has extension suffix='.c'
      result.append(path)
  else:
    children = os.listdir(path)
  
    for child in children:
      full_path = os.path.join(path, child)

      if os.path.isdir(full_path):
        result += find_files(suffix, full_path)
      elif os.path.isfile(full_path) and full_path.endswith(suffix):
        result.append(full_path)

  return result
  '''
  # Iterative
  result = []
  nodesToExpand = [path]  # stack

  while nodesToExpand:
    full_path = nodesToExpand.pop()
    if os.path.isfile(full_path) and full_path.endswith(suffix):
      result.append(full_path)
    elif os.path.isdir(full_path):
      for child in os.listdir(full_path):
        nodesToExpand.append(os.path.join(full_path, child))
  return sorted(result)
  '''


if __name__ == '__main__':
  print(find_files('.c', './testdir'))
  

# Test cases
print(find_files('_2.py', '.'))
print(find_files('', ''))
print(find_files('.c', None))
print(find_files('.c', './testdir'))
print(find_files('.h', './testdir'))

path = "./p_2_file_recursion.py"
suffix = ".py"
print(find_files(suffix, path))
