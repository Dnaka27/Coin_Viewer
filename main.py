import streamlit as st
import pandas as pd
import numpy as np
from binance.client import Client
import plotly.express as px
from dotenv import load_dotenv
import os

st.set_page_config(
    page_title="Coin Viewer - Binance Edition",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente Binance
@st.cache_resource
def get_binance_client():
    """Inicializa e retorna cliente Binance"""
    try:
        API_KEY = os.getenv("API_KEY", "")
        API_SECRET = os.getenv("API_SECRET", "")
        
        if API_KEY and API_SECRET:
            return Client(API_KEY, API_SECRET)
        else:
            return Client()  # Cliente público
    except Exception as e:
        st.error(f"Erro ao inicializar cliente Binance: {e}")
        return None


client = get_binance_client()

# Mapeamento de moedas
MOEDAS_DISPONIVEIS = {
    "Bitcoin (BTC)": "BTC",
    "Ethereum (ETH)": "ETH",
    "Binance Coin (BNB)": "BNB",
    "Ripple (XRP)": "XRP",
    "Cardano (ADA)": "ADA",
    "Solana (SOL)": "SOL",
    "Polkadot (DOT)": "DOT",
    "Dogecoin (DOGE)": "DOGE",
    "Avalanche (AVAX)": "AVAX",
    "Polygon (MATIC)": "MATIC",
}

MOEDAS_BASE = {
    "Dólar Americano (USDT)": "USDT",
    "Bitcoin (BTC)": "BTC",
    "Ethereum (ETH)": "ETH",
    "Binance USD (BUSD)": "BUSD",
}

INTERVALOS = {
    "1 dia": Client.KLINE_INTERVAL_1DAY,
    "4 horas": Client.KLINE_INTERVAL_4HOUR,
    "1 hora": Client.KLINE_INTERVAL_1HOUR,
}


def obter_dados_binance(par_trading, intervalo, limite):
    """
    Obtém dados históricos de preços da Binance
    
    Args:
        par_trading: String no formato 'BTCUSDT'
        intervalo: Intervalo de tempo (Client.KLINE_INTERVAL_*)
        limite: Número de candles a buscar
    
    Returns:
        DataFrame com os dados de preço ou None em caso de erro
    """
    if not client:
        return None
        
    try:
        klines = client.get_klines(
            symbol=par_trading,
            interval=intervalo,
            limit=limite
        )
        
        # Converter para DataFrame
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])
        
        # Converter timestamp para datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        # Converter preços para float
        df['close'] = df['close'].astype(float)
        
        return df[['timestamp', 'close']]
    
    except Exception as e:
        st.error(f"Erro ao obter dados para {par_trading}: {str(e)}")
        return None


def criar_grafico(dados_dict, moeda_base):
    """
    Cria gráfico interativo com Plotly
    
    Args:
        dados_dict: Dicionário com {nome_moeda: DataFrame}
        moeda_base: Nome da moeda base para o título
    """
    # Preparar dados para o gráfico
    df_completo = pd.DataFrame()
    
    for moeda, df in dados_dict.items():
        if df is not None and not df.empty:
            df_temp = df.copy()
            df_temp['Moeda'] = moeda
            df_completo = pd.concat([df_completo, df_temp], ignore_index=True)
    
    if df_completo.empty:
        st.warning("Nenhum dado disponível para plotar")
        return
    
    # Criar gráfico
    fig = px.line(
        df_completo,
        x='timestamp',
        y='close',
        color='Moeda',
        markers=True,
        title=f'Cotações em relação a {moeda_base}'
    )
    
    fig.update_layout(
        xaxis_title="Data/Hora",
        yaxis_title=f"Preço ({moeda_base})",
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)


