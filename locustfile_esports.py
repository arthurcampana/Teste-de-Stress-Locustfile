"""
Trabalho de Teste de Stress - Qualidade e Teste de Software
Parte 2: Automação com Python e Locust

Simula o comportamento de clientes (jogadores) requisitando dados de uma API
global. O host publico https://jsonplaceholder.typicode.com e usado, simulando
que a rota /users representa a busca pelo perfil dos jogadores profissionais.

Como executar:
    1. Instalar o Locust:  pip install locust
    2. Rodar o teste:      python -m locust -f locustfile_esports.py
    3. Acessar o painel:   http://localhost:8089
    4. Configurar no painel:
         - Number of users: 50
         - Spawn rate: 5
         - Host: https://jsonplaceholder.typicode.com
         - Tempo de execucao: 3 minutos
"""

from locust import HttpUser, task, between


class JogadorProfissional(HttpUser):
    """
    Usuario virtual que simula um jogador profissional buscando seu perfil.

    - wait_time dinamico entre 2 e 4 segundos (tempo de pensamento/preenchimento)
    - Cada iteracao faz um GET na rota /users
    """

    # Tempo de simulacao de preenchimento de dados/pensamento (think time)
    # definido de forma dinamica entre 2 e 4 segundos.
    wait_time = between(2, 4)

    @task
    def buscar_perfil_jogadores(self):
        """
        Faz uma requisicao GET na rota /users, simulando a busca pelo
        perfil dos jogadores profissionais.
        """
        self.client.get("/users")
