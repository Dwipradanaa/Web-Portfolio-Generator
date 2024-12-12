from jinja2 import Environment, FileSystemLoader
import os

# Template loading
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index_template.html')

# Fungsi untuk mendapatkan input dari pengguna
def get_input(prompt, default_value=""):
    user_input = input(prompt + f" (default: {default_value}): ")
    return user_input if user_input else default_value

# Mengumpulkan data dari pengguna
print("Selamat datang di Web Portfolio Generator!")
name = get_input("Masukkan nama Anda", "John Doe")
profession = get_input("Masukkan profesi Anda", "Software Developer")
about = get_input("Tuliskan deskripsi tentang diri Anda", "A passionate software developer with experience in building web applications.")
email = get_input("Masukkan alamat email Anda", "johndoe@example.com")

# Mengumpulkan data keterampilan
skills = []
print("\nMasukkan keterampilan Anda. Ketik 'selesai' untuk mengakhiri.")
while True:
    skill = input("Masukkan keterampilan: ")
    if skill.lower() == 'selesai':
        break
    skills.append(skill)

# Mengumpulkan data proyek
projects = []
print("\nMasukkan proyek yang telah Anda kerjakan. Ketik 'selesai' untuk mengakhiri.")
while True:
    project_name = input("Nama proyek: ")
    if project_name.lower() == 'selesai':
        break
    project_description = input("Deskripsi proyek: ")
    projects.append({"name": project_name, "description": project_description})

# Membuat dictionary untuk portfolio data
portfolio_data = {
    "name": name,
    "profession": profession,
    "about": about,
    "skills": skills,
    "projects": projects,
    "email": email
}

# Render template dengan data yang dimasukkan pengguna
output_html = template.render(portfolio_data)

# Simpan ke file output
os.makedirs('output', exist_ok=True)
with open('output/index.html', 'w') as f:
    f.write(output_html)

print("\nPortfolio berhasil dihasilkan! Lihat file 'output/index.html' untuk melihat hasilnya.")
