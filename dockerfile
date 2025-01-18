# imagem base oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponhe a porta em que a aplicação vai rodar
EXPOSE 5000

# Variável de ambiente que define o ambiente de execução da API
ENV FLASK_ENV="development"
ENV JWT_SECRET_KEY="UREI982Q3HFHWJHMDCO98283YWE8FHHWKQL1O23"

# Comando para iniciar a aplicação com Gunicorn (ou flask de estiver de dev)
CMD ["sh", "-c", "if [ \"${FLASK_ENV:-production}\" = 'development' ]; then flask run --host=0.0.0.0 --port=5000; else gunicorn -w 4 -b 0.0.0.0:5000 app:app; fi"]
