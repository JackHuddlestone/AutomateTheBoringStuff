from pathlib import Path

dir = Path.cwd()
nonExistentDir = Path('/home/pi/Documents/Chocolate/Donuts/Are/Horrible')

print(dir.exists())
print(dir.is_dir())
print(nonExistentDir.exists())
