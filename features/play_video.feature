Feature: Reprodução Contínua de Vídeos

  Scenario: O usuário retoma um vídeo de onde parou
    Given o usuário está logado na Netflix
    And o usuário pausou um vídeo no minuto 15
    When o usuário acessa a Netflix novamente e inicia a reprodução do vídeo
    Then o vídeo deve começar a partir do minuto 15

  Scenario: O próximo episódio é reproduzido automaticamente
    Given o usuário assistiu um episódio inteiro de uma série
    When o episódio termina
    Then o próximo episódio deve começar automaticamente
