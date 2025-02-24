# ponderada2_M9_S3_programacao

Para aferir a qualidade dos requisitos não funcionais (RNF) — neste caso, o autoplay do próximo episódio — é necessário avaliar alguns aspectos do sistema quando os códigos são executados. A seguir, apresento uma análise com base no código de exemplo e nos testes unitários:

1. Confiabilidade e Consistência do Comportamento
Aspecto Avaliado:

O RNF “O próximo episódio é reproduzido automaticamente” exige que, ao concluir um episódio, o sistema automaticamente inicie o próximo sem intervenção do usuário.
Análise:

O código implementado na classe NetflixApp simula esse comportamento por meio do método watch_episode(), que define a variável episode_finished como True.
O método is_playing_next_episode() utiliza essa flag para retornar se o autoplay foi acionado.
Os testes unitários (em tests/test_rnf.py) verificam que, após chamar watch_episode(), a função retorna True, indicando que o comportamento esperado está ocorrendo.
Essa abordagem demonstra que o requisito não funcional está sendo atendido de forma consistente, desde que a simulação corresponda ao comportamento real desejado.
2. Escalabilidade e Desempenho (Aspectos de RNF)
Aspecto Avaliado:

Embora o exemplo fornecido seja uma simulação simples, a ideia de reprodução automática do próximo episódio está relacionada a como o sistema lida com a transição entre conteúdos sem impactar a experiência do usuário.
Análise:

Em um sistema real, o autoplay envolve pré-carregamento e gerenciamento de recursos para evitar interrupções (buffering).
O código de exemplo, mesmo sendo simplificado, permite a verificação de que o fluxo de execução não exige intervenção manual e que a transição ocorre imediatamente após a finalização do episódio.
Testes unitários garantem que essa transição ocorra de forma previsível, contribuindo para a robustez do sistema.
Para aferir a qualidade completa do RNF em um ambiente de produção, seriam necessários testes de carga e de desempenho, mas a simulação já ajuda a identificar se o fluxo básico está correto.
3. Facilidade de Manutenção e Testabilidade
Aspecto Avaliado:

Um requisito não funcional de qualidade deve permitir que a aplicação seja testada e mantida com facilidade.
Análise:

A separação do código em módulos (por exemplo, netflix_mock.py ou netflix_service.py) e a criação de testes unitários separados para RF e RNF demonstram que a arquitetura está organizada para facilitar a manutenção.
A utilização de frameworks como pytest e Behave permite que alterações futuras sejam testadas de forma automatizada, garantindo que o comportamento esperado (como o autoplay) continue funcionando mesmo após mudanças no código.
Esse modelo modular e testável é um indicador de alta qualidade no atendimento dos requisitos não funcionais.
4. Conclusão
A qualidade dos requisitos não funcionais (neste caso, o autoplay do próximo episódio) pode ser aferida de forma positiva se considerarmos que:

O código simula o comportamento desejado e os testes unitários comprovam que a funcionalidade está operando conforme esperado.
A abordagem modular e os testes automatizados garantem que o sistema seja confiável e de fácil manutenção.
Embora a simulação não aborde aspectos complexos como desempenho em ambientes reais de alta carga, ela fornece uma base sólida para iniciar a implementação e avaliação dos requisitos não funcionais.

Essa avaliação demonstra que, mesmo em um cenário acadêmico com código simulado, é possível aferir a qualidade dos requisitos não funcionais por meio de testes automatizados e da organização modular do sistema.
