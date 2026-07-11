# FarmTech Solutions: Assistente Agrícola Inteligente

## 📜 Descrição

Na quarta fase de desenvolvimento do **FarmTech Solutions**, o projeto evolui da etapa de estruturação de dados para a tomada de decisão autônoma utilizando Inteligência Artificial e visualização em tempo real. O objetivo central é fornecer ao gestor agrícola um sistema preditivo que analisa as condições do solo e indica a necessidade exata de irrigação, otimizando o uso de recursos hídricos.

O ecossistema consome os dados simulados dos sensores (Umidade, pH, NPK e status de chuva) diretamente de um banco de dados em nuvem **Oracle Cloud**. Para garantir os padrões de mercado, implementamos uma arquitetura de segurança utilizando o `python-dotenv`, isolando as credenciais do banco em variáveis de ambiente (`.env`).

Após o processo de extração e limpeza robusta com a biblioteca Pandas, a aplicação utiliza o Scikit-Learn para treinar um modelo preditivo de **Regressão Linear**. Este modelo é exportado e consumido por um Dashboard interativo desenvolvido em **Streamlit**. Através dessa interface, o usuário pode monitorar os gráficos analíticos da produção e utilizar um Simulador de Manejo Agrícola, onde a IA processa os inputs climáticos inseridos e emite diagnósticos operacionais instantâneos sobre o acionamento da bomba de irrigação.

Mias informações, vídeo no YT:https://youtu.be/sZGCBQeMAik e https://youtu.be/7ltbqva4W5c
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
