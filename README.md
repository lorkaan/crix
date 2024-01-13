# Password Cracker
This is a password cracker for when I forget my passwords to my Test databases. Currently, it just has the code for cracking hashes used by the default Django database, but it can be easily extended. 

### Disclaimer
This is should only be used against databases you own or have consent to run this on. 

### Notes
It has a Pipfile and Virtual Environment, but does not require it to run at the moment as it does not contain third-party libraries anymore. I kept the Virtual Environment in case of any third-party libraries required in the future.

## Usage

`python crack.py -h` will get you a help screen.

The two arguments are `--hash` and `--password` (or `-p`)

`''hash` takes a list of hashes or filepaths with hashes in them. Files must be delimited by newline characters (\n) and each line can contain a hash or be of the following format ```<username>:<hash>```

`--password` takes a list of filepaths containing passwords. Files must be delimited by newline characters (\n)

E.g
`python crack.py --hash <path_to_hash_file> <hash> --password <path_to_password_file>`

## Future
I need to make the password argument optionally a file or a password string rather than forcing a file. 