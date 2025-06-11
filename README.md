# INFOWEEK-ApiDay

Rest:

um acromio para representional state Transfer (Transferencia de estado representativo)

a transefrencia de dados de uma maneira figurativa, representativa e de maneira didatica

a transferencia de dados geralmente é realizada usando protocolo HTTP

O rest delimita obrigações para nesses transferencia de dados

Resouce seria entao: uma entidade ou um objeto

request/response

### NECESSIDADES (Constraints) para ser RestFull

_Uniforme intercafe_: Manter uma uniformidade, ou uma constancia,
e ou padrão para a construção desta interface. A nossa API tem que ser coerente com quem vai consumi-la. 
Usar somente uma linguagem de comunicação(JSON) e nao varias ao mesmo tempo. Sempre enviar respostas aos
clientes.

_Cliente server_: separação do cliente e do armazenamento de dados (servidor), dessa forma,
poder ter portabilidade entre os clientes como react-native (mobile) ou por exemplo react (web)

_Stateless_:cada  requisição que o cliente faz para o servidor, deverá conter as informações
necessarias paa o servidor entender e responder (Response) e a requisição  (request). Exemplo:
A sessão do usuario devera ser enviada para rodas as requisiçoes anterior. No nosso portal por exemplo, temos por 
padrão usar tokens para as cominicações.

_Cacheable_: As respostas para uma requisição, deverão ser explicitas ao dizer se aquela requisição, pode ou não ser cacheada pelo
cliente.

_Layerd System_: O cliente acessa a um endpoint, sem precisar saber da complexidade, de quais passos estão sendo necessarios para responder a requisição.

_Code on demanda (optional)_: Da a possibilidade da nossa aplicação (API) pegar codigos, como o javaScript, e executar no cliente

## Restful

restful é a aplicação de todos os padrões REST

## BOAS PRATICAS

-Utilizar verbos HTTP para nossas requisiçoes
-Utilizar plural ou singlar na criação de endpoints? (Isso importa?)
-Não eixe barra final no seu endPoint (/Cliente/)
-Nunca deixe o cliente sem resposta

## VERBOS HTTP

- GET: receber dados de um resource
- POST: Enviar dados ou info para serem processados por um resource
- PUT: Atualizar dados de um resource
- DELETE: Deletar um Resource

## STATUS DAS RESPOSTAS (RESPONSES)

- 1XX: Informação
- 2XX: Sucesso
- 200: CREATED
- 204: Não tem conteudo PUT POST DELETE
- 3XX: Rediretcion
- 4XX: Cliente Error
    -400: Bad Request
    -404: Not found
-5XX: Server Error
    -50: Internal Server Error
