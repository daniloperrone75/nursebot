# pip install gTTS
from gtts import gTTS

# pip install python-vlc
import vlc
import time

def reproduzir_audio(texto):
    tts = gTTS(texto, lang="pt")
    tts.save('nursebot.mp3')
    player = vlc.MediaPlayer("nursebot.mp3")
    player.play()
    time.sleep(5)  # tempo para permitir a reprodução antes da próxima fala

def ao_tocar_tela():
    reproduzir_audio("Olá! Como posso ajudar você hoje?")

def main():
    reproduzir_audio("Bem-vindo! Este é o robô nursebot. Estou aqui para ajudar com informações ou levar itens até você.")
    reproduzir_audio("Por favor, selecione no tablet o serviço desejado, como pedido de remédio, água ou chamada de enfermagem.")
    reproduzir_audio("Seu pedido foi recebido! Em instantes, estarei a caminho.")
    reproduzir_audio("Pronto! Entrega realizada com sucesso. Fique à vontade para me chamar novamente se precisar.")

