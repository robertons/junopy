


# SDK Python3 para Integração com Juno

Esta SDK foi desenvolvida para abstrair aos desenvolvedores os principais detalhes da comunicação com API v2 da Juno tanto em [produção](https://juno.com.br/#) quanto em ambiente [sandbox](https://sandbox.juno.com.br/#).

Você pode acessar a documentação base da api aqui: [Api V2 Juno](https://dev.juno.com.br/api/v2).

![Licença](https://img.shields.io/github/license/robertons/junopy) ![image](https://img.shields.io/pypi/v/junopy) ![image](https://img.shields.io/pypi/status/junopy) ![image](https://img.shields.io/badge/python-v3.7-blue) ![image](https://img.shields.io/badge/build-passing-brightgreen) ![image](https://img.shields.io/badge/coverage-100%25-brightgreen) ![image](https://img.shields.io/github/last-commit/robertons/junopy)

# Instalação
Instalação utilizando Pip
```bash
pip install junopy
```
Git/Clone
```
git clone https://github.com/robertons/junopy
cd junopy
pip install -r requirements.txt
python setup.py install
```
# Objetos

Os objetos neste SDK podem ser criados em 3 (três) formas distintas a critério do utilizador.

## Criação

**Método 1 - Construção**
```python
objeto = Objeto(campo1 = 'valor', campo2 = 'valor 2', campo_datetime = datetime.now(), campo_float = 10.1)
```
**Método 2 - Construção com Dicionário**
```python
objeto = Objeto(**{'campo1':'valor', 'campo2':'valor 2', 'campo_datetime':datetime.now(), 'campo_float' = 10.1})
```
**Método 3 - Pós-Construção**
```python
objeto = Objeto()
objeto.campo1 = 'valor'
objeto.campo2 = 'valor 2'
objeto.campo_datetime = datetime.now()
objeto.campo_float = 10.1
```
##  Método toJSON

Método toJSON() retorna os dados do Objeto em formato *diciciontario* não codificados.

```python
objeto = Objeto(...)
print(objeto.toJSON())
```


## Configuração Inicial
|posição  | campo |  obrigatório | padrão | descrição |
|--|--|--|--|--|
| 1 | private_token | **sim** |  | Token Privado Juno
| 2 | clientId | **sim** |  | Id Cliente
| 3 | clientSecret | **sim** |  | Chave Cliente
| 4 | sandbox | **não** | **False** | Ambiente Produção/Sandbox
| 5 | debug | **não** | **False** | Depuração Request Post, Get, Put, Patch e Delete

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET', sandbox=True)
```
### Obtenção de TOKEN

Cada token com permissão de acesso ao servidor de serviço tem validade de 1 hora, a recomendação da Juno é que um novo Token seja gerado apenas em caso de expiração. A instancia gerada administra isso automaticamente, contudo a função *GetToken* permite obter o token para que os dados sejam utilizado em outras instâncias.  Este processo **não é obrigatório, mas é recomendável** principalmente em sistemas onde serão **criadas novas instâncias junopy a cada transação**

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#section/Servidor-de-Autorizacao)**

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
junopy.GetToken()
token_valido_1h = junopy.TOKEN
```

### Definição Token de Acesso - Usando dados gerados anteriormente

É possível definir manualmente os dados de acesso através da função *SetToken*

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
junopy.SetToken('access_token', 'token_type', 'expires')
```
# Utilidades

 **Lista de Bancos**
```python
bancos = junopy.util.Banks()
```
**Lista de Tipos de Empresas**
```python
tipos_empresas = junopy.util.CompanyTypes()
```
**Tipos de Negócios**
```python
tipos_empresas = junopy.util.BusinessAreas()
```
**Chave Publica de Criptografia**
```python
chave_publica = junopy.util.PublicKey()
```

**Validação Webhook**
Todo Webhook recebido da Juno traz consigo uma assinatura no header da `Requisição Post`. A assinatura é um hash para validar a autenticidade do conteúdo.  

Ao criar um Webhook é gerado uma chave que deve ser armazenada em segurança e utilizada neste processo.  

**Leia atentamente como funciona o processo em [Criação e Assinatura de Webhook]**(https://dev.juno.com.br/api/v2#operation/createWebhook)

| campo | tipo | obrigatório |
|--|--|--|
| x_signature | string | **sim** |
| body_content | bytes |**sim** |
| secret | string |**sim** |

o retorno da função será `True` ou `False`
```python
webhook_valido = junopy.util.IsValidWebhook(x_signature, body_content, secret)
```

# Conta Digital

A seção compreende:
-   Criação de contas digitais
-   Consulta de contas digital
-   Alteração de dados da conta digital

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Contas-Digitais)**

### Criação

No exemplo abaixo foram utilizados os 3 métodos de criação de objeto de formas distintas:

**Após o preenchimento do Objeto o comando Create, realiza o Post na ApiV2.**

```python
	conta = junopy.DigitalAccount()
    conta.name = "Usuário Teste"
    conta.document = "123.456.789-00"
    conta.email = "usu.teste@email.com"
    conta.birthDate = "1980-01-01" #
    conta.phone = "9999999999"
    conta.businessArea = 2015
    conta.linesOfBusiness = "INDIVIDUAL"

    conta.address = junopy.Address(**{
    		'street': 'Nome da Rua',
    		'number': '01',
    		'complement': 'Casa',
    		'neighborhood': 'Bairro',
    		'city': 'Cidade',
    		'state': 'UF',
    		'postCode': '99999999'
    })

    conta_bancaria =  junopy.BankAccount()
    conta_bancaria.bankNumber = "000"
    conta_bancaria.agencyNumber = "1111"
    conta_bancaria.accountNumber = "22334455"
    conta_bancaria.accountComplementNumber = "0"
    conta_bancaria.accountType = "CHECKING"
    conta_bancaria.accountHolder = junopy.AccountHolder(name='Usuario Teste', document='00000000000')
    conta.bankAccount = conta_bancaria

    conta.Create()
```

### Consulta
```python
	conta = junopy.DigitalAccount(id='dac_E6FECDB17EAC5992').Get()
```

** Consulta de conta digital criada a partir do token privado da conta digital**

```python
	conta_digital_criada = junopy.DigitalAccount(id='dac_E6FECDB17EAC5992', resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').Get()
```

### Atualização
```python
	conta = junopy.DigitalAccount()
	conta.id = "dac_E6FECDB17EAC5992"
	conta.resourceToken = '8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9'
	conta.address = junopy.Address(
    		street = 'Nome da Rua',
    		number = '01',
    		complement = 'Casa',
    		neighborhood = 'Bairro',
    		city = 'Cidade',
    		state = 'UF',
    		postCode = '99999999'
    })
	conta = junopy.DigitalAccount().Update()
```

##  Soluções Whitelabel

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Novo-Onboarding)**

###   Novo Onboarding - Somente Envio de Documentos

```python
onboarding = junopy.onboarding.Documents(
        returnUrl="https://www.website.com.br/documents",
        refreshUrl="https://www.website.com.br/invalid")
```

###  Novo Onboarding - Solução Completa Conta e Envio de Documentos

```python
onboarding = junopy.onboarding.Account(
        referenceId='id_proprio',
        returnUrl="https://www.website.com.br/documents",
        refreshUrl="https://www.website.com.br/invalid"
    )
```

#  Documentos

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Documentos)**

**Consulta**

```python
documentos_esperados = junopy.Document(id='dac_E6FECDB17EAC5993').Get()
```
**Consulta de outra Conta Digital (Resource)**

```python
documentos_esperados = junopy.Document(id='dac_E6FECDB17EAC5992', resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').Get()
```

**Lista Documentos**

```python
documentos_esperados = junopy.Document().Get()
```

**Lista Documentos de outra Conta Digital (Resource)**

```python
documentos_esperados = junopy.Document(resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').Get()
```

## Envio de Documentos/Arquivos

**Método path do arquivo**
Uma array de string contendo o caminho local do arquivo

```python
documentos_esperados = junopy.Document(
        id='doc_AD1E698AB61CF185',
        resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').SendFiles(['arquivo_1.pdf', 'arquivo_2.pdf'])
```

**Método BufferedReader do arquivo**
Uma array com tuplas onde posição 0 é o nome do arquivo e posição 1 os BufferedReader

```python
documentos_esperados = junopy.Document(
        id='doc_AD1E698AB61CF185', resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').SendFiles([('arquivo_1.pdf', file_buffered)])

```

**Método bytes do arquivo**
Uma array com tuplas onde posição 0 é o nome do arquivo e posição 1 os bytes

```python
documentos_esperados = junopy.Document(
        id='doc_AD1E698AB61CF185', resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').SendFiles([('arquivo_1.pdf', file_bytes)])

```

# Saldo

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Saldo)**

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
saldo = junopy.Balance()
```
> {'balance': 0.0, 'withheldBalance': 0.0, 'transferableBalance': 0.0}

**ou de outra conta digital**

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
saldo = junopy.Balance(resourceToken = '8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9')
```

# Transferência


**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Transferencias)**


### Conta Bancária Padrão
```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
transfer = junopy.transfers.Default(100.0)
```
### Transferência P2P
```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
#P2P(name:str, document:str, amount:float, accountNumber:str)
transfer = junopy.transfers.P2P('Nome', 'CPF/CNPJ', 100.0, 'NUMERO_CONTA_2P')
```

### Transferência Bancária
```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
#Bank(name:str, document:str, amount:float, bank:BankAccount)

conta_bancaria =  junopy.BankAccount()
conta_bancaria.bankNumber = "000"
conta_bancaria.agencyNumber = "1111"
conta_bancaria.accountNumber = "22334455"
conta_bancaria.accountComplementNumber = "0"
conta_bancaria.accountType = "CHECKING"
transfer = junopy.transfers.Bank('Nome', 'CPF/CNPJ', 100.0, conta_bancaria)
```


### Transferência PIX
```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
#Pix(name:str, document:str, amount:float, bank:BankAccount)
transfer = junopy.transfers.Pix('Nome', 'CPF/CNPJ', 100.0, junopy.BankAccount(
	ispb='0000000',
	bankNumber="000",
	agencyNumber="1111",
	accountNumber="22334455",
	accountComplementNumber="0",
	accountType="SAVINGS"
}))
```

# Notificações

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Notificacoes)**


### Listar Tipos de Eventos

Retorna uma lista de objetos `EventType`

| Tipo de Evento | Descrição |
|--|--|
| DIGITAL_ACCOUNT_STATUS_CHANGED | Mudanças de  _status_  de uma conta digital |
| DIGITAL_ACCOUNT_CREATED | Confirmação de criação de uma conta digital -  **Válido somente para a solução Whitelabel** |
| DOCUMENT_STATUS_CHANGED | Mudanças de  _status_  de um documento da conta digital |
| TRANSFER_STATUS_CHANGED | Mudanças de  _status_  de uma transferência |
| P2P_TRANSFER_STATUS_CHANGED | Mudanças de  _status_  de uma transferência P2P |
| CHARGE_STATUS_CHANGED | Mudanças de  _status_  de uma cobrança emitida |
| CHARGE_READ_CONFIRMATION | Confirmação de leitura/visualização de uma cobrança |
| PAYMENT_NOTIFICATION | Pagamento de uma cobranças |

```python
import junopy
events = junopy.EventTypes()
```
# Webhooks
**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#operation/createWebhook)**

### Criação
Cria e retorna um objeto `Webhook`

```python
import junopy

junopy.Juno('PRIVATE_TOKEN', 'CLIENT_ID', 'CLIENT_SECRET')
#Webhook().Create(url:str, eventTypes:list)
webhook = junopy.Webhook().Create("https://url.segura_recebe_notificacao.com", ["DIGITAL_ACCOUNT_CREATED", "DIGITAL_ACCOUNT_STATUS_CHANGED"])
```

### Listar webhooks

```python
webhooks = junopy.Webhooks()
```

### Consultar Webhooks

```python
webhooks = junopy.Webhook(id='wbh_6D7EF263A2755055').Get()
```

### Atualizar Webhooks

```python
#Webhook().Update(status:str, eventTypes:list)
webhook = junopy.Webhook(id='wbh_6D7EF263A2755055').Update("INACTIVE", ["DIGITAL_ACCOUNT_CREATED", "DIGITAL_ACCOUNT_STATUS_CHANGED"])
```

### Excluir Webhooks

```python
webhook = junopy.Webhook(id='wbh_6D7EF263A2755055').Delete()
```

# Cobranças
**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#tag/Cobrancas)**

## Criar Cobrança

```python
cobranca = junopy.charges.Create(
            junopy.Charge(
                description = 'Cobrança Teste',
                amount = 10.0,
                paymentTypes = ['BOLETO', 'CREDIT_CARD']
            ),
            junopy.Billing(
                name = 'Nome do Usuário',
                document = 'CPF',
                email = 'email',
                address = junopy.Address(
                    street= 'Rua',
            		number='Numero',
            		complement='Complemento',
            		neighborhood='Bairro',
            		city='Cidade',
            		state='UF',
            		postCode='99999999'
                ),
                phone = '99999199999',
                notify = False
            )
        )
```

O Retorno será uma lista objeto `ChargeResource`


## Listar Cobrança

É possível realizar buscas  utilizando filtros, veja na documentação oficial: [(Documentação)](https://dev.juno.com.br/api/v2#operation/listCharges)

Devolve 20 cobranças por páginas, podendo ser estendido até 100 páginas com `pageSize=100`.

```python
busca = junopy.charges.Search()
```
**ou**
```python
busca = junopy.charges.Search(pageSize=100)
```
**ou**

```python
busca = junopy.charges.Search(createdOnStart='2021-07-10')
```
A partir da primeira busca é possível navegar pelas páginas superiores/inferiores através dos métodos `Next` e `Previous`

**Para avançar:**
```python
proxima = junopy.charges.Next()
```

**Para voltar:**
```python
anterior = junopy.charges.Previous()
```

## Consultar Cobrança

```python
cobranca = junopy.charges.Get(id="chr_8C87D875719FE478195F5AE32309F77B")
```

## Cancelar Cobrança

```python
junopy.charges.Cancel(id="chr_8C87D875719FE478195F5AE32309F77B")
```

## Atualizar Split

```python
junopy.charges.SetSplit(id="chr_8C87D875719FE478195F5AE32309F77B", split=[
        junopy.Split(
            recipientToken = "Token",
            amount = 10.0,
            amountRemainder = True,
            chargeFee= True),
        junopy.Split(
            recipientToken = "Token2",
            amount = 10.0,
            amountRemainder = False,
            chargeFee= True)
        ])
```

# Checkout Transparente

## Tokenizar Cartão
**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#operation/tokenizeCreditCard)**

```python
cartao_credito = junopy.creditcard.Tokenize(hash="0210da66-6c54-4f3b-9e95-9e044be38d79")
```

## Checkout Transparente
**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#operation/createPayment)**

```python

    # CRIAÇÃO DE COBRANÇA
    cobranca = junopy.charges.Create(
            junopy.Charge(
                description = 'Produto Exemplo',
                amount = 340.0,
                paymentTypes = ['CREDIT_CARD']
            ),
            junopy.Billing(
                name = 'Usuario Teste',
                document = 'cpf',
                email = 'usuario@email.com.br',
                address = junopy.Address(
                    		street = 'Endereco',
                    		number = 'Numero',
                    		complement = 'Complemento',
                    		neighborhood = 'Bairro',
                    		city = 'Cidade',
                    		state = 'UF',
                    		postCode = '99999999'),
                phone = '99999999999',
                notify = False
            )
        )

    # PROCESSAMENTO DE PAGAMENTO
    if len(cobranca) > 0:
        pagamento = junopy.payment.Create(
            chargeId = cobranca[0].id,
            creditcard =  junopy.CreditCard(
                    creditCardId = '9a453d71-3ec1-44a5-b2f3-0596ced42a35'
                ),
            billing = junopy.Billing(
                    name = 'Usuario Teste',
                    email = 'usuario@email.com.br',
                    address = junopy.Address(
                    		street = 'Endereco',
                    		number = 'Numero',
                    		complement = 'Complemento',
                    		neighborhood = 'Bairro',
                    		city = 'Cidade',
                    		state = 'UF',
                    		postCode = '99999999'),
                    delayed = False
                )
        )

```


## Estornar transações de cartão de crédito
**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#operation/refundPaymenta)**

### Integral
```python
 estorno = junopy.payment.Refund(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08')
```

### Parcial
```python
estorno = junopy.payment.Refund(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08', amount=40.00)
```

### Split
```python
estorno = junopy.payment.Refund(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08', amount=40.00, split=[
		junopy.Split(
            recipientToken="Token",
            amount=10.0,
            amountRemainder=True,
            chargeFee=True),
        junopy.Split(
            recipientToken="Token2",
            amount=10.0,
            amountRemainder=False,
            chargeFee=True)])
```

## Capturar pagamento de cartão de crédito

**Mais detalhes em [Documentação Oficial](https://dev.juno.com.br/api/v2#operation/capturePayment)**


### Integral
```python
 captura = junopy.payment.Capture(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08')
```

### Parcial
```python
captura = junopy.payment.Capture(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08', amount=100.00)
```

# Planos e Assinaturas

## Planos

### Criar Plano

```python
plano = junopy.Plan(name="Plano Teste", amount=100.00).Create()
```


### Consultar Plano

```python
plano = junopy.Plan(id='pln_76A6AC4929EF068B').Get()
```

### Listar Plano

```python
planos = junopy.Plan().Get()
```


### Desativar Plano

```python
plano = junopy.Plan(id='pln_76A6AC4929EF068B').Deactivate()
```

### Reativar Plano

```python
plano = junopy.Plan(id='pln_76A6AC4929EF068B').Reactivate()
```

## Assinaturas

### Criar Assinatura

```python
assinatura = junopy.Subscription(
        dueDay=10,
        planId='pln_76A6AC4929EF068B',
        chargeDescription='Assinatura Recorrente Plano de Teste',
        creditCardDetails=junopy.CreditCard(
            creditCardId='9a453d71-3ec1-44a5-b2f3-0596ced42a35'
        ),
        billing=junopy.Billing(
            name='Usuario Teste',
            document='cpf',
            email='usuario@email.com.br',
            address=junopy.Address(
                street='Rua',
                number='numero',
                complement='completemento',
                neighborhood='bairro',
                city='cidade',
                state='UF',
                postCode='99999999')),
            notify=False
    ).Create()
```


### Consultar Assinatura

```python
assinatura = junopy.Subscription(id='sub_EDA3F6CA13DFEC4C').Get()
```

### Listar Assinaturas

```python
assinaturas = junopy.Subscription().Get()
```

### Desativar Assinatura

```python
assinatura = junopy.Subscription(id='sub_EDA3F6CA13DFEC4C').Deactivate()
```

### Reativar Assinatura

```python
assinatura = junopy.Subscription(id='sub_EDA3F6CA13DFEC4C').Reactivate()
```

### Cancelar Assinatura

```python
assinatura = junopy.Subscription(id='sub_EDA3F6CA13DFEC4C').Cancel()
```

### Completar Assinatura

```python
assinatura = junopy.Subscription(id='sub_EDA3F6CA13DFEC4C').Complete()
```

# Pagar Contas


```python
pagamento_conta = junopy.Bill(
        numericalBarCode="00190500954014481606906809350314337370000001000",
        paymentDescription="Boleto Bancário",
        beneficiaryDocument="CPF/CNPJ",
        dueDate="2021-07-12",
        paymentDate="yyyy-MM-dd",
        billAmount=10.00,
        paidAmount=10.00,
    ).Create()
```

# PIX

### Gerar Chave  ( Pix Keys)

```python
# CHAVE GERADA UMA ÚNICA VEZ
uudi = str(uuid.uuid4())
pix = junopy.pix.Keys(idempotency=uudi)
```

### OBTER QR CODE ESTÁTICO

```python
pix = junopy.pix.StaticQRCode(
        idempotency='d63313cd-d01a-4091-b352-182a0a96baca',
        key='06c4e6fe-48cb-4263-89a3-c8bc342ce65e',
        includeImage=True,
        amount=100.00,
        reference='Teste de Pix',
        additionalData='Teste de Pix com Dados Adicionais')
```

# PicPay

EM DESENVOLVIMENTO


## Suporte Oficial da Juno

Em caso de dúvidas, problemas ou sugestões:  [falecom@juno.com.br](mailto:falecom@juno.com.br)

## Change log

Veja em  [CHANGELOG](CHANGELOG.md) para maiores informações sobre as mudanças recentes

## Contribuições

As contribuições  por meio de `Pull Requests` são bem-vindas e serão totalmente creditadas.

## Segurança

Se você descobrir qualquer problema relacionado à segurança, envie um e-mail para robertonsilva@gmail.com

## Créditos

- Autor [Roberto Neves](https://github.com/robertons)

## Licença
Veja em  [LICENÇA](LICENSE) para maiores informações sobre a licença de uso.
