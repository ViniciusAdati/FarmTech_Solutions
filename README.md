# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions: Assistente Agrícola Inteligente (Fase 4)

## Grupo 84

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Milton Akira Fukuhara</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Samyr de Souza Pereira</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Antonio Filipe de Souza Branco</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Albert Oliveira Ribeiro</a> 
- <a href="https://www.linkedin.com/in/vinicius-adati/">Vinicius Seiti Adati</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>

---

## 📜 Descrição

Na quarta fase de desenvolvimento do **FarmTech Solutions**, o projeto evolui da etapa de estruturação de dados para a tomada de decisão autônoma utilizando Inteligência Artificial e visualização em tempo real. O objetivo central é fornecer ao gestor agrícola um sistema preditivo que analisa as condições do solo e indica a necessidade exata de irrigação, otimizando o uso de recursos hídricos.

O ecossistema consome os dados simulados dos sensores (Umidade, pH, NPK e status de chuva) diretamente de um banco de dados em nuvem **Oracle Cloud**. Para garantir os padrões de mercado, implementamos uma arquitetura de segurança utilizando o `python-dotenv`, isolando as credenciais do banco em variáveis de ambiente (`.env`).

Após o processo de extração e limpeza robusta com a biblioteca Pandas, a aplicação utiliza o Scikit-Learn para treinar um modelo preditivo de **Regressão Linear**. Este modelo é exportado e consumido por um Dashboard interativo desenvolvido em **Streamlit**. Através dessa interface, o usuário pode monitorar os gráficos analíticos da produção e utilizar um Simulador de Manejo Agrícola, onde a IA processa os inputs climáticos inseridos e emite diagnósticos operacionais instantâneos sobre o acionamento da bomba de irrigação.

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.
- <b>assets</b>: Arquivos relacionados a elementos não-estruturados deste repositório, como imagens de evidência.
- <b>config</b>: Arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.
- <b>document</b>: Documentos do projeto requeridos nas atividades e modelagens.
- <b>scripts</b>: Scripts auxiliares para tarefas específicas, como ingestão de dados e setup do banco.
- <b>src</b>: Todo o código fonte criado para a Fase 4 (`app.py`, `modelo.py`, `requirements.txt` e o artefato de ML `modelo_irrigacao.pkl`).
- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto.

---

## 🔧 Como executar o código

### Pré-requisitos
* Python 3.10+ instalado.
* Acesso a uma instância do banco de dados Oracle configurada (as credenciais de acesso devem ser adicionadas a um arquivo `.env` na raiz do projeto).

### Passo 1: Instalar Dependências
Instale todos os pacotes necessários listados no `requirements.txt`:
```bash
pip install -r src/requirements.txt
