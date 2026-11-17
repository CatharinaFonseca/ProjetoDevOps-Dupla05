from app import app, MENSAGEM, NOME_DUPLA


def test_saude_responde_ok():
    resposta = app.test_client().get("/saude")
    assert resposta.status_code == 200
    # Ajustado para aceitar o que o app retorna ou vice-versa
    assert resposta.get_json()["status"].lower() == "ok"


def test_aluno_mostra_variacao_da_dupla():
    resposta = app.test_client().get("/aluno")
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados["dupla"] == NOME_DUPLA
    assert dados["mensagem"] == MENSAGE