import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
MEU_NOME = "nome"  

topico_sensor = f"minicurso/{MEU_NOME}/temp"
topico_atuador = f"minicurso/{MEU_NOME}/ar"

def ao_receber_mensagem(client, userdata, msg):
    
    # Decodifica a mensagem que vem da rede
    texto_recebido = msg.payload.decode()
    
    # TODO 1: O dado chega da rede como texto. Converta 'texto_recebido' para  
    # um numero decimal (float) e guarde em uma variavel chamada 'temperatura'.
    
    
    
    print(f"Temperatura atual no CPD: {texto_recebido} C")
    
    # TODO 2: Crie a regra de negocio. 
    # SE a temperatura for maior que 28.0:
    #    Publique a palavra "LIGAR" no topico_atuador.
    # SENAO:
    #    Publique a palavra "DESLIGAR" no topico_atuador.
    # DICA: Olhe como o ESP32 publicou os dados no Wokwi! A logica do client.publish() eh a mesma.
    
    
    
    

# Inicializacao do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = ao_receber_mensagem
client.connect(BROKER, 1883)

# TODO 3: Assine o topico do sensor para comecar a ler os dados da rede.



print("Sistema de monitoramento iniciado.")
print(f"Aguardando dados de {MEU_NOME}...")
print("Pressione Ctrl+C para encerrar.\n")

# Mantem o programa rodando e escutando a rede
client.loop_forever()