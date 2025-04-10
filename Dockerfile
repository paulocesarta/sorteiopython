# Use uma imagem base Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o app vai usar
EXPOSE 8080

# Usa gunicorn para servir o app Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

