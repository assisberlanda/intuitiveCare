# 🌐 intuitiveCare
✨ Teste de Nivelamento v.250321

## Testes desenvolvidos
| Web Scrapping | Transformação de Dados | Banco de Dados | API |
|:-:|:-:|:-:|:-:|
| [web_scraping.py](https://github.com/assisberlanda/intuitiveCare/blob/main/web_scraping.py) | [change_data.py](https://github.com/assisberlanda/intuitiveCare/blob/main/change_data.py) | <br> [demonstracoes_contabeis.sql](https://github.com/assisberlanda/intuitiveCare/blob/main/demonstracoes_contabeis.sql) <br><br> [operadoras_ativas.sql](https://github.com/assisberlanda/intuitiveCare/blob/main/operadoras_ativas.sql) | [PresidentSearch.vue](https://github.com/assisberlanda/intuitiveCare/blob/main/president_search/src/components/PresidentSearch.vue)|
| [Anexos I e II](https://github.com/assisberlanda/intuitiveCare/tree/main/web_scraping) | [Teste_assis_berlanda.zip](https://github.com/assisberlanda/intuitiveCare/tree/main/test_table) | <br> [demonstracoes_contabeis/2023](https://github.com/assisberlanda/intuitiveCare/tree/main/data_base/demonstracoes_contabeis%3A2023) <br><br> [demonstracoes_contabeis/2024](https://github.com/assisberlanda/intuitiveCare/tree/main/data_base/demonstracoes_contabeis%3A2024) <br><br> [Relatorio_cadop.csv](https://github.com/assisberlanda/intuitiveCare/blob/main/data_base/Relatorio_cadop.csv)| [Teste API](https://github.com/assisberlanda/intuitiveCare/tree/main/test_api) <br><br> [postman_collection.json](https://github.com/assisberlanda/intuitiveCare/blob/main/test_api/postman_collection.json) |
### ✅ Testar se o FastAPI está rodando
No terminal, dentro da pasta president_search onde está main.py, execute:
```
uvicorn main:app --reload
```
Abra outro terminal, dentro da pasta president_search onde está main.py, execute:
```
npm run serve
```
#### Testar a aplicação
Abra um navegador e acesse:
```
http://localhost:8080/
```

#### Testar a API no navegador ou no Postman
Copie e cole no browser do navegador:
```
http://127.0.0.1:8000/buscar_presidente
```
#### 💡 Testar a documentação automática
Clique para executar no navegador:

[Swagger UI](http://127.0.0.1:8000/docs#/)

[Redoc](http://127.0.0.1:8000/redoc)
- Clique no Botão GET
- Clique no Botão Try it out
- Clique no Botão Execute
- Clique no Botão Download
