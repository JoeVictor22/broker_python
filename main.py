from config import PYRO_URL
if __name__ == "__main__":
    import Pyro4

    with Pyro4.Proxy(PYRO_URL) as p:
        try:
            p._pyroBind()

            from app.client import Client
            from app.sensor import Sensor


            choice = input("Digite: \n1 (para criar um cliente)\n2 (para criar um sensor)\n")

            if choice == "1":
                print("Criando Cliente")
                name = input("Digite o nome (vazio para gerar aleatorio)\n")
                topic = input("Digite o tópico (vazio para gerar aleatorio)\n")

                if name == "":
                    name = None
                if topic == "":
                    topic = None

                cliente = Client(name=name, topic_name=topic)
                cliente.start()

            elif choice == "2":
                print("Criando Sensor")
                name = input("Digite o nome (vazio para gerar aleatorio)\n")
                topic = input("Digite o tópico (vazio para gerar aleatorio)\n")

                if name == "":
                    name = None
                if topic == "":
                    topic = None

                sensor = Sensor(name=name, topic_name=topic)
                sensor.start()
            else:
                print("Opção invalida")

        except Pyro4.errors.CommunicationError as eee:
            from app.server import start_server
            print(eee)

            print("Iniciando servidor")
            start_server()
