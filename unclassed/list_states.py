# requires 'requests'
from requests import get
from json import loads

state_request = get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
state_obj = loads(state_request.text)

[print(name) for name in list(map(lambda item: item["nome"], state_obj))]

