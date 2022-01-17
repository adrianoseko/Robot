*** Settings ***

Library  Ping
Library  bitcoin
library  mail

*** Variables ***

${url}        google.com
${url2}       http://www.google.com
${teste}      ERRO
${result}      
${mail}

*** Keywords ***

Robot 
    # Aciona o ping e passa a url de conexão
    ${result}=  ping
    ...    ${url}

    # Verifica retorno, pega o preço do bitcoin
    IF  ${result} == 1
        ${robot}=  price bitcoin
        ...        ${url2}  

    # Verifica retorno e envia e-mail
        IF  ${robot}[1] == 1
            ${mail}=  mail
            ...     ${robot}[0]
            log  ${mail}  console=yes  
    
    # Em caso de Erro 
        ELSE
            log    ${robot[0]}    console=yes  
        END

    ELSE
        log    ${teste}     console=yes
    END
      

*** Tasks ***
Play robot
    Robot 
    

    
    