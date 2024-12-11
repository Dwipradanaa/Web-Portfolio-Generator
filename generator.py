from jinja2 import Environment, FileSystemLoader
import os
from twilio.rest import Client

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

# Template loading
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index_template.html')

# Render template dengan data yang dimasukkan pengguna
output_html = template.render(portfolio_data)

# Simpan ke file output
os.makedirs('output', exist_ok=True)
with open('output/index.html', 'w') as f:
    f.write(output_html)

# Fungsi untuk mengirim pesan WhatsApp
def send_whatsapp_message(to_whatsapp_number):
    # Twilio credentials (ganti dengan kredensial Anda)
    account_sid = 'AC00bd02851f70d685a2e14695de8f93ed'  # Gantilah dengan SID akun Twilio Anda
    auth_token = '5e52332326e41ba58e48cf35ffa16cfc'    # Gantilah dengan token otentikasi Twilio Anda
    client = Client(account_sid, auth_token)

    # Nomor WhatsApp pengirim
    from_whatsapp_number = '+13203616474'  # Nomor WhatsApp Twilio Anda

    # Mengirim pesan WhatsApp ke nomor yang ditentukan
    message = client.messages.create(
        body="Hi! Portfolio Anda telah berhasil dibuat. Berikut adalah file portfolio Anda.",
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f"Pesan berhasil dikirim ke {to_whatsapp_number}: {message.sid}")

# Meminta nomor WhatsApp penerima dari pengguna
to_whatsapp_number = input("Masukkan nomor WhatsApp penerima script (format: whatsapp:+628811882828): ")

# Panggil fungsi untuk mengirim pesan WhatsApp
send_whatsapp_message(to_whatsapp_number)

print("\nPortfolio berhasil dihasilkan dan pesan WhatsApp telah dikirim!")
