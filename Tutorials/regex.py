import re
mystr = """I would like to test some function in the new tensorflow2.3 However, I am struggling with installation process.

I saw: How do I install the most recent Tensorflow (here: 2.2) on Windows when conda does not yet support it?

I executed: pip install --upgrade pip

I got:

ERROR: Could not find a version that satisfies the requirement tensorflow-cpu==2.3.0rc2 (from versions: 1.15.0rc0, 1.15.0rc1, 1.15.0rc2, 1.15.0rc3, 1.15.0, 2.1.0rc0, 2.1.0rc1, 2.1.0rc2, 2.1.0)
ERROR: No matching distribution found for tensorflow-cpu==2.3.0rc2
tensorflow
pip
tensorflow2

findall, search, split, sub, finditer
"""
pattern = re.compile(r"flow$ ")
matches = pattern.finditer(mystr)
for match in matches :
    print(match)
