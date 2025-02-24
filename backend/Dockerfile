# 1️⃣ Usa a imagem oficial do Python
FROM python:3.9

# 2️⃣ Define o diretório de trabalho dentro do container
WORKDIR /app

# 3️⃣ Copia o arquivo de dependências primeiro (para otimizar cache)
COPY requirements.txt .

# 4️⃣ Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copia todos os arquivos do projeto
COPY . .

# 6️⃣ Expõe a porta 8000 para o FastAPI
EXPOSE 8000

# 7️⃣ Executa testes
CMD ["pytest"]

# 8️⃣ Comando para iniciar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
