from pathlib import Path


path1 = Path()
for file in path1.glob('*.py'):
    print(file)
