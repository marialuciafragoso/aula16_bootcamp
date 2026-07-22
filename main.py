from controller import get_cep, add_cep_to_db


def main():
    cep = input("Digite o CEP que deseja consultar: ")

    cep_schema = get_cep(cep)

    if cep_schema:
        print(f"CEP encontrado: {cep_schema.cep}")
        print(f"Logradouro: {cep_schema.logradouro}")
        print(f"Bairro: {cep_schema.bairro}")
        print(f"Cidade: {cep_schema.cidade}")
        print(f"Estado: {cep_schema.estado}")

        cep_salvo = add_cep_to_db(cep_schema)

        print(f"\nCEP salvo no banco de dados com ID: {cep_salvo}")

    else:
        print("Não foi possível encontrar esse CEP.")


if __name__ == "__main__":
    main()

