from django_hasher import DjangoHasher

if __name__ == '__main__':

    hash_text1 = "$pbkdf2_sha256$600000$pZXnd7tjgluPNorbdctsMi$B9Cjs5U3Bcq6kmO9Py9fzG+b/1QibcVcadoc8w6tiXA="
    hash_text2 = "$pbkdf2_sha256$600000$gVctVjtcvyJBJ0vrj0ep7r$qVc361m/45Q8k/d2Ez6sDS5Yzgo1LrAE67wO0FA4XoI="
    hash_text3 = "$pbkdf2_sha256$600000$zv4Jl40jFrglYL81LS70DL$qxvrdqBzrrty4qBjlo8lqJCBhV16EsYm8BdK+wkNEPs="

    filepath = "./secret_codes.txt"

    hashs = {
        "admin2": hash_text1,
        "testuser": hash_text2,
        "darthkaan": hash_text3
    }

    for username, hash_text in hashs.items():
        cur = DjangoHasher.find_hash(filepath, hash_text)
        print(f"Username: {username}\tPassword: {cur}")