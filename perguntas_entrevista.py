def reverse_string(word):
    result = ''.join(reversed(word))


def test_reverse_string():
    input_str = "UrbanRoutes"

    reversed_str = reverse_string(input_str)

    assert reversed_str == 'setuoRnabrU'

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)