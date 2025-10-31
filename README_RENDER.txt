
Projeto preparado para deploy no Render.

Foi realizado:
- settings.py modificado para usar python-dotenv e dj-database-url.
- DATABASE_URL será lido da variável de ambiente DATABASE_URL.
- DEBUG, ALLOWED_HOSTS configuráveis por variáveis de ambiente.
- Adicionados Procfile, requirements.txt, runtime.txt.
- Whitenoise configurado para servir arquivos estáticos em produção.
- .env removido do pacote (não incluído por segurança).

Como subir no Render:
1. No painel do Render, crie um novo Web Service ligado ao seu repositório (ou faça upload do ZIP).
2. Defina a variável de ambiente DATABASE_URL com o valor do Neon.
3. Defina ALLOWED_HOSTS (opcional) e DEBUG (opcional).
4. Comando de build: pip install -r requirements.txt
5. Comando de start: será usado o Procfile (gunicorn).

Arquivo criado: /mnt/data/ProjetoFinalRoveri_for_render.zip
