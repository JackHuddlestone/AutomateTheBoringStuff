from pathlib import Path

#list files in systemd for example
p = Path('/lib/systemd')
for fileObj in p.glob('systemd-s*'): # find all systemmd files which begin with s
    print(f'FILE FOUND - {fileObj}')