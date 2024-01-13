from django_hasher import DjangoHasher
import os
import argparse


def is_file_path(path):
    if os.path.isfile(path):
        return True
    elif os.path.isdir(path):
        raise Exception("Expected File or Hash, got nothing")
    else:
        return False
    

"""
Simple CLI for this cracking script. If this gets 
more complex with more Hasher classes, increase the complexity
of this CLI Code.
"""

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some variables for cracking')
    parser.add_argument(
        '--hash', nargs="+",
        help="The hash(s) or file(s) with hashes to check. Files must be delimited by \\n characters and may have usernames in the format <username>:<hash>"
    )
    parser.add_argument("--password", "-p", nargs="+",
        help="The file(s) with passwords to check against. Files must be delimited by the \\n character"
    )
    args = parser.parse_args()

    for cur_hash in args.hash:
        try:
            file_flag = is_file_path(cur_hash)
            hash_flag = not file_flag
        except Exception as e:
            print(e)
            file_flag = False
            hash_flag = False
        finally:
            if file_flag:
                with open(cur_hash, 'r') as hash_file:
                    line = hash_file.readline()
                    while line:
                        if line.endswith('\n'):
                            line = line[0:-1]
                        line_parts = line.split(":", 1)
                        if len(line_parts) == 2:
                            cur_user = line_parts[0]
                            cur_hash = line_parts[1]
                        else:
                            cur_hash = line_parts[0]
                            cur_user = None
                        for passfile in args.password:
                            try:
                                pass_file_flag = is_file_path(passfile)
                            except Exception as e:
                                print(e)
                                pass_file_flag = False
                            finally:
                                if pass_file_flag:
                                    cur = DjangoHasher.find_hash(passfile, cur_hash)
                                    if cur_user == None:
                                        print(f"Password: {cur}\tHash: {cur_hash}")
                                    else:
                                        print(f"Password: {cur}\t: Username: {cur_user}")
                                else:
                                    continue
                        line = hash_file.readline()
            elif hash_flag:
                for passfile in args.password:
                    try:
                        pass_file_flag = is_file_path(passfile)
                    except Exception as e:
                        print(e)
                        pass_file_flag = False
                    finally:
                        if pass_file_flag:
                            cur = DjangoHasher.find_hash(passfile, cur_hash)
                            print(f"Password: {cur}\tHash: {cur_hash}")
                        else:
                            continue
            else:
                continue
