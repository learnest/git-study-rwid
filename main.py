# git init untuk menggunakan directory sebagai folder project
print("Hello world!")

# git add [file] digunakan untuk memasukkan file ke dalam staged changes
# staged changes sendiri adalah sebuah area dimana file2 yang telah diubah
# akan ditaruh sebelum commit

# untuk save, pakai git commit -m "commit comment"
# version control bisa lihat di git log
# changes tidak akan muncul jika file tidak di save

print("Hello world!")
print("Hello world!")
print("Hello world!")

# untuk add several changes in one-go, gunakan git add *

# branches adalah kelompok development yang terpisah-pisah
# digunakan untuk develop fitur tanpa mengganggu branch lain karena sudah terisolasi
# untuk membuat branch baru, gunakan git branch [nama branch]



# git reset --hard akan restore save point di commit yang terakhir
# git merge menggabungkan fitur2 yang ada di dua branch
print("Kode ini dari branch dev")


# Di atas akan menjadi hasil git merge


# Jika terjadi merge conflict maka:
# edit file yang ter-merge dan hapus tanda merge conflict
# (<<<<<<<, =======, >>>>>>>)

# Github adalah remote repository untuk menyimpan file

# git checkout [hash] bisa masuk dan edit saved file