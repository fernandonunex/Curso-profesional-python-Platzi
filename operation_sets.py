def run():
    set_names1 = {'pedro', 'juan', 'pablo', 'raul', 'fernando'}
    set_names2 = {'fernando', 'maria', 'raul', 'saul', 'cesar'}
    print(set_names1)
    print(set_names2)

    print("Union")
    set_names3 = set_names1 | set_names2
    print(set_names3)
    print("Interseccion")
    set_names4 = set_names1 & set_names2
    print(set_names4)
    print("Diferencia")
    set_names5 = set_names1 - set_names2
    print(set_names5)
    print("Diferencia simetrica")
    set_names6 = set_names1 ^ set_names2
    print(set_names6)



if __name__ == "__main__":
    run()
