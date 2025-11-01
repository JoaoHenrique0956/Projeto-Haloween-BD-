from tkinter import *
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
from pymongo import MongoClient
from datetime import datetime


# conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://joaoh:joao123@clusterdoce.zpjbfpc.mongodb.net/?retryWrites=true&w=majority",
    tls=True,
    tlsAllowInvalidCertificates=True
)
db = client["halloween"]
collection = db["cofre_doces"]

# gerar chave de criptografia
key = Fernet.generate_key()
fernet = Fernet(key)
print("Chave gerada:", key.decode())  # exibe no terminal a chave usada


# função para salvar os dados
def salvar_dados():
    nome = entry_nome.get()
    doce = entry_doce.get()
    quantidade = entry_qtd.get()

    if not nome or not doce or not quantidade:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número!")
        return

    doce_criptografado = fernet.encrypt(doce.encode()).decode()
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    collection.insert_one({
        "child": nome,
        "candy_type": doce_criptografado,
        "qty": quantidade,
        "timestamp": timestamp
    })

    messagebox.showinfo("Sucesso", "Doce salvo no MongoDB com sucesso!")
    entry_nome.delete(0, END)
    entry_doce.delete(0, END)
    entry_qtd.delete(0, END)


# função para listar e descriptografar
def listar_dados():
    docs = collection.find()
    txt_saida.delete(1.0, END)

    for doc in docs:
        try:
            doce_original = fernet.decrypt(doc["candy_type"].encode()).decode()
        except:
            doce_original = "[chave incorreta ou dado inválido]"

        txt_saida.insert(END, f"👧 Criança: {doc['child']}\n")
        txt_saida.insert(END, f"🍬 Doce: {doce_original}\n")
        txt_saida.insert(END, f"📦 Quantidade: {doc['qty']}\n")
        txt_saida.insert(END, f"🕒 Data: {doc['timestamp']}\n")
        txt_saida.insert(END, "-"*40 + "\n")


# interface tkinter
janela = Tk()
janela.title("Cofre de Doces Criptografado 🎃")
janela.geometry("480x480")
janela.configure(bg="#1f1f1f")

Label(janela, text="Cofre de Doces Criptografado", font=("Arial", 14, "bold"), bg="#1f1f1f", fg="orange").pack(pady=10)

frame = Frame(janela, bg="#1f1f1f")
frame.pack(pady=10)

Label(frame, text="Nome da Criança:", bg="#1f1f1f", fg="white").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = Entry(frame, width=30)
entry_nome.grid(row=0, column=1)

Label(frame, text="Tipo de Doce:", bg="#1f1f1f", fg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_doce = Entry(frame, width=30)
entry_doce.grid(row=1, column=1)

Label(frame, text="Quantidade:", bg="#1f1f1f", fg="white").grid(row=2, column=0, sticky="w", pady=5)
entry_qtd = Entry(frame, width=30)
entry_qtd.grid(row=2, column=1)

Button(janela, text="Salvar no Cofre", command=salvar_dados, bg="orange", fg="black", font=("Arial", 10, "bold")).pack(pady=5)
Button(janela, text="Listar e Descriptografar", command=listar_dados, bg="gray", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

txt_saida = scrolledtext.ScrolledText(janela, width=55, height=12, bg="#2b2b2b", fg="white", font=("Consolas", 9))
txt_saida.pack(pady=10)

janela.mainloop()
