# Executar o visualizador AISWEB no GitHub Codespaces

Este repositório está configurado para executar o app Python em um Codespace. O app original foi feito para uso local; o inicializador em `.devcontainer/run_ais.py` faz o servidor escutar na interface do container, como o encaminhamento de portas do Codespaces exige, e evita tentar abrir um navegador dentro do container.

## Como iniciar

1. Abra o repositório no GitHub e selecione **Code → Codespaces → Create codespace on `copilot/run-aisweb-in-codespaces`** (ou crie o Codespace a partir da branch que contém esta configuração).
2. No terminal do Codespace, execute:

   ```bash
   python3 .devcontainer/run_ais.py
   ```

3. Quando o Codespaces perguntar sobre a porta **8765**, abra a porta no navegador. A configuração tenta abri-la automaticamente.
4. No app, informe o código ICAO do aeródromo, por exemplo `SBGR`.

O app usa apenas a biblioteca padrão do Python, então não precisa instalar dependências adicionais. O Codespace precisa de acesso à internet para consultar a AISWEB. O encaminhamento da porta está configurado como **privado**; para compartilhar o app, altere a visibilidade da porta conscientemente nas opções de Ports.

## Observações

- O servidor permanece disponível enquanto o Codespace estiver ativo. Ao parar ou suspender o Codespace, o app deixa de responder; inicie o comando novamente ao retomá-lo.
- O cache de cartas fica em `cache_aisweb/` no Codespace.
- Esta configuração não publica o app como um site permanente nem o executa por meio do GitHub Actions.
