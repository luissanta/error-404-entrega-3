import pulsar, _pulsar

from .utils import consultar_schema_registry, obtener_schema_avro_de_diccionario, broker_host

def obtener_suscripcion_a_topico():
    json_schema = consultar_schema_registry('public/default/eventos-suscripcion')  
    avro_schema = obtener_schema_avro_de_diccionario(json_schema)

    client = pulsar.Client(f'pulsar://{broker_host()}:6650')
    return client.subscribe('eventos-suscripcion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-bff', schema=avro_schema)