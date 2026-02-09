# Coin Viewer - Binance Edition

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Aplicativo web interativo para visualização de cotações de criptomoedas em tempo real usando a API da Binance.

---

![Menu](assets/Menu.png)

---

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Configuração](#configuração)
- [Licença](#licença)
- [Contato](#contato)

## Sobre o Projeto

O **Coin Viewer** é uma aplicação desenvolvida em Python com Streamlit que permite acompanhar as principais criptomoedas do mercado em tempo real. O projeto utiliza a API pública da Binance para obter dados históricos e atualizados de preços, oferecendo uma interface limpa e intuitiva para análise de tendências.

- **Gratuito**: Utiliza a API pública da Binance, sem necessidade de credenciais
- **Tempo Real**: Dados atualizados diretamente da maior exchange de criptomoedas do mundo
- **Intuitivo**: Interface amigável desenvolvida com Streamlit
- **Flexível**: Permite comparar múltiplas moedas e configurar diferentes intervalos de tempo
- **Leve**: Não requer instalação complexa, apenas Python e algumas bibliotecas

## Principais Funcionalidades

- **Visualização de Múltiplas Criptomoedas**: Compare BTC, ETH, BNB, XRP, ADA, SOL e mais
- **Intervalos Personalizáveis**: Escolha entre intervalos de 1 hora, 4 horas ou 1 dia
- **Histórico Extenso**: Analise até 365 dias de dados históricos
- **Gráficos Interativos**: Gráficos responsivos com Plotly (zoom, pan, hover)
- **Estatísticas em Tempo Real**: Preço atual e variação percentual
- **Diferentes Moedas Base**: Visualize cotações em USDT, BTC, ETH ou BUSD
- **Interface Responsiva**: Layout adaptável para diferentes tamanhos de tela
- **Barra de Progresso**: Feedback visual durante carregamento dos dados

## Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

- [Python 3.8+](https://www.python.org/) - Linguagem de programação
- [Streamlit](https://streamlit.io/) - Framework para criação de aplicações web
- [Binance API](https://binance-docs.github.io/apidocs/) - API para dados de criptomoedas
- [Plotly](https://plotly.com/python/) - Biblioteca para gráficos interativos
- [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados
- [Python-Binance](https://python-binance.readthedocs.io/) - Cliente Python para API Binance

## Instalação

### Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

### Passo a Passo

1. **Clone o repositório** (ou faça download do código)

```bash
git clone https://github.com/seu-usuario/coin-viewer.git
cd coin-viewer
```

2. **Crie um ambiente virtual** (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**

```bash
streamlit run coin_viewer_final.py
```

5. **Acesse no navegador**

A aplicação abrirá automaticamente em `http://localhost:8501`

## Como Usar

### Interface Básica

1. **Selecione a moeda base** (coluna esquerda)
   - Escolha em qual moeda deseja ver os preços (USDT, BTC, ETH, BUSD)

2. **Escolha o intervalo de tempo** (coluna esquerda)
   - Defina o intervalo entre cada ponto no gráfico (1h, 4h, 1d)

3. **Selecione as criptomoedas** (coluna direita)
   - Escolha uma ou mais moedas para comparar
   - Por padrão, Bitcoin e Ethereum já vêm selecionados

4. **Ajuste o período** (coluna direita)
   - Use o slider para definir quantos dias de histórico visualizar (1 a 365 dias)

5. **Clique em "Visualizar Cotações"**
   - Aguarde o carregamento dos dados
   - Analise o gráfico e as estatísticas

## Configuração

### Usando API Keys da Binance (Opcional)

Para funcionalidades avançadas ou limites maiores de requisições:

1. **Crie uma conta na Binance** (se ainda não tiver)
   - Acesse: https://www.binance.com/

2. **Gere suas API Keys**
   - Faça login na Binance
   - Vá em "Gerenciamento de API"
   - Crie uma nova API Key
   - **IMPORTANTE**: NÃO habilite permissões de trading, apenas leitura

Adicione suas credenciais:

```env
API_KEY=sua_api_key_aqui
API_SECRET=sua_api_secret_aqui
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### Sobre a API Binance

Este projeto utiliza a API pública da Binance. Certifique-se de seguir os [Termos de Uso da Binance](https://www.binance.com/en/terms).

---

## Agradecimentos

- [Binance](https://www.binance.com/) - Por fornecer a API pública
- [Streamlit](https://streamlit.io/) - Framework incrível para criar aplicações web
- [Plotly](https://plotly.com/) - Biblioteca de visualização de dados
- Comunidade Python - Pelo suporte e bibliotecas open source

---

**Desenvolvido com ❤️ usando Python e Streamlit**

Se este projeto foi útil para você, considere dar uma ⭐!