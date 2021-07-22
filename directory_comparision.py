import os
import sys
import hashlib

compromised="compromised"
original="original"
walk_dir = compromised
"""print('walk_dir = ' + walk_dir)
print("walk_dir(absolute)=" + os.path.abspath(walk_dir))
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))"""

for root, subdirs, files in os.walk(walk_dir):
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    with open(list_file_path, 'wb') as list_file:
         for filename in files:
            compromised_file_path = os.path.join(root, filename)
            original_file_path=compromised_file_path.replace(compromised,original)
            try:
                compromised_md5=hashlib.md5(open(compromised_file_path,'r').read().encode('utf-8'))
                original_md5=hashlib.md5(open(original_file_path,'r').read().encode('utf-8'))
                if (compromised_md5.hexdigest() != original_md5.hexdigest()):
                    print("[*] Modified File:\t%s\t%s" , compromised_file_path)
            except(Exception):
                print("newly file created detected" , compromised_file_path)

            with open(compromised_file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')