def processar_requisicao(moeda_base_selecionada, moedas_comparar, periodo_dias, intervalo):
    """
    Processa a requisição e obtém dados de todas as moedas selecionadas
    
    Returns:
        Dicionário com dados de cada moeda ou None se erro
    """
    if not client:
        st.error("Cliente Binance não está disponível")
        return None
        
    moeda_base_codigo = MOEDAS_BASE[moeda_base_selecionada]
    dados_dict = {}
    
    # Calcular limite de candles baseado no período e intervalo
    if intervalo == Client.KLINE_INTERVAL_1DAY:
        limite = min(periodo_dias, 1000)
    elif intervalo == Client.KLINE_INTERVAL_4HOUR:
        limite = min(periodo_dias * 6, 1000)
    elif intervalo == Client.KLINE_INTERVAL_1HOUR:
        limite = min(periodo_dias * 24, 1000)
    else:
        limite = min(periodo_dias, 1000)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    total_moedas = len(moedas_comparar)
    
    for idx, moeda_nome in enumerate(moedas_comparar):
        moeda_codigo = MOEDAS_DISPONIVEIS[moeda_nome]
        
        # Pular se for a mesma moeda
        if moeda_codigo == moeda_base_codigo:
            continue
        
        status_text.text(f"Buscando dados de {moeda_nome}...")
        
        # Criar par de trading (ex: BTCUSDT)
        par_trading = f"{moeda_codigo}{moeda_base_codigo}"
        
        # Tentar obter dados
        df = obter_dados_binance(par_trading, intervalo, limite)
        
        if df is not None and not df.empty:
            dados_dict[moeda_nome] = df
        
        # Atualizar barra de progresso
        progress_bar.progress((idx + 1) / total_moedas)
    
    progress_bar.empty()
    status_text.empty()
    
    return dados_dict if dados_dict else None


# Interface principal
def main():
    """Função principal da aplicação"""
    
    # Cabeçalho
    st.title("Coin Viewer")
    st.subheader("Acompanhe criptomoedas em tempo real com a Binance")
    
    # Informações sobre a API
    with st.expander("Sobre os dados"):
        st.write("""
        Este aplicativo usa a API pública da Binance para obter cotações de criptomoedas.
        
        - Dados em tempo real das principais criptomoedas
        - Histórico de até 1000 períodos (dependendo do intervalo)
        - Sem necessidade de API Key para uso básico
        
        [Documentação da Binance API](https://binance-docs.github.io/apidocs/)
        """)
    
    st.write("---")
    
    # Controles em colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Configurações")
        
        moeda_base = st.selectbox(
            "Moeda base (cotação)",
            list(MOEDAS_BASE.keys()),
            index=0,
            help="A moeda em que os preços serão exibidos"
        )
        
        intervalo_selecionado = st.selectbox(
            "Intervalo de tempo",
            list(INTERVALOS.keys()),
            index=0,
            help="Intervalo entre cada ponto no gráfico"
        )
    
    with col2:
        st.header("Moedas para comparar")
        
        moedas_selecionadas = st.multiselect(
            "Selecione as criptomoedas",
            list(MOEDAS_DISPONIVEIS.keys()),
            default=["Bitcoin (BTC)", "Ethereum (ETH)"],
            help="Escolha uma ou mais moedas para comparar"
        )
        
        periodo = st.slider(
            "Período (dias)",
            min_value=1,
            max_value=365,
            value=30,
            help="Quantidade de dias de histórico"
        )
    
    st.write("---")
    
    # Botão de calcular centralizado
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        calcular = st.button(
            "Visualizar Cotações",
            use_container_width=True,
            type="primary"
        )
    
    # Processar quando botão clicado
    if calcular:
        if not moedas_selecionadas:
            st.warning("Selecione pelo menos uma criptomoeda para comparar")
        elif not client:
            st.error("Não foi possível conectar ao cliente Binance. Verifique sua instalação.")
        else:
            # Processar requisição
            intervalo_api = INTERVALOS[intervalo_selecionado]
            
            with st.spinner('Buscando dados da Binance...'):
                dados = processar_requisicao(
                    moeda_base,
                    moedas_selecionadas,
                    periodo,
                    intervalo_api
                )
            
            if dados and len(dados) > 0:
                # Criar e exibir gráfico
                criar_grafico(dados, MOEDAS_BASE[moeda_base])
                
                # Exibir estatísticas
                st.write("---")
                st.subheader("Estatísticas")
                
                cols = st.columns(len(dados))
                for idx, (moeda, df) in enumerate(dados.items()):
                    with cols[idx]:
                        preco_atual = df['close'].iloc[-1]
                        preco_inicial = df['close'].iloc[0]
                        variacao = ((preco_atual - preco_inicial) / preco_inicial) * 100
                        
                        st.metric(
                            label=moeda,
                            value=f"{preco_atual:.4f} {MOEDAS_BASE[moeda_base]}",
                            delta=f"{variacao:.2f}%"
                        )
            else:
                st.error("Não foi possível obter os dados. Verifique sua conexão com a internet.")
    
    # Footer
    st.write("---")

# Executar aplicação
if __name__ == "__main__":
    if client is None:
        st.error("ERRO: Não foi possível inicializar o cliente Binance. Verifique se a biblioteca python-binance está instalada corretamente.")
        st.stop()
    main()