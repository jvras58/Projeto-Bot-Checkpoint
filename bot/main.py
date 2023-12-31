import time

import discord
from config.conector_discord import ConectorDiscord
from config.config import get_settings
from funcoes.alertas import (
    alerta_checkpoint,
    verificar_checkpoints_nao_enviados,
)
from funcoes.comandos import (
    alerta_dm_horario,
    comousar,
    definir_alerta,
    envia_dm,
    envia_link_bot,
    idcheckpoint,
    idignore,
    idplanilha,
    offavisodm,
    offeveryone,
    onavisodm,
    oneveryone,
    processa_mensagem_canal_alvo,
    readicionarids,
)
from funcoes.dados import dados, envia_planilha
from funcoes.mensagens import on_message as on_message_mensagens
from funcoes.mensagens import on_ready as on_ready_mensagens

cliente_discord = discord.Client(intents=discord.Intents.all())
conector_discord = ConectorDiscord()


@cliente_discord.event
async def on_ready():
    """
    Função assíncrona que é chamada quando o bot está pronto para ser utilizado.
    Chama a função on_ready_mensagens passando os parâmetros necessários.
    """
    await on_ready_mensagens(
        cliente_discord,
        conector_discord,
        dados,
        alerta_checkpoint,
        verificar_checkpoints_nao_enviados,
    )


@cliente_discord.event
async def on_message(mensagem):
    """
    Função que trata eventos de mensagens recebidas no cliente Discord.

    Parâmetros:
    - mensagem: A mensagem recebida pelo BOT.

    """
    await on_message_mensagens(
        mensagem,
        cliente_discord,
        conector_discord,
        envia_link_bot,
        processa_mensagem_canal_alvo,
        envia_planilha,
        envia_dm,
        comousar,
        offeveryone,
        oneveryone,
        offavisodm,
        onavisodm,
        definir_alerta,
        alerta_dm_horario,
        idignore,
        readicionarids,
        idcheckpoint,
        idplanilha,
    )


while True:
    try:
        # Inicialização do cliente do Discord
        cliente_discord.run(get_settings().DISCORD_TOKEN)
    except Exception as e:
        print(f'Erro: {e}. Reiniciando o bot.')
        time.sleep(5)  # Pausa por 5s
