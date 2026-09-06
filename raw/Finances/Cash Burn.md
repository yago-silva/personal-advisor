---
type: note
domain: finances
created: 2026-09-05
updated: 2026-09-06
lang: pt
links:
  - "https://docs.google.com/spreadsheets/d/15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w/"
  - "https://docs.google.com/spreadsheets/d/13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg"
---

# Cash burn — como medir

O valor vive na planilha de fluxo de caixa. Esta nota fixa **como derivá-lo**, porque o total de `Débito` da planilha **não é** o burn.

## O erro de ler o Débito direto

A planilha lança transferências de poupança como `Débito`:

- `Reembolso Reserva de emergência` — aporte na reserva
- `Reembolso Provisão cartões de crédito` — aporte no fundo que cobre a dívida de cartão

As duas **constroem patrimônio**. Somá-las ao burn faz um mês de poupança alta parecer um mês de gasto alto — e foi exatamente o que aconteceu nas leituras anteriores do vault.

## Método

```
burn = Débito total − Reembolso Reserva de emergência − Reembolso Provisão cartões de crédito
```

Ler na planilha [2026 - Planejamento de Gastos](https://docs.google.com/spreadsheets/d/15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w/) via Drive MCP. As abas são `Jan`…`Dez` (nomes curtos — `Janeiro!` não resolve). Totais em `C3:C8`; entradas em `C10:F…`; saídas em `K10:M…`.

## Qual mês usar como referência

Use um **mês de salário puro** — só a entrada `Salário | Yandeh`, sem equity Fluencypass, sem 13º, sem rescisão. Meses com renda extraordinária inflam tanto o aporte na reserva quanto as despesas eventuais, e não representam o regime permanente.

A partir de **nov/2026** todos os meses são assim: a última parcela de equity da Fluencypass cai em out/2026 e o contrato de horas se encerra. Renda passa a ser **fonte única** — um contrato PJ, sem FGTS e sem seguro-desemprego. Isso é o que justifica a reserva, não o conforto.

Ao ler, separe também os **gastos sazonais** do mês (aniversários, presentes de fim de ano, IPVA) para não confundir pico com base.

## Linhas que enganam quem lê o rótulo

Confirmado pelo Yago em **2026-09-06**, depois de uma avaliação que chamou as três de erro. Nenhuma é erro.

- **`Smartfit (Yago)` / `Smartfit (Stephanie)`** — não é academia avulsa. É a **mensalidade do Wellhub** (benefício Yandeh: a empresa dá o acesso, o plano escolhido é pago pelo titular). Não há duplicidade com o benefício — o rótulo é herdado.
- **`Yago Silva Sistemas (ISS) - Equity`** — o imposto é recolhido **no mês seguinte** ao da receita. A linha em `Nov` é o equity de `Out` (parcela 4/4); a de `Set` é a de `Ago`. `Dez` não tem porque `Nov` não teve equity. **A série está correta de ponta a ponta.**
- **`Convênio`** — é o **plano de saúde antigo, mantido de propósito** como ponte até o Yago se sentir seguro na Yandeh. O SulAmérica da Yandeh não tem mensalidade ([[raw/Career/Yandeh/Details|Details]]); o convênio é redundância deliberada, hedge contra o emprego novo não vingar. Zerar em `Nov`/`Dez` é o plano de saída, não inconsistência.

**Regra:** antes de chamar uma linha da planilha de erro, perguntar. Os rótulos são abreviações do Yago, não descrições — e as decisões por trás deles não estavam escritas em lugar nenhum até esta nota.

## Burn de planejamento — R$ 30.000,00/mês (definido em 2026-09-06)

Número que o **Yago fixou** para planejar. Não é a média medida: é a média medida **mais folga para o sazonal**.

Os meses de salário puro rodam abaixo disso. Mas o ano carrega aniversários, presentes de fim de ano, IPVA de dois veículos e manutenção não recorrente, que não aparecem no mês típico — planejar pelo mês típico subestima o ano. Os R$ 30 mil absorvem isso.

Este é um **valor de planejamento datado**, não estado de planilha; por isso fica literal aqui (a convenção nº 5 do `CLAUDE.md` permite premissas de plano e limiares de meta). O burn **medido** continua vivendo na planilha e se recalcula pelo método acima — os dois não devem ser confundidos.

**Revisar quando:** o burn medido cruzar os R$ 30 mil, o Flash/mobilidade for reconciliado (pode derrubar o medido), ou a composição familiar mudar.

## O que a leitura de 2026-09-05 mostrou

- O burn recorrente medido está **mais de 50% acima** da premissa de R$ 17.320,70 usada no replanejamento de mai/2026 — premissa que atravessa [[raw/Plans/Relocation|o plano de relocação]]. Contra o burn de planejamento de R$ 30 mil, a defasagem passa de 70%. Todos os prazos derivados dela estão errados.
- Quase todo o aumento é **provisão discricionária nova** (Saldo Livre por pessoa, provisão Iood, alimentação, suplementos), não custo fixo. É a alavanca mais barata que existe: cortar burn move ao mesmo tempo o quanto sobra por mês **e** o tamanho da meta de reserva.
- A taxa de poupança real de ago–dez/2026 passa de metade das entradas. O saldo mensal perto de zero na planilha não é aperto — é alocação.

## Metas ancoradas no burn

Os alvos são múltiplos do **burn cheio replanejado**, não do essencial — o padrão de vida discricionário faz parte da meta:

| Alvo | Definição | Com o burn de planejamento de 2026-09-06 |
|---|---|---|
| Reserva curto prazo | 1 × burn | R$ 30.000 |
| Reserva médio prazo | 6 × burn | R$ 180.000 |
| Reserva longo prazo | 12 × burn | R$ 360.000 |
| Renda passiva / independência | burn cheio coberto por proventos | R$ 30.000/mês em proventos |

Como os alvos são derivados, **eles se movem quando o burn se move**. A coluna da direita vale enquanto o burn de planejamento for R$ 30 mil — recalcular a cada revisão, nunca reusar um número escrito antes.

Onde a reserva está hoje contra esses alvos: ler `Reserva de Emergência` no `Resumo` do [patrimônio](https://docs.google.com/spreadsheets/d/13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg).

## Achados em aberto (verificar na planilha)

1. **Benefícios Yandeh fora do fluxo** — Flash (R$ 1.100/mês) e auxílio-mobilidade (R$ 360/mês) são termos contratuais ([[raw/Career/Yandeh/Details|Details]]) e **não aparecem como entrada em nenhum mês**. Se o Flash cobre parte do mercado, o burn medido está superestimado; se não é usado, é valor parado. **Maior imprecisão do modelo hoje.**
2. **Duas linhas de `Estacionamento - Moto`** no mesmo mês (uma maior, uma pequena), em set, nov e dez. Dois lugares distintos ou lançamento duplicado? Se forem dois, renomear.
3. **Caixa zero por desenho** — o aporte da reserva é calibrado para zerar o mês na casa das dezenas de reais, e `Caixa` e `Saldo conta de investimento` estão em zero no `Resumo`. Não é falta de dinheiro; é falta de colchão transacional. Qualquer imprevisto vira cartão ou saque da reserva, e sacar da reserva para ruído corrompe o instrumento.
4. **Resultado das saídas da carteira não é registrado** — oito dos onze tickers estão zerados, e a fórmula da planilha marca ROE −100% em toda posição zerada (trata quantidade zero como perda total). Não é o resultado real. **Não existe registro de quanto as oito saídas deram.** Além disso, girar oito posições contradiz a tese buy-and-hold de [[raw/Finances/Investment Thesis|Investment Thesis]] — ou a tese descreve o comportamento, ou precisa ser reescrita.
5. **IPVA e licenciamento de dois veículos** — não aparecem em set-dez e não vi provisão. Caem em janeiro, de uma vez. Confirmar na aba `Jan`.
6. **Parcela do cartão fora do fluxo** — `Cartão Rico` e `Cartão Nubank` estão zerados em todos os meses; a parcela consome a provisão, não o salário. Logo, o fim do parcelamento **não libera fluxo mensal** — libera a provisão. A premissa contrária em [[raw/Plans/Relocation|Relocation]] está incorreta.
7. **Veículos** — carro e moto somam uma fatia relevante da renda bruta em custeio recorrente, e o capital parado neles é grande frente ao que existe de líquido. A moto **está registrada** desde 2026-09-05 como o transporte do Yago para o trabalho ([[raw/Finances/Overview|Overview]] → `Vehicles`), logo o custeio dela é deslocamento, não discricionário. A pergunta em aberto passou a ser qual dos **dois** veículos a família precisa.

## Achados encerrados

- **ISS-Equity em `Nov`** — não era resíduo. Imposto é recolhido no mês seguinte à receita; ver "Linhas que enganam". Encerrado em 2026-09-06.
- **`Convênio` lançado de forma irregular** — não era erro. É o plano-ponte deliberado; ver "Linhas que enganam". Encerrado em 2026-09-06.
