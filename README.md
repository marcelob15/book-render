# book-render
book-render


'''
### **3. Executando a API Localmente**

Com os arquivos `api/models.py` e `api/main.py` prontos, agora podemos rodar nossa API.

1.  Abra seu terminal na pasta raiz do projeto (`book-api`).
2.  Execute o seguinte comando para iniciar o servidor:
    ```bash
    uvicorn api.main:app --reload
    uvicorn api.main:app --reload --port 9000
    
    externo 
    uvicorn api.main:app --reload --host 0.0.0.0 --port 9000
    ```
    *   `uvicorn`: É o servidor ASGI que vai "rodar" nossa aplicação FastAPI.
    *   `api.main:app`: Indica ao Uvicorn para encontrar o objeto `app` dentro do arquivo `api/main.py`.
    *   `--reload`: Faz com que o servidor reinicie automaticamente sempre que você salvar uma alteração no código.

3.  Se tudo estiver certo, você verá uma saída parecida com esta:
    ```
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [xxxxx]
    INFO:     Started server process [xxxxx]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

### **4. Testando a API e a Documentação (Swagger)**

O FastAPI gera automaticamente uma documentação interativa da sua API.

1.  Abra seu navegador e acesse: **http://127.0.0.1:8000/docs**
                                   http://127.0.0.1:9000/docs

Você verá a interface do Swagger UI, onde pode ver todos os seus endpoints, seus modelos de dados e até mesmo testá-los diretamente pelo navegador!



**Teste alguns endpoints:**

*   Clique no endpoint `GET /api/v1/health`, depois em "Try it out" e "Execute". Você verá o status da API.
*   Tente o `GET /api/v1/categories` para ver a lista de categorias.
*   Tente o `GET /api/v1/books/{book_id}`. Coloque `5` no campo `book_id` e execute.
*   Experimente a busca em `GET /api/v1/books/search`, fornecendo um `title` como "light".

'''